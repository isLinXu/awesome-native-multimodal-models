# 贡献指南

这个仓库有两种内容：**人写的判断** 和 **机器抓的数据**。两者的贡献方式不同。

---

## 1. 推荐一篇论文 / 一个项目

最省事的方式：直接开 Issue，标题写 `[paper] 论文名` 或 `[repo] owner/name`。

请附上：

- arXiv 链接（`https://arxiv.org/abs/XXXX.XXXXX`）或仓库链接
- **一句话说明它属于哪条赛道**，以及为什么值得收
- 赛道 id：`tokenizers` / `unified-ug` / `any-to-any` / `omni` / `pretraining`

维护者会把它加进对应的 `classics`（奠基/必读）或 `github_seed`（长期跟踪）。

如果这是架构上的里程碑模型，请同时改 [`scripts/data.py`](scripts/data.py) 的 `TIMELINE_MODELS` 与 `TAXONOMY_TREE`，然后跑：

```bash
python scripts/validate.py
```

> 请不要直接往 `docs/*.md` 的论文表里手工加行——那些表由脚本维护，
> 手工加的行没有对应的 `data/papers.json` 记录，下次跑脚本可能被截断掉。

## 2. 改进自动分类（收益最大）

分类逻辑全在 [`config/taxonomy.yml`](config/taxonomy.yml)。

| 现象 | 改哪里 |
| :-- | :-- |
| 某类工作总收不进来 | 在对应赛道的 `arxiv_queries` 加查询式，或 `keywords.strong` 加词 |
| 收进来一堆离题的论文 | 加到 `negative`，或把过宽的词从 `strong` 降到 `medium` |
| 赛道之间抢论文 | 调 `keywords` 权重，让该赛道的关键词更「专有」 |
| 某个仓库明显不属于本赛道 | 加到 `github_blocklist` |

`github_blocklist` 是**人工精确剔除**用的：

- 只放你**确定**离题的仓库
- 拿不准的先开 Issue 讨论
- 加的时候**必须写注释说明为什么**

改完请本地验证：

```bash
python scripts/fetch_arxiv.py --dry-run --days 30 --sources arxiv
```

## 3. 加一条新赛道

1. 在 `config/taxonomy.yml` 的 `categories` 下加一块
2. 新建 `docs/<id>.md`，必须包含这段标记块：

```markdown
<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
<!-- table:end classics -->

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
<!-- table:end papers -->
```

3. 在 `README.md` 的赛道表里加一行，并加上对应的 `<!--STATS:cat_id-->` 标记
4. 在 `scripts/render_charts.py` 的 `TRACK_COLORS` 加一行颜色
5. 跑 `python scripts/render_charts.py`，它会生成 sparkline 并插入文档
6. 跑一遍 `python scripts/seed_classics.py && python scripts/fetch_arxiv.py --dry-run`

## 4. 提交前自检

```bash
python scripts/seed_classics.py
python scripts/fetch_arxiv.py --dry-run
python scripts/update_metadata.py --dry-run
python scripts/render_charts.py
python scripts/check_md.py
python scripts/validate.py
```

## 5. 关于「必读」清单的标准

能进 `classics` 的论文，需要满足至少两条：

- 提出了一种**新范式**，而不只是把分数刷高
- 被后续工作**反复引用**为 baseline 或起点
- 定义了一个**被广泛采用的评测方式**
- 对某个开放问题给出了**可复用的分析**

不要提交「我也觉得不错」的增量工作——那个交给自动抓取就够了。

## 6. 代码风格

- 自动跟踪脚本只用 `requests` + `PyYAML`，不引入新依赖
- 所有网络请求走 `common.http_get`（自带指数退避与 4xx 短路）
- 任何一步失败只降级不抛异常，定时任务不能因为单个数据源挂了就全红
- 写文件前先 `write_if_changed` / 幂等判断，避免产生无意义的 diff
