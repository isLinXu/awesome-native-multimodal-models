# 🚀 项目雷达 · GitHub Tracker

> 每日快照 star 数，按 **7 日增速** 排序。增速比总量更能反映「现在大家在做什么」。
> 数据来自 `data/repos.json`（含每个仓库的 star 历史），由 `scripts/track_github.py` 维护。

[← 返回总览](../README.md) · [自动周报](digest.md)

---

## 榜单口径

| 项目 | 说明 |
| :-- | :-- |
| 入选 | 配置中的种子仓库 + 按赛道关键词搜索命中（`stars ≥ 阈值`、近半年有 push、非归档、不在黑名单） |
| 排序 | 7 日 star 增量 → 30 日增量 → 总 star；**快照不足 7 天时用日均增速折算兜底** |
| `≈+N` | **估算值**：按 `总 star ÷ 仓库存活天数 × 7` 折算，不是实测增量，仅供建库首日排序参考 |
| `—` | 该窗口无法计算，也没有估算依据（如缺少创建时间） |
| `🆕` | 仓库创建于近 120 天内 |

> 为什么不用总 star 排？因为总 star 是**存量**，会把多年前的老项目顶在上面；
> 增速是**流量**，才看得出赛道当前的注意力在哪。
>
> 为什么首日要用估算兜底？因为本仓库的快照是逐日累积的，刚建库时所有仓库都只有一天记录，
> 真实 7 日增量算不出来。若此时直接按总 star 排，榜单会退化成「老牌大项目榜」，
> 刚爆发的项目永远上不来。所以用日均速度折算成 7 日估计值顶上，
> **满 7 天后自动切换为真实增量**，估算值随之消失。

## 当前榜单

先看增速，再看明细——条形长度是 7 日 star 增量，颜色是所属赛道：

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/ranking-dark.svg">
  <img src="../assets/ranking-light.svg" alt="项目 star 增速 Top 12">
</picture>

完整名单含语言、赛道、30 日增量：

