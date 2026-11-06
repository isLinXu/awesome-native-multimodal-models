# 🎙️ Omni Models · Omni 实时交互

> 一句话：**能看、能听、能说，而且要跟得上。**
> 目标不是「多一个生成头」，而是 GPT-4o 那一档全双工体验：低延迟、可打断、多模态同时在线。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/spark-omni-dark.svg">
  <img src="../assets/spark-omni-light.svg" alt="Omni Models 近 12 周论文发布趋势">
</picture>

[← 返回总览](../README.md) · [预训练底座 →](pretraining.md)

---

## 1. 和 Any-to-Any 怎么分

| | Any-to-Any | Omni |
| :-- | :-- | :-- |
| 核心问题 | 模态覆盖全不全 | 交互是不是实时、全双工 |
| 典型能力 | 文→图、图→音、视频→文 | 边看边听边说，可打断 |
| 代表 | CoDi, NExT-GPT, AnyGPT | GPT-4o, Qwen2.5-Omni, MiniCPM-o, VITA |

闭源模型（GPT-4o / Gemini）往往没有 arXiv ID，自动抓取会漏。它们被记在 `scripts/data.py` 的时间线里，不进这篇的论文表。

## 2. 🏛 奠基与必读

> 由 `scripts/seed_classics.py` 按 arXiv ID 校验后自动填充；ID 失效会自动剔除，不留死链。

<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2024-08-09 | **VITA: Towards Open-Source Interactive Omni Multimodal LLM** | Chaoyou Fu, Haojia Lin et al. | VITA：开源交互式 Omni 的早期代表，把语音+视觉拉进同一对话循环 | [📄 2408.05211](https://arxiv.org/abs/2408.05211) |
| 2025-03-26 | **Qwen2.5-Omni Technical Report** | Jin Xu, Zhifang Guo et al. | Qwen2.5-Omni：开源 Omni 的标杆技术报告 | [📄 2503.20215](https://arxiv.org/abs/2503.20215) |
| 2025-09-22 | **Qwen3-Omni Technical Report** | Jin Xu, Zhifang Guo et al. | Qwen3-Omni：Thinker-Talker MoE，把 Omni 从交互推进到更强的统一建模 | [📄 2509.17765](https://arxiv.org/abs/2509.17765) |
<!-- table:end classics -->

## 3. 📄 自动跟踪的最新论文

> 每日由 GitHub Actions 从 arXiv 抓取、打分、去重后写入；按提交日期倒序，表内最多保留 200 条，更早的仍留在 `data/papers.json`。

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2026-11-05 | **THG-Omni: Traceable Human-Centric Graph Supervision for Video Reasoning** | Jisheng Dang, Kai Wei et al. | Omni-modal models can answer questions about video… | [📄 2611.07836](https://arxiv.org/abs/2611.07836) `cs.CV` |
| 2026-11-04 | **CRESiST: Self-Enhancing Explorative Policy Learning for Simultaneous Speech Translation** | Chenyang Le, Pei Zhang et al. | Simultaneous Speech Translation (SimulST) requires balancing translation quality and latency… | [📄 2611.06501](https://arxiv.org/abs/2611.06501) `cs.CL` |
| 2026-11-04 | **SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?** | Peiran Wu, Fangfei Gou et al. | Omni models answer questions about videos by jointly processing sampled frames and audio in one… | [📄 2611.06083](https://arxiv.org/abs/2611.06083) `cs.CV` |
| 2026-11-04 | **PatchCon: Patch-aware Weighted Supervised Contrastive Learning for Vulnerability Detection** | Chaomeng Lu, Pooya Rostami Mazrae et al. | Automated vulnerability detection is critical for securing modern software systems… | [📄 2611.06583](https://arxiv.org/abs/2611.06583) `cs.SE` |
| 2026-11-03 | **Confidence-Aware Aggregation for Multimodal Audio Reasoning** | Michel Olvera, Paraskevas Stamatiadis et al. | Large Audio Language Models (LALMs) enable generative reasoning over complex acoustic scenes bu… | [📄 2611.04580](https://arxiv.org/abs/2611.04580) `cs.SD` |
| 2026-11-03 | **How Do Artificial Agents Make Decisions in Light of Visual Data?** | Keyty Loza, Shayan Monadjemi | Vision-language models (VLMs) have demonstrated significant advances in reasoning with visual d… | [📄 2611.05671](https://arxiv.org/abs/2611.05671) `cs.AI` |
| 2026-11-03 | **TSFM Meets LLM: Context as Covariates** | Hemanth Ram, Sai Shankar Narasimhan et al. | Textual information is ubiquitous in real-world time series datasets, appearing as news… | [📄 2611.05515](https://arxiv.org/abs/2611.05515) `cs.LG` |
| 2026-11-03 | **Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems** | Pengfei Zhou, Yixing Ma et al. | Artificial general intelligence (AGI) requires a method that can understand, generate, reason… | [📄 2611.05275](https://arxiv.org/abs/2611.05275) `cs.CV` |
| 2026-11-02 | **InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems** | Richard Yucheng He, Chen Xu et al. | Most benchmarks for real-time voice systems focus on one aspect, such as turn-taking… | [📄 2611.02430](https://arxiv.org/abs/2611.02430) `cs.SD` |
| 2026-11-02 | **R$^2$-Omni: Reducing Structural and Precision Redundancy in Omni-LLMs for Long-Form Generation** | Bolong Feng, Pengfei Zhou et al. | Omni-modal large language models (Omni-LLMs) typically process large numbers of multimodal toke… | [📄 2611.03247](https://arxiv.org/abs/2611.03247) `cs.CV` |
| 2026-10-30 | **RECITE: Revising Eligibility Criteria Incorporating Textual Evidence** | Russell Ro, Reza Abbasi-Asl | Overly restrictive eligibility criteria contribute to widespread enrollment failure in clinical… | [📄 2610.41368](https://arxiv.org/abs/2610.41368) `cs.AI` |
| 2025-11-01 | **MiniCPM-o 4.5** | — | MiniCPM omni 4.5 - enhanced | [📄 2511.07905](https://arxiv.org/abs/2511.07905) `catalog` |
| 2025-06-01 | **NExT-OMNI** | — | NExT-OMNI all-modal model | [📄 2506.08838](https://arxiv.org/abs/2506.08838) `catalog` |
| 2025-03-01 | **Qwen2.5-Omni** | — | Qwen2.5 omnivore multimodal model | [📄 2503.20215](https://arxiv.org/abs/2503.20215) `catalog` |
| 2025-03-01 | **InteractiveOmni** | — | Interactive omni model | [📄 2503.17366](https://arxiv.org/abs/2503.17366) `catalog` |
| 2025-01-01 | **VITA-1.5** | — | VITA 1.5 with improved capabilities | [📄 2501.12599](https://arxiv.org/abs/2501.12599) `catalog` |
| 2025-01-01 | **SALMONN-Omni** | — | Speech audio language music omni model | [📄 2501.10801](https://arxiv.org/abs/2501.10801) `catalog` |
| 2024-09-01 | **LLaMA-Omni** | — | Seamless speech interaction with LLaMA | [📄 2409.06666](https://arxiv.org/abs/2409.06666) `catalog` |
| 2024-08-01 | **VITA** | — | Open-source interactive omni model | [📄 2408.05211](https://arxiv.org/abs/2408.05211) `catalog` |
<!-- table:end papers -->
