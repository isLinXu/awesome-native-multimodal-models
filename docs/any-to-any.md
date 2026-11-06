# 🌐 Any-to-Any Multimodal · 任意到任意

> 一句话：**任意模态进，任意模态出。**
> 文本、图像、音频、视频、动作走同一套接口。和 Omni 的差别在于：这里强调生成覆盖面，Omni 强调实时交互。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/spark-any-to-any-dark.svg">
  <img src="../assets/spark-any-to-any-light.svg" alt="Any-to-Any Multimodal 近 12 周论文发布趋势">
</picture>

[← 返回总览](../README.md) · [Omni 实时交互 →](omni.md)

---

## 1. 两种实现

| 路线 | 做法 | 代表 | 上限 |
| :-- | :-- | :-- | :-- |
| **可组合扩散** | 各模态 latent 在共享空间对齐，按需组合 | CoDi, CoDi-2, OmniFlow | 交互弱，更像生成器 |
| **离散 AR 全模态** | 所有模态都变成 token，LLM 统一解码 | NExT-GPT, AnyGPT, MIO, Qwen3-Omni | 依赖各模态 tokenizer 质量 |
| **Omni-AR 满模态** | 再把动作、3D、多轮对话接进去 | Unified-IO 2, Ming-Omni | 数据配比和评测都还没统一 |

## 2. 🏛 奠基与必读

> 由 `scripts/seed_classics.py` 按 arXiv ID 校验后自动填充；ID 失效会自动剔除，不留死链。

<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2023-05-19 | **Any-to-Any Generation via Composable Diffusion** | Zineng Tang, Ziyi Yang et al. | CoDi：用可组合扩散第一次把 any-to-any 做成统一接口 | [📄 2305.11846](https://arxiv.org/abs/2305.11846) |
| 2023-09-11 | **NExT-GPT: Any-to-Any Multimodal LLM** | Shengqiong Wu, Hao Fei et al. | NExT-GPT：把 LLM 接到任意模态编解码器上的开源范式 | [📄 2309.05519](https://arxiv.org/abs/2309.05519) |
| 2024-02-19 | **AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling** | Jun Zhan, Junqi Dai et al. | AnyGPT：离散序列建模把多模态压进同一套 token | [📄 2402.12226](https://arxiv.org/abs/2402.12226) |
| 2025-05-05 | **Ming-Lite-Uni: Advancements in Unified Architecture for Natural Multimodal Interaction** | Inclusion AI, Biao Gong et al. | Ming-Lite-Uni：统一视觉生成器 + native 多模态 AR，Any-to-Any 的 2025 开源代表 | [📄 2505.02471](https://arxiv.org/abs/2505.02471) |
<!-- table:end classics -->

## 3. 📄 自动跟踪的最新论文

> 每日由 GitHub Actions 从 arXiv 抓取、打分、去重后写入；按提交日期倒序，表内最多保留 200 条，更早的仍留在 `data/papers.json`。

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2026-11-03 | **DreamX: Video Diffusion Model is a Universal Latent Action Learner** | Jisoo Kim, Chaehyun Kim et al. | Learning a universal action representation from video requires modeling dynamics that are consi… | [📄 2611.05377](https://arxiv.org/abs/2611.05377) `cs.CV` |
| 2026-10-30 | **scAnyOmics: Foundation-Model Distillation for Any-to-Any Completion of Multi-omics Virtual Cells** | Zhaoqi Song, Ye Du et al. | Recent advances in single-cell technologies have enabled the profiling of multiple molecular mo… | [📄 2610.41399](https://arxiv.org/abs/2610.41399) `cs.AI` |
| 2025-12-01 | **OmniFlow** | — | Omni flow for any-to-any generation | [📄 2412.01169](https://arxiv.org/abs/2412.01169) `catalog` |
| 2025-10-01 | **InteractiveOmni-A2A** | — | Unified omni-modal model for audio-visual multi-turn any-to-any dialogue | [📄 2510.13747](https://arxiv.org/abs/2510.13747) `catalog` |
| 2025-09-01 | **Qwen3-Omni** | — | Qwen3 omni model | [📄 2509.17765](https://arxiv.org/abs/2509.17765) `catalog` |
| 2025-05-01 | **Ming-Omni** | — | Ming all-modal omni model | [📄 2505.02471](https://arxiv.org/abs/2505.02471) `catalog` |
| 2025-02-01 | **M2-omni** | — | M2 omni multimodal model | [📄 2502.18778](https://arxiv.org/abs/2502.18778) `catalog` |
| 2025-01-01 | **Spider** | — | Spider any-to-any model | [📄 2501.03461](https://arxiv.org/abs/2501.03461) `catalog` |
| 2024-09-01 | **MIO** | — | Multimodal interleaved output model | [📄 2409.17692](https://arxiv.org/abs/2409.17692) `catalog` |
| 2024-05-01 | **X-VILA** | — | Cross-modality alignment extending VILA to any-to-any multimodal generation | [📄 2405.19335](https://arxiv.org/abs/2405.19335) `catalog` |
| 2024-03-01 | **Unified-IO 2** | — | Unified I/O for diverse tasks | [📄 2312.17172](https://arxiv.org/abs/2312.17172) `catalog` |
| 2024-02-01 | **AnyGPT** | — | Unified multimodal LLM with discrete sequence modeling | [📄 2402.12226](https://arxiv.org/abs/2402.12226) `catalog` |
| 2024-01-01 | **CoDi-2** | — | Improved CoDi with in-context generation | [📄 2311.18775](https://arxiv.org/abs/2311.18775) `catalog` |
| 2023-09-01 | **NExT-GPT** | — | Any-to-any multimodal LLM | [📄 2309.05519](https://arxiv.org/abs/2309.05519) `catalog` |
| 2023-05-01 | **CoDi** | — | Any-to-any generation via composable diffusion | [📄 2305.11846](https://arxiv.org/abs/2305.11846) `catalog` |
<!-- table:end papers -->