<!-- table:start repos -->
| 排名 | 项目 | 一句话 | ⭐ | 7 日 Δ | 30 日 Δ | 语言 | 赛道 |
| --: | :-- | :-- | --: | --: | --: | :-- | :-- |
| 1 | [**OpenBMB/MiniCPM-V**](https://github.com/OpenBMB/MiniCPM-V) | See, hear, and interact on your local devices. | ⭐ 27,076 | ≈+187 | — | Python | `omni` |
| 2 | [**QwenLM/Qwen3-VL**](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team… | ⭐ 20,169 | ≈+177 | — | Jupyter Notebook | `pretraining` |
| 3 | [**deepseek-ai/Janus**](https://github.com/deepseek-ai/Janus) | Janus-Series: Unified Multimodal Understanding and Generation Models | ⭐ 17,764 | ≈+166 | — | Python | `unified-ug` |
| 4 | [**openai/CLIP**](https://github.com/openai/CLIP) | CLIP (Contrastive Language-Image Pretraining)… | ⭐ 34,574 | ≈+112 | — | Jupyter Notebook | `pretraining` |
| 5 | [**ByteDance-Seed/Bagel**](https://github.com/ByteDance-Seed/Bagel) | Open-source unified multimodal model | ⭐ 6,209 | ≈+77 | — | Python | `unified-ug` |
| 6 | [**QwenLM/Qwen3-Omni**](https://github.com/QwenLM/Qwen3-Omni) | Qwen3-omni is a natively end-to-end, omni-modal LLM developed by the Qwen team… | ⭐ 4,095 | ≈+70 | — | Jupyter Notebook | `any-to-any` |
| 7 | [**OpenGVLab/InternVL**](https://github.com/OpenGVLab/InternVL) | [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-… | ⭐ 10,170 | ≈+66 | — | Python | `pretraining` |
| 8 | [**FoundationVision/VAR**](https://github.com/FoundationVision/VAR) | [NeurIPS 2024 Best Paper Award][GPT beats diffusion🔥] [scaling laws in visual… | ⭐ 8,765 | ≈+65 | — | Jupyter Notebook | `tokenizers` |
| 9 | [**VectorSpaceLab/OmniGen2**](https://github.com/VectorSpaceLab/OmniGen2) | OmniGen2: Exploration to Advanced Multimodal Generation… | ⭐ 4,118 | ≈+56 | — | Jupyter Notebook | `unified-ug` |
| 10 | [**QwenLM/Qwen2.5-Omni**](https://github.com/QwenLM/Qwen2.5-Omni) | Qwen2.5-Omni is an end-to-end multimodal model by Qwen team at Alibaba Cloud… | ⭐ 4,096 | ≈+48 | — | Jupyter Notebook | `omni` |
| 11 | [**baaivision/Emu3**](https://github.com/baaivision/Emu3) | Next-Token Prediction is All You Need | ⭐ 2,454 | ≈+22 | — | Python | `unified-ug` |
| 12 | [**Gen-Verse/MMaDA**](https://github.com/Gen-Verse/MMaDA) | MMaDA - Open-Sourced Multimodal Large Diffusion Language Models (dLLMs with bl… | ⭐ 1,676 | ≈+22 | — | Python | `unified-ug` |
| 13 | [**NExT-GPT/NExT-GPT**](https://github.com/NExT-GPT/NExT-GPT) | Code and models for ICML 2024 paper, NExT-GPT: Any-to-Any Multimodal Large Lan… | ⭐ 3,633 | ≈+22 | — | Python | `any-to-any` |
| 14 | [**VITA-MLLM/VITA**](https://github.com/VITA-MLLM/VITA) | ✨✨[NeurIPS 2025] VITA-1.5: Towards GPT-4o Level Real-Time Vision and Speech In… | ⭐ 2,540 | ≈+22 | — | Python | `omni` |
| 15 | [**CompVis/taming-transformers**](https://github.com/CompVis/taming-transformers) | Taming Transformers for High-Resolution Image Synthesis | ⭐ 6,536 | ≈+21 | — | Jupyter Notebook | `tokenizers` |
| 16 | [**showlab/Show-o**](https://github.com/showlab/Show-o) | [ICLR & NeurIPS 2025] Repository for Show-o series… | ⭐ 1,986 | ≈+17 | — | Python | `unified-ug` |
| 17 | [**FoundationVision/LlamaGen**](https://github.com/FoundationVision/LlamaGen) | Autoregressive Model Beats Diffusion: 🦙 Llama for Scalable Image Generation | ⭐ 1,973 | ≈+16 | — | Python | `tokenizers` |
| 18 | [**bytedance/1d-tokenizer**](https://github.com/bytedance/1d-tokenizer) | This repo contains the code for 1D tokenizer and generator | ⭐ 1,177 | ≈+10 | — | Jupyter Notebook | `tokenizers` |
| 19 | [**FoundationVision/Liquid**](https://github.com/FoundationVision/Liquid) | (Accepted by IJCV) Liquid: Language Models are Scalable and Unified Multi-moda… | ⭐ 640 | ≈+6 | — | Python | `unified-ug` |
| 20 | [**OpenMOSS/AnyGPT**](https://github.com/OpenMOSS/AnyGPT) | A unified multimodal language model based on discrete sequence modeling | ⭐ 889 | ≈+6 | — | Python | `any-to-any` |
| 21 | [**NVlabs/QLIP**](https://github.com/NVlabs/QLIP) | [arXiv: 2502.05178] QLIP: Text-Aligned Visual Tokenization Unifies Auto-Regres… | ⭐ 97 | ≈+1 | — | Jupyter Notebook | `tokenizers` |
<!-- table:end repos -->

## 怎么读这张榜

- **`unified-ug` 拉起来**：通常对应一次开源统一模型发布（Janus / BAGEL / Show-o 这一档）。
- **`omni` 和 `any-to-any` 交叉**：同一仓库可能同时被两条赛道搜到，表格里会打两个标签。
- **`tokenizers` 仓库偏少**：研究密集、工程复现少，是典型的早期特征。
- **增速突然拉起的仓库**，通常对应一次模型发布或一篇高传播度论文，值得点进去看 commit 时间线。

## 想看更细的？

- 每个仓库的完整 star 历史：`data/repos.json` → `repos.<full_name>.history`
- 赛道分布与总量：`data/stats.json`
- 想加仓库：改 `config/taxonomy.yml` 的 `github_seed` 或 `github_queries`，或直接提 Issue。

---

[← 返回总览](../README.md) · [自动周报](digest.md)
