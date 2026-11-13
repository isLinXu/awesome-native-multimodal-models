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
| 1 | [**OpenBMB/MiniCPM-OCR**](https://github.com/OpenBMB/MiniCPM-OCR) 🆕 | Fast, accurate OCR with correctness assessment. | ⭐ 912 | ≈+376 | — | TypeScript | `omni` |
| 2 | [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | A framework for efficient model inference with omni-modality models | ⭐ 7,732 | ≈+126 | — | Python | `omni` |
| 3 | [**jingyaogong/minimind-o**](https://github.com/jingyaogong/minimind-o) | 🎙️ A 0.1B Omni model trained from scratch, capable of listening, speaking… | ⭐ 2,717 | ≈+97 | — | Python | `omni` |
| 4 | [**modelscope/ms-swift**](https://github.com/modelscope/ms-swift) | Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.8… | ⭐ 16,099 | ≈+94 | — | Python | `omni` |
| 5 | [**jd-opensource/JoyAI-Image**](https://github.com/jd-opensource/JoyAI-Image) | JoyAI-Image is the unified multimodal foundation model for image understanding… | ⭐ 2,242 | ≈+69 | — | Python | `unified-ug` |
| 6 | [**OpenBMB/MiniCPM-V**](https://github.com/OpenBMB/MiniCPM-V) | See, hear, and interact on your local devices. | ⭐ 27,140 | +64 | — | Python | `omni` |
| 7 | [**bytedance/Lance**](https://github.com/bytedance/Lance) | A 3B-active-parameter native unified multimodal model for image and video unde… | ⭐ 1,366 | ≈+53 | — | Python | `unified-ug` |
| 8 | [**verl-project/verl-omni**](https://github.com/verl-project/verl-omni) | Multimodal RL training framework for diffusion & omni models | ⭐ 1,501 | ≈+51 | — | Python | `omni` |
| 9 | [**Tencent-Hunyuan/UniRL**](https://github.com/Tencent-Hunyuan/UniRL) | UniRL is a Framework for Unified Multimodal Model Reinforcement Learning | ⭐ 1,045 | ≈+46 | — | Python | `unified-ug` |
| 10 | [**QwenLM/Qwen3-VL**](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team… | ⭐ 20,208 | +39 | — | Jupyter Notebook | `pretraining` |
| 11 | [**appletea233/OneSearch-VL**](https://github.com/appletea233/OneSearch-VL) 🆕 | A unified multimodal deep research agent for images and videos… | ⭐ 198 | ≈+38 | — | Python | `unified-ug` |
| 12 | [**OpenSenseNova/SenseNova-Vision**](https://github.com/OpenSenseNova/SenseNova-Vision) | Vision as Unified Multimodal Generation | ⭐ 730 | ≈+37 | — | Python | `unified-ug` |
| 13 | [**NVlabs/Eagle**](https://github.com/NVlabs/Eagle) | Eagle: Frontier Vision-Language Models with Data-Centric Strategies | ⭐ 3,842 | ≈+31 | — | Python | `pretraining` |
| 14 | [**InternLM/xtuner**](https://github.com/InternLM/xtuner) | A Next-Generation Training Engine Built for Ultra-Large MoE Models | ⭐ 5,223 | ≈+30 | — | Python | `pretraining` |
| 15 | [**openai/CLIP**](https://github.com/openai/CLIP) | CLIP (Contrastive Language-Image Pretraining)… | ⭐ 34,603 | +29 | — | Jupyter Notebook | `pretraining` |
| 16 | [**facebookresearch/tuna-2**](https://github.com/facebookresearch/tuna-2) | Official implementation of Tuna-2: Pixel Embeddings Beat Vision Encoders for U… | ⭐ 763 | ≈+26 | — | Python | `unified-ug` |
| 17 | [**redai-studio/Relax**](https://github.com/redai-studio/Relax) | An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at… | ⭐ 676 | ≈+22 | — | Python | `omni` |
| 18 | [**ZJU4HealthCare/HealthGPT**](https://github.com/ZJU4HealthCare/HealthGPT) | 【ICML 2025 Spotlight】 Official Repo for Paper ‘’HealthGPT : A Medical Large Vi… | ⭐ 1,670 | ≈+18 | — | Python | `pretraining` |
| 19 | [**AIFrontierLab/TorchUMM**](https://github.com/AIFrontierLab/TorchUMM) | A unified multimodal model toolkit (NeurIPS'26) | ⭐ 583 | ≈+18 | — | Python | `unified-ug` |
| 20 | [**Tencent-Hunyuan/Hunyuan3D-Buffalo1.0**](https://github.com/Tencent-Hunyuan/Hunyuan3D-Buffalo1.0) 🆕 | [Tech Report] A Unified Multimodal Model for Scalable 3D Generation… | ⭐ 261 | ≈+17 | — | — | `unified-ug` |
| 21 | [**roboflow/maestro**](https://github.com/roboflow/maestro) | streamline the fine-tuning process for multimodal models: PaliGemma 2… | ⭐ 2,695 | ≈+17 | — | Python | `pretraining` |
| 22 | [**jingyi0000/VLM_survey**](https://github.com/jingyi0000/VLM_survey) | Collection of AWESOME vision-language models for vision tasks | ⭐ 3,133 | ≈+17 | — | — | `pretraining` |
| 23 | [**EvolvingLMMs-Lab/NEO**](https://github.com/EvolvingLMMs-Lab/NEO) | NEO Series: Native Vision-Language Models from First Principles | ⭐ 925 | ≈+16 | — | Python | `pretraining` |
| 24 | [**czvvd/PartLLM**](https://github.com/czvvd/PartLLM) 🆕 | [SIGGRAPH Asia 2026 (TOG)] PartLLM: A Unified Multimodal Foundation for 3D Par… | ⭐ 160 | ≈+16 | — | Python | `unified-ug` |
| 25 | [**deepgenteam/deepgen**](https://github.com/deepgenteam/deepgen) | A Lightweight Unified Multimodal Model for Advancing Image Generation and Edit… | ⭐ 584 | ≈+15 | — | Python | `unified-ug` |
| 26 | [**EvolvingLMMs-Lab/lmms-engine**](https://github.com/EvolvingLMMs-Lab/lmms-engine) | A simple, unified multimodal models training engine… | ⭐ 833 | ≈+12 | — | Python | `unified-ug` |
| 27 | [**emcf/thepipe**](https://github.com/emcf/thepipe) | Get clean data from tricky documents, powered by vision-language models ⚡ | ⭐ 1,528 | ≈+11 | — | Python | `pretraining` |
| 28 | [**OpenBMB/MiniCPM-o-Demo**](https://github.com/OpenBMB/MiniCPM-o-Demo) | Official PyTorch+CUDA Full-functional Web Demo for MiniCPM-o 4.5 | ⭐ 427 | ≈+11 | — | Python | `omni` |
| 29 | [**1038lab/ComfyUI-QwenVL**](https://github.com/1038lab/ComfyUI-QwenVL) | ComfyUI-QwenVL custom node: Integrates the Qwen-VL series… | ⭐ 926 | ≈+11 | — | Python | `pretraining` |
| 30 | [**QwenLM/Qwen3-Omni**](https://github.com/QwenLM/Qwen3-Omni) | Qwen3-omni is a natively end-to-end, omni-modal LLM developed by the Qwen team… | ⭐ 4,105 | +10 | — | Jupyter Notebook | `any-to-any` |
| 31 | [**OpenSQZ/MiniCPM-V-CookBook**](https://github.com/OpenSQZ/MiniCPM-V-CookBook) | Cook up amazing AI applications effortlessly with MiniCPM / MiniCPM-V / MiniCP… | ⭐ 670 | ≈+10 | — | Python | `omni` |
| 32 | [**gokayfem/awesome-vlm-architectures**](https://github.com/gokayfem/awesome-vlm-architectures) | Curated visual catalog of 200+ vision-language model (VLM/MLLM) architectures… | ⭐ 1,366 | ≈+10 | — | Markdown | `pretraining` |
| 33 | [**InternRobotics/InternVLA-A-series**](https://github.com/InternRobotics/InternVLA-A-series) | InternVLA-A1: Unifying Understanding, Generation… | ⭐ 574 | ≈+10 | — | Python | `pretraining` |
| 34 | [**houyuanchen111/UniVidX**](https://github.com/houyuanchen111/UniVidX) | [SIGGRAPH 2026 / TOG] Official code of the paper "UniVidX: A Unified Multimoda… | ⭐ 259 | ≈+9 | — | Python | `unified-ug` |
| 35 | [**KangLiao929/Puffin**](https://github.com/KangLiao929/Puffin) | Puffin Series: Towards Unified Multimodal 3D World Models | ⭐ 517 | ≈+9 | — | Python | `unified-ug` |
| 36 | [**NVIDIA-Omniverse/usd-content-agents**](https://github.com/NVIDIA-Omniverse/usd-content-agents) | AI-powered agents for automating 3D content workflows using Vision-Language Mo… | ⭐ 244 | ≈+9 | — | Python | `pretraining` |
| 37 | [**fyzhang1/FocusGUI**](https://github.com/fyzhang1/FocusGUI) 🆕 | Official code for "Focused Omni-Modal GUI Agents“ | ⭐ 95 | ≈+8 | — | Python | `omni` |
| 38 | [**InternRobotics/InternVLA-M1**](https://github.com/InternRobotics/InternVLA-M1) | InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generali… | ⭐ 438 | ≈+7 | — | Python | `pretraining` |
| 39 | [**zli12321/Vision-Language-Models-Overview**](https://github.com/zli12321/Vision-Language-Models-Overview) | A most Frontend Collection and survey of vision-language model papers… | ⭐ 733 | ≈+7 | — | HTML | `pretraining` |
| 40 | [**vulab-AI/Awesome-Spatial-VLMs**](https://github.com/vulab-AI/Awesome-Spatial-VLMs) | [Awesome-Spatial-VLMs] This repository is the official… | ⭐ 474 | ≈+7 | — | Python | `pretraining` |
| 41 | [**lucasjinreal/Crane**](https://github.com/lucasjinreal/Crane) | A Pure Rust based LLM, VLM, VLA, TTS, OCR Inference Engine… | ⭐ 527 | ≈+6 | — | Rust | `omni` |
| 42 | [**ByteDance-Seed/Bagel**](https://github.com/ByteDance-Seed/Bagel) | Open-source unified multimodal model | ⭐ 6,215 | +6 | — | Python | `unified-ug` |
| 43 | [**VITA-Group/VLM-3R**](https://github.com/VITA-Group/VLM-3R) | [CVPR 2026] VLM-3R: Vision-Language Models Augmented with Instruction-Aligned… | ⭐ 454 | ≈+6 | — | Python | `pretraining` |
| 44 | [**zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP**](https://github.com/zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP) | A curated list of awesome prompt/adapter learning methods for vision-language… | ⭐ 802 | ≈+6 | — | — | `pretraining` |
| 45 | [**hustvl/Senna**](https://github.com/hustvl/Senna) | [IJCV 2026] Senna: Bridging Large Vision-Language Models and End-to-End Autono… | ⭐ 559 | ≈+5 | — | Python | `pretraining` |
| 46 | [**gokayfem/ComfyUI_VLM_nodes**](https://github.com/gokayfem/ComfyUI_VLM_nodes) | ComfyUI nodes for vision-language models: Qwen3-VL, Moondream 3, Florence-2… | ⭐ 593 | ≈+4 | — | Python | `pretraining` |
| 47 | [**IBM/terramind**](https://github.com/IBM/terramind) | TerraMind is the first any-to-any generative foundation model for Earth Observ… | ⭐ 332 | ≈+4 | — | Jupyter Notebook | `any-to-any` |
| 48 | [**HarryHsing/OmniAgent**](https://github.com/HarryHsing/OmniAgent) | OmniAgent (ICML 2026): the first native omni-modal agent for active video perc… | ⭐ 90 | ≈+4 | — | Python | `omni` `pretraining` |
| 49 | [**VectorSpaceLab/OmniGen2**](https://github.com/VectorSpaceLab/OmniGen2) | OmniGen2: Exploration to Advanced Multimodal Generation… | ⭐ 4,122 | +4 | — | Jupyter Notebook | `unified-ug` |
| 50 | [**GingerCohle/VLMCSHFG**](https://github.com/GingerCohle/VLMCSHFG) | This is the official code repo for "Vision-Language Models Empowered Nighttime… | ⭐ 370 | ≈+4 | — | Python | `pretraining` |
| 51 | [**liyanlin06/UniM**](https://github.com/liyanlin06/UniM) | [CVPR 2026] Official repo of "UniM: A Unified Any-to-Any Interleaved Multimoda… | ⭐ 113 | ≈+4 | — | Python | `any-to-any` |
| 52 | [**Fr0zenCrane/UniCoT**](https://github.com/Fr0zenCrane/UniCoT) | [ICLR 2026] Uni-CoT: Towards Unified Chain-of-Thought Reasoning Across Text an… | ⭐ 238 | ≈+4 | — | Python | `any-to-any` |
| 53 | [**jamjamjon/usls**](https://github.com/jamjamjon/usls) | A Rust library integrated with ONNXRuntime… | ⭐ 447 | ≈+3 | — | Rust | `pretraining` |
| 54 | [**JIA-Lab-research/MGM-Omni**](https://github.com/JIA-Lab-research/MGM-Omni) | MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech | ⭐ 202 | ≈+3 | — | Python | `omni` |
| 55 | [**modelscope/mcore-bridge**](https://github.com/modelscope/mcore-bridge) | MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art l… | ⭐ 107 | ≈+3 | — | Python | `omni` |
| 56 | [**mstar-project/mstar**](https://github.com/mstar-project/mstar) | A high-performance, universal serving framework for any-to-any models. | ⭐ 114 | ≈+3 | — | Python | `any-to-any` |
| 57 | [**FoundationVision/VAR**](https://github.com/FoundationVision/VAR) | [NeurIPS 2024 Best Paper Award][GPT beats diffusion🔥] [scaling laws in visual… | ⭐ 8,768 | +3 | — | Jupyter Notebook | `tokenizers` |
| 58 | [**kyegomez/ScreenAI**](https://github.com/kyegomez/ScreenAI) | Implementation of the ScreenAI model from the paper: "A Vision-Language Model… | ⭐ 387 | ≈+3 | — | Python | `pretraining` |
| 59 | [**mala-lab/Awesome-Anomaly-Detection-Foundation-Models**](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) | A curated list of papers & resources on anomaly detection foundation models us… | ⭐ 227 | ≈+3 | — | — | `pretraining` |
| 60 | [**Zihan-Su/UniMRG**](https://github.com/Zihan-Su/UniMRG) | [ICML 2026] The official implementation of paper "Generation Enhances Understa… | ⭐ 102 | ≈+3 | — | Python | `unified-ug` |
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
