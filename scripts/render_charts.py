#!/usr/bin/env python3
"""把 data/*.json 渲染成 SVG 图表，供 README 与赛道文档内嵌展示。

为什么手写 SVG 而不用 matplotlib：
  1. CI 里不用多装一个几十 MB 的绘图库，requirements.txt 保持两行
  2. 输出是矢量图，任何缩放下都清晰，体积只有几 KB
  3. 配色/布局完全可控，且能同时产出浅色与深色两套（GitHub 用 <picture> 切换）

生成物（assets/ 下）：
  banner-{light,dark}.svg        顶部横幅：项目名 + 关键数字
  trend-{light,dark}.svg         近 12 周论文发布趋势（按赛道堆叠）
  distribution-{light,dark}.svg  赛道论文占比
  spark-<track>-{light,dark}.svg 单赛道迷你趋势线（嵌在赛道文档顶部）

用法：
  python scripts/render_charts.py
  python scripts/render_charts.py --weeks 16 --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from common import DATA, DOCS, ROOT, load_config, log, read_json, write_if_changed

ASSETS = ROOT / "assets"

# ── 配色 ──────────────────────────────────────────────────────────────────────
# 五个赛道各一色，与 scripts/data.py META.categories 对齐。
TRACK_COLORS = {
    "tokenizers": "#4ECDC4",
    "unified-ug": "#FF6B6B",
    "any-to-any": "#A8E6CF",
    "omni": "#DDA0DD",
    "pretraining": "#FAD7A0",
}

THEMES = {
    "light": {
        "bg": "#FFFFFF",
        "panel": "#F8FAFC",
        "fg": "#0F172A",
        "muted": "#64748B",
        "grid": "#E2E8F0",
        "axis": "#CBD5E1",
        "shadow": "#0F172A",
    },
    "dark": {
        "bg": "#0D1117",
        "panel": "#161B22",
        "fg": "#E6EDF3",
        "muted": "#8B949E",
        "grid": "#30363D",
        "axis": "#484F58",
        "shadow": "#000000",
    },
}

FONT = (
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans SC', "
    "'PingFang SC', 'Microsoft YaHei', Roboto, sans-serif"
)


# ── 工具 ──────────────────────────────────────────────────────────────────────
def esc(text: str) -> str:
    """XML 转义。标题里常有 & < > 和引号。"""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def text_width(text: str, size: float) -> float:
    """粗略估算文本宽度：中日韩字符按 1em，其余按 0.55em。

    SVG 没有字体度量，只能估算。宁可估宽一点，避免文字溢出容器。
    """
    w = 0.0
    for ch in text:
        w += size if ord(ch) > 0x2E80 else size * 0.55
    return w


def truncate(text: str, max_px: float, size: float) -> str:
    """按估算宽度截断，超出加省略号。"""
    if text_width(text, size) <= max_px:
        return text
    out = ""
    for ch in text:
        if text_width(out + ch + "…", size) > max_px:
            break
        out += ch
    return out + "…"


def svg_open(width: int, height: int, theme: Dict[str, str], title: str) -> List[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">',
        f"<title>{esc(title)}</title>",
        f'<rect width="{width}" height="{height}" fill="{theme["bg"]}"/>',
        f'<g font-family="{FONT}">',
    ]


def svg_close() -> List[str]:
    return ["</g>", "</svg>", ""]


# ── 数据聚合 ──────────────────────────────────────────────────────────────────
def week_start(d: datetime) -> datetime:
    return (d - timedelta(days=d.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)


def daily_velocity(rec: Dict[str, Any]) -> float:
    """日均 star 增速 = 总 star / 仓库存活天数（与 track_github.py 同一口径）。"""
    created = rec.get("created_at") or ""
    if len(created) != 10:
        return 0.0
    try:
        born = datetime.strptime(created, "%Y-%m-%d")
    except ValueError:
        return 0.0
    age = max((datetime.now(timezone.utc).replace(tzinfo=None) - born).days, 1)
    return int(rec.get("stars") or 0) / age


def load_data(weeks: int) -> Dict[str, Any]:
    config = load_config()
    cats = config["categories"]
    order = [c["id"] for c in cats]
    names = {c["id"]: c["name"] for c in cats}
    emojis = {c["id"]: c.get("emoji", "") for c in cats}

    papers = read_json(DATA / "papers.json", {"papers": {}}).get("papers", {})
    repos = read_json(DATA / "repos.json", {"repos": {}}).get("repos", {})

    # 每周 × 每赛道的论文数
    per_week: Dict[datetime, Counter] = defaultdict(Counter)
    track_total = Counter()
    for rec in papers.values():
        pub = rec.get("published") or ""
        if len(pub) != 10:
            continue
        try:
            dt = datetime.strptime(pub, "%Y-%m-%d")
        except ValueError:
            continue
        bucket = per_week[week_start(dt)]
        for tid in rec.get("categories") or []:
            bucket[tid] += 1
            track_total[tid] += 1

    # 取最近 N 周，并补全中间没有论文的空周（否则 x 轴会跳周）
    if per_week:
        last = max(per_week)
    else:
        last = week_start(datetime.now(timezone.utc).replace(tzinfo=None))
    all_weeks = [last - timedelta(weeks=i) for i in range(weeks - 1, -1, -1)]
    series = {w: per_week.get(w, Counter()) for w in all_weeks}

    stars_total = sum(int(r.get("stars") or 0) for r in repos.values())

    # 项目增速榜：有真实 7 日增量就用它，否则用日均速度折算（与 track_github 的排序口径一致）
    ranking: List[Dict[str, Any]] = []
    for name, rec in repos.items():
        d7 = rec.get("delta_7d")
        vel = daily_velocity(rec)
        effective = d7 if d7 is not None else vel * 7
        ranking.append(
            {
                "name": name,
                "stars": int(rec.get("stars") or 0),
                "delta": int(round(effective)),
                "measured": d7 is not None,
                "track": (rec.get("categories") or [""])[0],
            }
        )
    ranking.sort(key=lambda r: (r["delta"], r["stars"]), reverse=True)

    return {
        "order": order,
        "names": names,
        "emojis": emojis,
        "papers_total": len(papers),
        "repos_total": len(repos),
        "stars_total": stars_total,
        "track_total": track_total,
        "weeks": all_weeks,
        "series": series,
        "ranking": ranking,
    }


# ── 图表 1：横幅 ──────────────────────────────────────────────────────────────
def render_banner(theme_name: str, theme: Dict[str, str], d: Dict[str, Any]) -> str:
    W, H = 1200, 154
    out = svg_open(W, H, theme, "Awesome Native Multimodal Models")

    # 顶部色带：五条赛道拼成一条细线，暗示"五条赛道并列"
    seg = W / len(d["order"])
    for i, tid in enumerate(d["order"]):
        out.append(
            f'<rect x="{i * seg:.1f}" y="0" width="{seg:.1f}" height="5" '
            f'fill="{TRACK_COLORS.get(tid, theme["muted"])}"/>'
        )

    # 左：一句话定位（不重复 h1 的仓库名，避免视觉冗余）
    out.append(
        f'<text x="48" y="62" font-size="27" font-weight="700" fill="{theme["fg"]}" '
        f'letter-spacing="-0.4">原生多模态模型在怎么长出来</text>'
    )
    out.append(
        f'<text x="49" y="88" font-size="13" fill="{theme["muted"]}">'
        f"每天从 arXiv 与 GitHub 抓取 · 打分归类 · 去重排序 · 自动提交</text>"
    )

    # 右：三个关键数字，横排右对齐
    right = W - 48
    stats = [
        (f"{d['papers_total']:,}", "篇论文"),
        (f"{d['repos_total']:,}", "个项目"),
        (f"{d['stars_total'] / 1000:.0f}k", "累计 star"),
    ]
    cell_w = 104
    for i, (value, label) in enumerate(reversed(stats)):
        cx = right - i * cell_w
        out.append(f'<text x="{cx}" y="62" font-size="25" font-weight="700" text-anchor="end" '
                   f'fill="{theme["fg"]}">{esc(value)}</text>')
        out.append(f'<text x="{cx}" y="84" font-size="11" text-anchor="end" '
                   f'fill="{theme["muted"]}">{esc(label)}</text>')

    # 五条赛道小标签
    x = 48.0
    for tid in d["order"]:
        label = f"{d['emojis'].get(tid, '')} {d['names'].get(tid, tid)}".strip()
        color = TRACK_COLORS.get(tid, theme["muted"])
        w = text_width(label, 11) + 24
        out.append(f'<rect x="{x:.1f}" y="110" width="{w:.1f}" height="24" rx="12" '
                   f'fill="{color}" fill-opacity="0.12"/>')
        out.append(f'<circle cx="{x + 11:.1f}" cy="122" r="3.2" fill="{color}"/>')
        out.append(f'<text x="{x + 19:.1f}" y="126.5" font-size="11" fill="{color}">{esc(label)}</text>')
        x += w + 9

    out += svg_close()
    return "\n".join(out)


# ── 图表 2：周度趋势（堆叠柱） ────────────────────────────────────────────────
def render_trend(theme_name: str, theme: Dict[str, str], d: Dict[str, Any]) -> str:
    W, H = 1200, 330
    left, right, top, bottom = 64, 32, 74, 56
    plot_w, plot_h = W - left - right, H - top - bottom
    weeks: List[datetime] = d["weeks"]
    series = d["series"]

    # y 轴上限：取整到 20 的倍数，保证 4 条网格线落在整数上
    peak = max((sum(c.values()) for c in series.values()), default=0)
    step = max(20, ((peak // 20) + 1) * 20 / 4)
    y_max = step * 4

    out = svg_open(W, H, theme, "近 12 周论文发布趋势")
    out.append(f'<text x="{left}" y="34" font-size="16" font-weight="600" fill="{theme["fg"]}">'
               f"近 {len(weeks)} 周论文发布趋势</text>")
    out.append(f'<text x="{left}" y="56" font-size="12" fill="{theme["muted"]}">'
               f"按赛道堆叠 · 数据来自 arXiv，每周一为起点</text>")

    # 网格 + y 轴刻度
    for i in range(5):
        y = top + plot_h - plot_h * i / 4
        out.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" '
                   f'stroke="{theme["grid"]}" stroke-width="1"/>')
        out.append(f'<text x="{left - 12}" y="{y + 4:.1f}" font-size="11" text-anchor="end" '
                   f'fill="{theme["muted"]}">{int(step * i)}</text>')

    # 柱子
    n = len(weeks)
    slot = plot_w / n
    bar_w = min(slot * 0.58, 46)
    for idx, wk in enumerate(weeks):
        cx = left + slot * (idx + 0.5)
        x0 = cx - bar_w / 2
        cursor = top + plot_h
        counts = series[wk]
        total = sum(counts.values())
        for tid in d["order"]:
            v = counts.get(tid, 0)
            if not v:
                continue
            h = plot_h * v / y_max
            cursor -= h
            # 顶部留 1px 缝隙，堆叠段之间才有分隔感
            out.append(f'<rect x="{x0:.1f}" y="{cursor + (1 if h > 3 else 0):.1f}" '
                       f'width="{bar_w:.1f}" height="{max(h - 1, 1):.1f}" '
                       f'fill="{TRACK_COLORS.get(tid, theme["muted"])}"/>')
        # 柱顶总数
        if total:
            out.append(f'<text x="{cx:.1f}" y="{cursor - 7:.1f}" font-size="11" text-anchor="middle" '
                       f'fill="{theme["muted"]}">{total}</text>')
        # x 轴标签：每两周一个，避免拥挤
        if idx % 2 == 0 or idx == n - 1:
            out.append(f'<text x="{cx:.1f}" y="{top + plot_h + 22}" font-size="11" '
                       f'text-anchor="middle" fill="{theme["muted"]}">{wk:%m/%d}</text>')

    # 基线
    out.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" '
               f'stroke="{theme["axis"]}" stroke-width="1"/>')

    # 图例（右上）
    lx = W - right
    for tid in reversed(d["order"]):
        label = d["names"].get(tid, tid)
        w = text_width(label, 11) + 22
        lx -= w + 16
        out.append(f'<rect x="{lx:.1f}" y="28" width="9" height="9" rx="2" '
                   f'fill="{TRACK_COLORS.get(tid, theme["muted"])}"/>')
        out.append(f'<text x="{lx + 14:.1f}" y="36" font-size="11" fill="{theme["muted"]}">'
                   f"{esc(label)}</text>")

    out += svg_close()
    return "\n".join(out)


# ── 图表 3：赛道占比（横向条形） ──────────────────────────────────────────────
def render_distribution(theme_name: str, theme: Dict[str, str], d: Dict[str, Any]) -> str:
    W = 1200
    row_h, gap = 44, 10
    top = 62
    H = top + len(d["order"]) * (row_h + gap) + 16
    name_w, value_w = 250, 130
    bar_x = 24 + name_w
    bar_w = W - bar_x - value_w - 32

    total = sum(d["track_total"].values()) or 1
    out = svg_open(W, H, theme, "赛道论文分布")
    out.append(f'<text x="24" y="32" font-size="16" font-weight="600" fill="{theme["fg"]}">'
               f"五条赛道的论文占比</text>")
    out.append(f'<text x="24" y="52" font-size="12" fill="{theme["muted"]}">'
               f"共 {d['papers_total']:,} 篇 · 一篇论文可同时属于多条赛道</text>")

    peak = max(d["track_total"].values(), default=1)
    for i, tid in enumerate(d["order"]):
        y = top + i * (row_h + gap)
        color = TRACK_COLORS.get(tid, theme["muted"])
        count = d["track_total"].get(tid, 0)
        label = f"{d['emojis'].get(tid, '')} {d['names'].get(tid, tid)}".strip()

        out.append(f'<text x="24" y="{y + 27}" font-size="13" fill="{theme["fg"]}">'
                   f"{esc(truncate(label, name_w - 16, 13))}</text>")
        # 轨道底色 + 数据条
        out.append(f'<rect x="{bar_x}" y="{y + 12}" width="{bar_w}" height="20" rx="6" '
                   f'fill="{theme["grid"]}" fill-opacity="0.55"/>')
        w = max(bar_w * count / peak, 4)
        out.append(f'<rect x="{bar_x}" y="{y + 12}" width="{w:.1f}" height="20" rx="6" fill="{color}"/>')
        out.append(f'<text x="{bar_x + bar_w + 56}" y="{y + 27}" font-size="13" font-weight="600" '
                   f'text-anchor="end" fill="{theme["fg"]}">{count}</text>')
        out.append(f'<text x="{bar_x + bar_w + 116}" y="{y + 27}" font-size="12" '
                   f'text-anchor="end" fill="{theme["muted"]}">{count / total * 100:.0f}%</text>')

    out += svg_close()
    return "\n".join(out)


# ── 图表 4：项目增速榜（横向条形） ────────────────────────────────────────────
def render_ranking(theme_name: str, theme: Dict[str, str], d: Dict[str, Any], top: int = 12) -> str:
    rows = d["ranking"][:top]
    W = 1200
    row_h = 30
    top_pad = 62
    H = top_pad + len(rows) * row_h + 14
    name_w = 240
    bar_x = 24 + name_w
    bar_w = W - bar_x - 130

    peak = max((r["delta"] for r in rows), default=1) or 1
    out = svg_open(W, H, theme, "项目 star 增速榜")
    out.append(f'<text x="24" y="30" font-size="16" font-weight="600" fill="{theme["fg"]}">'
               f"项目 star 增速 Top {len(rows)}</text>")
    out.append(f'<text x="24" y="50" font-size="12" fill="{theme["muted"]}">'
               f"快照满 7 天后为实测增量；不足 7 天按日均速度折算（与项目雷达表格同口径）</text>")

    for i, r in enumerate(rows):
        y = top_pad + i * row_h
        color = TRACK_COLORS.get(r["track"], theme["muted"])
        out.append(f'<text x="24" y="{y + 17}" font-size="12" fill="{theme["fg"]}">'
                   f'{esc(truncate(r["name"], name_w - 12, 12))}</text>')
        out.append(f'<rect x="{bar_x}" y="{y + 6}" width="{bar_w}" height="16" rx="5" '
                   f'fill="{theme["grid"]}" fill-opacity="0.5"/>')
        w = max(bar_w * r["delta"] / peak, 3)
        out.append(f'<rect x="{bar_x}" y="{y + 6}" width="{w:.1f}" height="16" rx="5" fill="{color}"/>')
        out.append(f'<text x="{W - 24}" y="{y + 17}" font-size="12" font-weight="600" '
                   f'text-anchor="end" fill="{theme["fg"]}">+{r["delta"]:,}</text>')

    out += svg_close()
    return "\n".join(out)


# ── 图表 5：单赛道迷你趋势线 ──────────────────────────────────────────────────
def render_spark(theme_name: str, theme: Dict[str, str], d: Dict[str, Any], track_id: str) -> str:
    W, H = 900, 96
    pad_l, pad_r, pad_t, pad_b = 8, 8, 22, 20
    plot_w, plot_h = W - pad_l - pad_r, H - pad_t - pad_b
    color = TRACK_COLORS.get(track_id, theme["muted"])
    weeks = d["weeks"]
    values = [d["series"][w].get(track_id, 0) for w in weeks]
    peak = max(values) or 1

    out = svg_open(W, H, theme, f"{track_id} 周度趋势")
    pts = []
    for i, v in enumerate(values):
        x = pad_l + plot_w * (i / max(len(values) - 1, 1))
        y = pad_t + plot_h - plot_h * (v / peak)
        pts.append((x, y))

    # 面积填充 + 折线
    if pts:
        area = (
            f"M {pts[0][0]:.1f},{pad_t + plot_h:.1f} "
            + " ".join(f"L {x:.1f},{y:.1f}" for x, y in pts)
            + f" L {pts[-1][0]:.1f},{pad_t + plot_h:.1f} Z"
        )
        out.append(f'<path d="{area}" fill="{color}" fill-opacity="0.14"/>')
        line = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        out.append(f'<path d="{line}" fill="none" stroke="{color}" stroke-width="2.2" '
                   f'stroke-linejoin="round" stroke-linecap="round"/>')
        # 末点高亮
        out.append(f'<circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="3.4" fill="{color}"/>')

    out.append(f'<text x="{pad_l}" y="14" font-size="11" fill="{theme["muted"]}">'
               f"近 {len(weeks)} 周本赛道论文发布 · 峰值 {peak} 篇/周</text>")
    out.append(f'<text x="{W - pad_r}" y="14" font-size="11" text-anchor="end" '
               f'fill="{theme["muted"]}">{weeks[0]:%m/%d} → {weeks[-1]:%m/%d}</text>')

    out += svg_close()
    return "\n".join(out)


# ── 入口 ──────────────────────────────────────────────────────────────────────
def main() -> int:
    parser = argparse.ArgumentParser(description="渲染 SVG 图表")
    parser.add_argument("--weeks", type=int, default=12, help="趋势图回溯周数")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    d = load_data(args.weeks)
    if not d["papers_total"] and not d["repos_total"]:
        log("没有数据，跳过渲染（首次建库后会自动出现）")
        return 0

    if not ASSETS.is_dir():
        ASSETS.mkdir(parents=True)
    jobs: List[Tuple[str, Any]] = []
    for theme_name, theme in THEMES.items():
        jobs.append((f"banner-{theme_name}.svg", render_banner(theme_name, theme, d)))
        jobs.append((f"trend-{theme_name}.svg", render_trend(theme_name, theme, d)))
        jobs.append((f"distribution-{theme_name}.svg", render_distribution(theme_name, theme, d)))
        jobs.append((f"ranking-{theme_name}.svg", render_ranking(theme_name, theme, d)))
        for tid in d["order"]:
            jobs.append((f"spark-{tid}-{theme_name}.svg", render_spark(theme_name, theme, d, tid)))

    changed = 0
    for name, svg in jobs:
        path = ASSETS / name
        if args.dry_run:
            log(f"  [dry-run] {name}  {len(svg):,} 字节")
            continue
        if write_if_changed(path, svg):
            changed += 1

    log(f"渲染完成：{len(jobs)} 个 SVG，其中 {changed} 个有变更")
    log(f"  近 {args.weeks} 周论文 {sum(sum(c.values()) for c in d['series'].values()):,} 篇（含跨赛道重复计）")

    synced = sync_docs(d, dry_run=args.dry_run)
    if synced:
        log(f"文档引用：新插入 {synced} 处 sparkline（新增赛道时自动补齐）")
    return 0


def sync_docs(d: Dict[str, Any], dry_run: bool = False) -> int:
    """确保每个赛道文档顶部都有本赛道的 sparkline 引用块。

    幂等：已有引用就跳过。这样新增赛道时不必手写 <picture>，
    跑一次脚本就把图生成 + 文档接入一起做完了。
    """
    config = load_config()
    inserted = 0
    for cat in config["categories"]:
        cid = cat["id"]
        if cid not in d["order"]:
            continue
        doc = DOCS / Path(cat["doc"]).name
        if not doc.exists():
            continue
        text = doc.read_text(encoding="utf-8")
        if f"spark-{cid}-light.svg" in text:
            continue
        block = (
            "<picture>\n"
            f'  <source media="(prefers-color-scheme: dark)" srcset="../assets/spark-{cid}-dark.svg">\n'
            f'  <img src="../assets/spark-{cid}-light.svg" alt="{cat["name"]} 近 12 周论文发布趋势">\n'
            "</picture>\n\n"
        )
        # 插在导航行（以 [← 开头）之前，保持"标题 → 定位 → 图 → 导航"的顺序
        m = re.search(r"^\[←", text, re.M)
        if not m:
            log(f"  [skip] {doc.name} 找不到导航行，未插入 sparkline")
            continue
        if dry_run:
            log(f"  [dry-run] 将向 {doc.name} 插入 sparkline")
        else:
            doc.write_text(text[: m.start()] + block + text[m.start() :], encoding="utf-8")
        inserted += 1
    return inserted


if __name__ == "__main__":
    sys.exit(main())
