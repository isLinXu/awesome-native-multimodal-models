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
| 1 | [**Tencent/WePocketModel**](https://github.com/Tencent/WePocketModel) 🆕 | A compact, unified multimodal model family with a single shared vision–languag… | ⭐ 167 | ≈+146 | — | Python | `unified-ug` |
| 2 | [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | A framework for efficient model inference with omni-modality models | ⭐ 7,934 | +127 | — | Python | `omni` |
| 3 | [**OpenBMB/MiniCPM-OCR**](https://github.com/OpenBMB/MiniCPM-OCR) 🆕 | Fast, accurate OCR with correctness assessment. | ⭐ 1,033 | +64 | — | TypeScript | `omni` |
| 4 | [**verl-project/verl-omni**](https://github.com/verl-project/verl-omni) | Multimodal RL training framework for diffusion & omni models | ⭐ 1,589 | +58 | — | Python | `omni` |
| 5 | [**modelscope/ms-swift**](https://github.com/modelscope/ms-swift) | Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.8… | ⭐ 16,161 | +46 | — | Python | `omni` |
| 6 | [**jingyaogong/minimind-o**](https://github.com/jingyaogong/minimind-o) | 🎙️ A 0.1B Omni model trained from scratch, capable of listening, speaking… | ⭐ 2,769 | +34 | — | Python | `omni` |
| 7 | [**openai/CLIP**](https://github.com/openai/CLIP) | CLIP (Contrastive Language-Image Pretraining)… | ⭐ 34,653 | +33 | — | Jupyter Notebook | `pretraining` |
| 8 | [**OpenBMB/MiniCPM-V**](https://github.com/OpenBMB/MiniCPM-V) | See, hear, and interact on your local devices. | ⭐ 27,188 | +30 | — | Python | `omni` |
| 9 | [**QwenLM/Qwen3-VL**](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team… | ⭐ 20,250 | +27 | — | Jupyter Notebook | `pretraining` |
| 10 | [**NVlabs/Eagle**](https://github.com/NVlabs/Eagle) | Eagle: Frontier Vision-Language Models with Data-Centric Strategies | ⭐ 3,864 | +11 | — | Python | `pretraining` |
| 11 | [**Sage-PhysicalAI/InternVLA-A-series**](https://github.com/Sage-PhysicalAI/InternVLA-A-series) | InternVLA-A1: Unifying Understanding, Generation… | ⭐ 575 | ≈+9 | — | Python | `pretraining` |
| 12 | [**AIFrontierLab/TorchUMM**](https://github.com/AIFrontierLab/TorchUMM) | A unified multimodal model toolkit (NeurIPS'26) | ⭐ 599 | +8 | — | Python | `unified-ug` |
| 13 | [**Sage-PhysicalAI/InternVLA-M1**](https://github.com/Sage-PhysicalAI/InternVLA-M1) | InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generali… | ⭐ 438 | ≈+7 | — | Python | `pretraining` |
| 14 | [**QwenLM/Qwen3-Omni**](https://github.com/QwenLM/Qwen3-Omni) | Qwen3-omni is a natively end-to-end, omni-modal LLM developed by the Qwen team… | ⭐ 4,122 | +7 | — | Jupyter Notebook | `any-to-any` |
| 15 | [**lucasjinreal/Crane**](https://github.com/lucasjinreal/Crane) | A Pure Rust based LLM, VLM, VLA, TTS, OCR Inference Engine… | ⭐ 536 | +6 | — | Rust | `omni` |
| 16 | [**deepseek-ai/Janus**](https://github.com/deepseek-ai/Janus) | Janus-Series: Unified Multimodal Understanding and Generation Models | ⭐ 17,777 | +5 | — | Python | `unified-ug` |
| 17 | [**ByteDance-Seed/Bagel**](https://github.com/ByteDance-Seed/Bagel) | Open-source unified multimodal model | ⭐ 6,223 | +4 | — | Python | `unified-ug` |
| 18 | [**OpenSenseNova/SenseNova-Vision**](https://github.com/OpenSenseNova/SenseNova-Vision) | Vision as Unified Multimodal Generation | ⭐ 734 | +4 | — | Python | `unified-ug` |
| 19 | [**Tencent-Hunyuan/UniRL**](https://github.com/Tencent-Hunyuan/UniRL) | UniRL is a Framework for Unified Multimodal Model Reinforcement Learning | ⭐ 1,053 | +3 | — | Python | `unified-ug` |
| 20 | [**EvolvingLMMs-Lab/NEO**](https://github.com/EvolvingLMMs-Lab/NEO) | NEO Series: Native Vision-Language Models from First Principles | ⭐ 931 | +3 | — | Python | `pretraining` |
| 21 | [**redai-studio/Relax**](https://github.com/redai-studio/Relax) | An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at… | ⭐ 679 | +3 | — | Python | `omni` |
| 22 | [**OpenSQZ/MiniCPM-V-CookBook**](https://github.com/OpenSQZ/MiniCPM-V-CookBook) | Cook up amazing AI applications effortlessly with MiniCPM / MiniCPM-V / MiniCP… | ⭐ 674 | +3 | — | Python | `omni` |
| 23 | [**NVIDIA-Omniverse/usd-content-agents**](https://github.com/NVIDIA-Omniverse/usd-content-agents) | AI-powered agents for automating 3D content workflows using Vision-Language Mo… | ⭐ 250 | +3 | — | Python | `pretraining` |
| 24 | [**QwenLM/Qwen2.5-Omni**](https://github.com/QwenLM/Qwen2.5-Omni) | Qwen2.5-Omni is an end-to-end multimodal model by Qwen team at Alibaba Cloud… | ⭐ 4,099 | +2 | — | Jupyter Notebook | `omni` |
| 25 | [**showlab/Show-o**](https://github.com/showlab/Show-o) | [ICLR & NeurIPS 2025] Repository for Show-o series… | ⭐ 1,988 | +2 | — | Python | `unified-ug` |
| 26 | [**FoundationVision/Liquid**](https://github.com/FoundationVision/Liquid) | (Accepted by IJCV) Liquid: Language Models are Scalable and Unified Multi-moda… | ⭐ 643 | +2 | — | Python | `unified-ug` |
| 27 | [**jamjamjon/usls**](https://github.com/jamjamjon/usls) | A Rust library integrated with ONNXRuntime… | ⭐ 449 | +2 | — | Rust | `pretraining` |
| 28 | [**kyegomez/ScreenAI**](https://github.com/kyegomez/ScreenAI) | Implementation of the ScreenAI model from the paper: "A Vision-Language Model… | ⭐ 389 | +2 | — | Python | `pretraining` |
| 29 | [**IBM/terramind**](https://github.com/IBM/terramind) | TerraMind is the first any-to-any generative foundation model for Earth Observ… | ⭐ 336 | +2 | — | Jupyter Notebook | `any-to-any` |
| 30 | [**Tencent-Hunyuan/Hunyuan3D-Buffalo1.0**](https://github.com/Tencent-Hunyuan/Hunyuan3D-Buffalo1.0) 🆕 | [Tech Report] A Unified Multimodal Model for Scalable 3D Generation… | ⭐ 263 | +2 | — | — | `unified-ug` |
| 31 | [**XuankunRong/Awesome-LVLM-Safety**](https://github.com/XuankunRong/Awesome-LVLM-Safety) | A curated list of resources dedicated to the safety of Large Vision-Language M… | ⭐ 225 | +2 | — | — | `pretraining` |
| 32 | [**czvvd/PartLLM**](https://github.com/czvvd/PartLLM) 🆕 | [SIGGRAPH Asia 2026 (TOG)] PartLLM: A Unified Multimodal Foundation for 3D Par… | ⭐ 164 | +2 | — | Python | `unified-ug` |
| 33 | [**mstar-project/mstar**](https://github.com/mstar-project/mstar) | A high-performance, universal serving framework for any-to-any models. | ⭐ 117 | +2 | — | Python | `any-to-any` |
| 34 | [**FoundationVision/VAR**](https://github.com/FoundationVision/VAR) | [NeurIPS 2024 Best Paper Award][GPT beats diffusion🔥] [scaling laws in visual… | ⭐ 8,771 | +1 | — | Jupyter Notebook | `tokenizers` |
| 35 | [**InternLM/xtuner**](https://github.com/InternLM/xtuner) | A Next-Generation Training Engine Built for Ultra-Large MoE Models | ⭐ 5,224 | +1 | — | Python | `pretraining` |
| 36 | [**baaivision/Emu3**](https://github.com/baaivision/Emu3) | Next-Token Prediction is All You Need | ⭐ 2,455 | +1 | — | Python | `unified-ug` |
| 37 | [**jd-opensource/JoyAI-Image**](https://github.com/jd-opensource/JoyAI-Image) | JoyAI-Image is the unified multimodal foundation model for image understanding… | ⭐ 2,245 | +1 | — | Python | `unified-ug` |
| 38 | [**1038lab/ComfyUI-QwenVL**](https://github.com/1038lab/ComfyUI-QwenVL) | ComfyUI-QwenVL custom node: Integrates the Qwen-VL series… | ⭐ 932 | +1 | — | Python | `pretraining` |
| 39 | [**EvolvingLMMs-Lab/lmms-engine**](https://github.com/EvolvingLMMs-Lab/lmms-engine) | A simple, unified multimodal models training engine… | ⭐ 835 | +1 | — | Python | `unified-ug` |
| 40 | [**zli12321/Vision-Language-Models-Overview**](https://github.com/zli12321/Vision-Language-Models-Overview) | A most Frontend Collection and survey of vision-language model papers… | ⭐ 734 | +1 | — | HTML | `pretraining` |
| 41 | [**deepgenteam/deepgen**](https://github.com/deepgenteam/deepgen) | A Lightweight Unified Multimodal Model for Advancing Image Generation and Edit… | ⭐ 585 | +1 | — | Python | `unified-ug` |
| 42 | [**OpenBMB/MiniCPM-o-Demo**](https://github.com/OpenBMB/MiniCPM-o-Demo) | Official PyTorch+CUDA Full-functional Web Demo for MiniCPM-o 4.5 | ⭐ 437 | +1 | — | Python | `omni` |
| 43 | [**lifinance/sdk**](https://github.com/lifinance/sdk) | LI.FI - Bridge & DEX aggregation: Any-to-Any Cross-Chain-Swap SDK | ⭐ 266 | +1 | — | TypeScript | `any-to-any` |
| 44 | [**Fr0zenCrane/UniCoT**](https://github.com/Fr0zenCrane/UniCoT) | [ICLR 2026] Uni-CoT: Towards Unified Chain-of-Thought Reasoning Across Text an… | ⭐ 240 | +1 | — | Python | `any-to-any` |
| 45 | [**fyzhang1/FocusGUI**](https://github.com/fyzhang1/FocusGUI) 🆕 | Official code for "Focused Omni-Modal GUI Agents“ | ⭐ 96 | +1 | — | Python | `omni` |
| 46 | [**OpenGVLab/InternVL**](https://github.com/OpenGVLab/InternVL) | [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-… | ⭐ 10,172 | 0 | — | Python | `pretraining` |
| 47 | [**CompVis/taming-transformers**](https://github.com/CompVis/taming-transformers) | Taming Transformers for High-Resolution Image Synthesis | ⭐ 6,533 | 0 | — | Jupyter Notebook | `tokenizers` |
| 48 | [**roboflow/maestro**](https://github.com/roboflow/maestro) | streamline the fine-tuning process for multimodal models: PaliGemma 2… | ⭐ 2,696 | 0 | — | Python | `pretraining` |
| 49 | [**Gen-Verse/MMaDA**](https://github.com/Gen-Verse/MMaDA) | MMaDA - Open-Sourced Multimodal Large Diffusion Language Models (dLLMs with bl… | ⭐ 1,677 | 0 | — | Python | `unified-ug` |
| 50 | [**ZJU4HealthCare/HealthGPT**](https://github.com/ZJU4HealthCare/HealthGPT) | 【ICML 2025 Spotlight】 Official Repo for Paper ‘’HealthGPT : A Medical Large Vi… | ⭐ 1,673 | 0 | — | Python | `pretraining` |
| 51 | [**bytedance/Lance**](https://github.com/bytedance/Lance) | A 3B-active-parameter native unified multimodal model for image and video unde… | ⭐ 1,370 | 0 | — | Python | `unified-ug` |
| 52 | [**bytedance/1d-tokenizer**](https://github.com/bytedance/1d-tokenizer) | This repo contains the code for 1D tokenizer and generator | ⭐ 1,179 | 0 | — | Jupyter Notebook | `tokenizers` |
| 53 | [**OpenMOSS/AnyGPT**](https://github.com/OpenMOSS/AnyGPT) | A unified multimodal language model based on discrete sequence modeling | ⭐ 889 | 0 | — | Python | `any-to-any` `unified-ug` |
| 54 | [**facebookresearch/tuna-2**](https://github.com/facebookresearch/tuna-2) | Official implementation of Tuna-2: Pixel Embeddings Beat Vision Encoders for U… | ⭐ 763 | 0 | — | Python | `unified-ug` |
| 55 | [**gokayfem/ComfyUI_VLM_nodes**](https://github.com/gokayfem/ComfyUI_VLM_nodes) | ComfyUI nodes for vision-language models: Qwen3-VL, Moondream 3, Florence-2… | ⭐ 593 | 0 | — | Python | `pretraining` |
| 56 | [**hustvl/Senna**](https://github.com/hustvl/Senna) | [IJCV 2026] Senna: Bridging Large Vision-Language Models and End-to-End Autono… | ⭐ 559 | 0 | — | Python | `pretraining` |
| 57 | [**KangLiao929/Puffin**](https://github.com/KangLiao929/Puffin) | Puffin Series: Towards Unified Multimodal 3D World Models | ⭐ 519 | 0 | — | Python | `unified-ug` |
| 58 | [**VITA-Group/VLM-3R**](https://github.com/VITA-Group/VLM-3R) | [CVPR 2026] VLM-3R: Vision-Language Models Augmented with Instruction-Aligned… | ⭐ 456 | 0 | — | Python | `pretraining` |
| 59 | [**InternRobotics/InternVLA-M1**](https://github.com/InternRobotics/InternVLA-M1) | InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generali… | ⭐ 438 | 0 | — | Python | `pretraining` |
| 60 | [**GingerCohle/VLMCSHFG**](https://github.com/GingerCohle/VLMCSHFG) | This is the official code repo for "Vision-Language Models Empowered Nighttime… | ⭐ 371 | 0 | — | Python | `pretraining` |
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
