# 🖼️ Unified Understanding + Generation · 统一理解与生成

> 一句话：**同一个模型既要看懂，也要画出来。**
> 这是 native multimodal 最硬的定义：共享计算路径、统一 token、端到端跨模态训练。不是在冻结 LLM 上加 adapter。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/spark-unified-ug-dark.svg">
  <img src="../assets/spark-unified-ug-light.svg" alt="Unified Understanding + Generation 近 12 周论文发布趋势">
</picture>

[← 返回总览](../README.md) · [任意到任意 →](any-to-any.md)

---

## 1. 这条赛道在争什么

理解要语义，生成要像素。把它们塞进同一个 Transformer 之后，编码器会打架。2024–2025 的主线就是在处理这个冲突：

```
像素级离散 AR     Chameleon / Emu3 / Liquid
        │
        ▼
解耦双编码器     Janus / Janus-Pro / OmniGen2
        │
        ▼
AR + Diffusion   Transfusion / Show-o / BAGEL / Show-o2
```

## 2. 读论文时对着这张表看

| 矛盾 | 表现 | 常见解法 |
| :-- | :-- | :-- |
| 语义 ↔ 像素 | 一个 encoder 两头不讨好 | 理解/生成解耦，骨干共享 |
| 离散 ↔ 连续 | 文本要 AR，图像要扩散 | 混合头、分模态损失 |
| 重建 ↔ 生成 | tokenizer 重建好未必生成好 | tokenizer-model 联合训 |
| 开源 ↔ 配方 | 很多 SOTA 不放数据配比 | 看消融，不只看分数 |

## 3. 🏛 奠基与必读

> 由 `scripts/seed_classics.py` 按 arXiv ID 校验后自动填充；ID 失效会自动剔除，不留死链。

<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2024-05-16 | **Chameleon: Mixed-Modal Early-Fusion Foundation Models** | Chameleon Team | Early-fusion 离散 AR 的里程碑：图文进同一个 next-token 空间 | [📄 2405.09818](https://arxiv.org/abs/2405.09818) |
| 2024-08-20 | **Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model** | Chunting Zhou, Lili Yu et al. | 同一模型里 next-token + diffuse，AR+Diffusion 混合的代表 | [📄 2408.11039](https://arxiv.org/abs/2408.11039) |
| 2024-08-22 | **Show-o: One Single Transformer to Unify Multimodal Understanding and Generation** | Jinheng Xie, Weijia Mao et al. | 一个 Transformer 统一理解与生成，离散+连续两条通路 | [📄 2408.12528](https://arxiv.org/abs/2408.12528) |
| 2024-09-27 | **Emu3: Next-Token Prediction is All You Need** | Xinlong Wang, Xiaosong Zhang et al. | Next-token prediction is all you need：纯 AR 覆盖图/文/视频 | [📄 2409.18869](https://arxiv.org/abs/2409.18869) |
| 2025-01-29 | **Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling** | Xiaokang Chen, Zhiyu Wu et al. | 解耦视觉编码：理解与生成不再抢同一个 encoder | [📄 2501.17811](https://arxiv.org/abs/2501.17811) |
| 2025-05-20 | **Emerging Properties in Unified Multimodal Pretraining** | Chaorui Deng, Deyao Zhu et al. | 大规模统一预训练出现涌现能力，2025 统一模型的标杆 | [📄 2505.14683](https://arxiv.org/abs/2505.14683) |
<!-- table:end classics -->

## 4. 📄 自动跟踪的最新论文

> 每日由 GitHub Actions 从 arXiv 抓取、打分、去重后写入；按提交日期倒序，表内最多保留 200 条，更早的仍留在 `data/papers.json`。

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2026-11-06 | **UniMore: Fine-Grained Supervision for Unified Understanding and Generation** | Haoyue Bai, Yinyi Luo et al. | Unified multimodal models combine image understanding and generation within one system… | [📄 2611.08996](https://arxiv.org/abs/2611.08996) `cs.MM` |
| 2026-11-06 | **Grounding-Aware Judge Reward Reinforcement Learning for Out-of-Domain Face Anti-Spoofing** | Xiaoyong Yu, Xinge Yu | Face Anti-Spoofing (FAS) must distinguish genuine faces from presentation attacks… | [📄 2611.09047](https://arxiv.org/abs/2611.09047) `cs.CV` |
| 2026-10-29 | **DiFuse: Fusing Native Diffusion Representations for Spatial Reasoning in Unified Multimodal Models** | Ruixin Fan, Weining Wang et al. | Unified multimodal models (UMMs) jointly support visual understanding and image generation… | [📄 2610.39609](https://arxiv.org/abs/2610.39609) `cs.CV` |
| 2026-10-29 | **SelfThinker: Self-Evolving Reasoning via Reliability-Verified Intrinsic Visual Thoughts** | Zhangquan Chen, Ruqi Huang | Unified multimodal models can both generate and understand images within a single set of weight… | [📄 2610.40115](https://arxiv.org/abs/2610.40115) `cs.CV` |
| 2026-10-29 | **Calibrating Attention-Based Token Pruning for Efficient Multi-Image Synthesis in UMMs** | Zimeng Wu, Qijian Tian et al. | Unified Multimodal Models (UMMs) enable powerful multi-image synthesis but incur substantial co… | [📄 2610.39467](https://arxiv.org/abs/2610.39467) `cs.CV` |
| 2026-10-29 | **RepConTUR: A Report-Conditioned Volumetric Multimodal Model for Abdominal Tumor Segmentation** | Seunghwan Lee, Sangjoon Park et al. | Tumor delineation is required for radiotherapy planning… | [📄 2610.40094](https://arxiv.org/abs/2610.40094) `cs.CV` |
| 2026-10-28 | **Continual Adaptation Across Modalities: Learning and Forgetting in Unified Multimodal Models** | Xinrui Wang, Zhihao Chen et al. | Unified multimodal models (UMMs), which can process and generate diverse modalities within a si… | [📄 2610.38436](https://arxiv.org/abs/2610.38436) `cs.LG` |
| 2026-10-28 | **IntReal: A Real-World Dataset and Benchmark for Multimodal Interleaved Generation** | Shaohan Yu, Jie Qin et al. | Humans routinely consume multimodal content, where textual and visual information is naturally… | [📄 2610.38425](https://arxiv.org/abs/2610.38425) [💻](https://github.com/yushaohan/IntReal) 🤗 |
| 2026-10-27 | **EmbeddingGemma 2: Unified and Efficient Multimodal Representations** | Henrique Schechter Vera, Sahil Dua et al. | EmbeddingGemma 2, an open multimodal embedding model which natively represents text, images… | [📄 2610.37364](https://arxiv.org/abs/2610.37364) 🤗 |
| 2026-10-26 | **Cross-modal Steering Vectors Exist Across Both Image and Text Generation** | Donghao Zeng, Nishant Subramani et al. | Are concepts and mechanisms unified across modalities in current AI models… | [📄 2610.36269](https://arxiv.org/abs/2610.36269) [💻](https://github.com/saintsauceee/cross-modal-steering) 🤗 |
| 2026-10-25 | **Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion** | Kam Man Wu, Yu Zhang et al. | Spatial audio authoring coordinates source decisions with soundfield synthesis… | [📄 2610.34415](https://arxiv.org/abs/2610.34415) `cs.SD` [💻](https://github.com/WJM-George/AMBIT) |
| 2026-10-23 | **RynnUnify: Towards Unified Embodied Brain** | Minghao Zhu, Bohan Hou et al. | RynnUnify, a 16B unified embodied model that combines strong embodied understanding with long-h… | [📄 2610.32965](https://arxiv.org/abs/2610.32965) [💻](https://github.com/alibaba-damo-academy/RynnUnify) 🤗 |
| 2026-10-20 | **MindView: Benchmarking Generative Multi-View Spatial Intelligence** | Yanbo Wang, Siqi Luo et al. | Spatial intelligence has recently been assessed through generative tasks such as spatially grou… | [📄 2610.28622](https://arxiv.org/abs/2610.28622) `cs.CV` |
| 2026-10-19 | **Oddin: Latent Visual Reasoning in Unified Multimodal Models via Self-Distillation from Image Generation** | Jaeyong Ko, Hankyeol Kim et al. | Unified large multimodal models (ULMMs) are able to perform visual reasoning through interleave… | [📄 2610.33062](https://arxiv.org/abs/2610.33062) `cs.CV` |
| 2026-10-19 | **Text-to-Image Generative Modeling Without Language Pretraining** | Keshigeyan Chandrasegaran, Yue Zhao et al. | Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned… | [📄 2610.26863](https://arxiv.org/abs/2610.26863) `cs.LG` |
| 2026-10-19 | **Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience** | Tianqi Liu, Hanfei Zhao et al. | World models enable embodied agents to anticipate action consequences… | [📄 2610.26855](https://arxiv.org/abs/2610.26855) `cs.CV` |
| 2026-10-15 | **FlexUMM: Flexible Representation Learning for Unified Multimodal Models** | Yinyi Luo, Haoyue Bai et al. | Unified multimodal models (UMMs) can integrate understanding and generation within a single bac… | [📄 2610.22682](https://arxiv.org/abs/2610.22682) `cs.AI` |
| 2026-10-15 | **Vision-Guided Closed-Loop Autonomous Navigation of Light-Driven Janus Microbots** | Kanhu Charan Andia, Harsh Prashant Katole et al. | Artificial microbots capable of precise and autonomous navigation could provide versatile platf… | [📄 2610.21222](https://arxiv.org/abs/2610.21222) `cs.RO` |
| 2026-10-14 | **ReasonUni: Reasoning-Augmented Reconstruction Advances Unified Multimodal Models** | Feize Wu, Zhiyuan Yan et al. | Image-to-text (I2T) understanding and text-to-image (T2I) generation are dual tasks in unified… | [📄 2610.20781](https://arxiv.org/abs/2610.20781) `cs.CV` |
| 2026-10-14 | **What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal Models** | Tengju Ru, Weitong Lian et al. | Fine-grained visual understanding requires distinguishing subtle differences in local attribute… | [📄 2610.23987](https://arxiv.org/abs/2610.23987) `cs.CV` |
| 2026-10-14 | **Can Learning to Answer Spatial Questions Improve Novel-View Generation?** | Jahyeok Koo, Hyeonseo Yu et al. | Generating novel views from limited observations requires preserving both the appearance and sp… | [📄 2610.20610](https://arxiv.org/abs/2610.20610) `cs.CV` |
| 2026-10-13 | **RSIgen: Reciprocal Self-Improvement for Agentic Visual Generation** | Yidi Liu, Haozhe Wang et al. | Agentic visual generation produces experience that can improve the native understanding (agent)… | [📄 2610.18688](https://arxiv.org/abs/2610.18688) `cs.CV` |
| 2026-10-12 | **Scaling Unified Multimodal Models to Long-Horizon Interleaved Generation** | Ziqiao Peng, Yutao Cui et al. | Unified multimodal models (UMMs) provide an interface for interleaved text-image generation… | [📄 2610.17080](https://arxiv.org/abs/2610.17080) `cs.CV` |
| 2026-10-12 | **Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems** | Xin Xu, Ke Cheng et al. | Improving an agent through successive revisions requires balancing exploration and evaluation u… | [📄 2610.16491](https://arxiv.org/abs/2610.16491) `cs.LG` |
| 2026-10-11 | **SIMIT: Self-Improving Vision-Language Models via Imagination at Test-Time** | Mehmet Onurcan Kaya, Desmond Elliott et al. | SIMIT, a test-time self-improvement framework in which a vision-language model creates its own… | [📄 2611.00053](https://arxiv.org/abs/2611.00053) `cs.CV` [💻](https://github.com/monurcan/simit_paper) |
| 2026-10-10 | **Optoelectronically Enabled Simultaneous and Decoupled Navigation and Selective Pairing of Electrically Driven Janus Particles for Multi-Agent Microrobotics** | Srikanta Debata, Ido Rachbuch et al. | Self-propelled Janus particles are promising active agents for microscale manipulation and micr… | [📄 2610.14560](https://arxiv.org/abs/2610.14560) `cond-mat.soft` |
| 2026-10-10 | **Getting Space Right: Agentic Rewards for Image Generation** | Xiaofeng Tan, Jiaxin Lin et al. | Reinforcement learning (RL) is promising for spatial text-to-image generation… | [📄 2610.14852](https://arxiv.org/abs/2610.14852) `cs.CV` |
| 2026-10-10 | **Understanding Unified VLMs: From Attention Probing to Guidance Tuning for Multimodal Generation** | Zhengyang Luo, Xiaoyu Qiu et al. | Unified vision-language models (VLMs) perform both text-to-image (T2I) and image-to-text (I2T)… | [📄 2610.15227](https://arxiv.org/abs/2610.15227) `cs.AI` |
| 2026-10-08 | **Syn-Omni: Structured Specialization and Progressive Collaboration for Omnimodal Embeddings** | Youngtaek Oh, Qiyu Wu et al. | Omnimodal embeddings naturally involve both shared representations and modality-specific featur… | [📄 2610.12256](https://arxiv.org/abs/2610.12256) `cs.CV` |
| 2026-10-07 | **Omni-Diffusion-Distill: Few-Step Distillation of Unified Multimodal Diffusion Large Language Models** | Hong Huang, Chenhongyi Yang et al. | Unified multimodal diffusion large language models (dLLMs) offer a single architecture for both… | [📄 2610.10990](https://arxiv.org/abs/2610.10990) `cs.CV` |
| 2026-10-07 | **From Pixel to Coding: Evaluating the Figure Reproduction Capabilities of MLLMs** | Zijian Chen, Zhengyu Chen et al. | Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in both visu… | [📄 2610.10066](https://arxiv.org/abs/2610.10066) `cs.CV` |
| 2026-10-06 | **Visual Abstention in Unified Multimodal Models** | Chufan Shi, Cheng Yang et al. | Unified multimodal models (UMMs) integrate understanding and generation… | [📄 2610.07887](https://arxiv.org/abs/2610.07887) `cs.CL` |
| 2026-10-05 | **Cross-Modal Forgetting and Transfer in Unified Multimodal Post-Training** | Francesco Colasurdo, Ivan Slobozhan et al. | Unified multimodal models answer questions about images and also generate images with one share… | [📄 2610.23918](https://arxiv.org/abs/2610.23918) `cs.CV` |
| 2026-10-04 | **The Poisoned Conversation: Privacy-Leaking Watermarks in Unified Multimodal Models** | Tobias Braun, Jonas Henry Grebe et al. | Multimodal models are increasingly shifting toward unified architectures that understand and ge… | [📄 2610.05453](https://arxiv.org/abs/2610.05453) `cs.CR` |
| 2026-10-02 | **Recursive Self-Improvement in Unified Multimodal Models** | Huijuan Wang, Chufan Shi et al. | Unified multimodal models (UMMs) understand and generate both text and images… | [📄 2610.03002](https://arxiv.org/abs/2610.03002) `cs.CL` |
| 2026-10-01 | **Octrees as an Explicit 3D Language** | Ran Dan, Si-Tong Wei et al. | Existing 3D large language models (LLMs) compromise on two fronts: they compress shapes into la… | [📄 2610.02388](https://arxiv.org/abs/2610.02388) `cs.CV` |
| 2026-09-30 | **Beyond Structural Unification: A Perspective and Roadmap on Unified Multimodal Models** | Yinyi Luo, Hayes Bai et al. | Unified Multimodal Models (UMMs) emerge as a promising way to combine understanding and generat… | [📄 2610.35906](https://arxiv.org/abs/2610.35906) `cs.MM` |
| 2026-09-30 | **Gestalt: Large Multimodal Interplay Model** | Zequn Yang, Yu Miao et al. | We propose Gestalt, a new paradigm of large multimodal model built around multimodal interplay… | [📄 2610.00576](https://arxiv.org/abs/2610.00576) `cs.CV` |
| 2026-09-29 | **Beyond Layers: Position-Resolved Gradient Conflict and Position-Aware Modulation for Unified Multimodal Models** | Shuyang Jiang, Fucheng Deng et al. | Unified multimodal models (UMMs) train image understanding and autoregressive image generation… | [📄 2609.38485](https://arxiv.org/abs/2609.38485) `cs.CV` |
| 2026-09-29 | **Does Gradient Conflict Predict the Understanding--Generation Trade-off? A Controlled Audit of Conflict-Metric Validity in Unified Multimodal Models** | Shuyang Jiang, Fucheng Deng et al. | Unified multimodal models (UMMs) are increasingly designed around gradient conflict between und… | [📄 2609.38465](https://arxiv.org/abs/2609.38465) `cs.LG` |
| 2026-09-28 | **Mutually Adversarial Self-Training with Evolving Data for Unified Multimodal Models** | Wentao Zhou, Weijie Gan et al. | Unified multimodal models (UMMs) combine image generation and visual understanding in a shared… | [📄 2609.36224](https://arxiv.org/abs/2609.36224) `cs.CV` |
| 2026-09-28 | **Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning** | Yijia Fan, Ziqi Huang et al. | Unified multimodal models can both look at and render images… | [📄 2609.35767](https://arxiv.org/abs/2609.35767) `cs.CV` |
| 2026-09-26 | **UniCache: Task- and Type-Aware KV Cache Compression for Unified Multimodal Models** | Wanqi Yang, Yuexiao Ma et al. | Unified multimodal models combine understanding, generation… | [📄 2609.32831](https://arxiv.org/abs/2609.32831) `cs.LG` |
| 2026-11-05 | **Multimodal Hierarchical Mixture-of-Experts for 3D Medical Vision-Language Modeling** | Gizem Mert, Szymon Płotka et al. | Medical 3D scans and reports are inherently hierarchical… | [📄 2611.08185](https://arxiv.org/abs/2611.08185) `cs.CV` |
| 2026-11-04 | **Prism: Bidirectional Self-Teaching for Unified Multimodal Models** | Peng Zhang, Qian Chen et al. | Unified Multimodal Models (UMMs) aim to support visual understanding and generation within a si… | [📄 2611.06343](https://arxiv.org/abs/2611.06343) `cs.CV` |
| 2026-11-03 | **Is Forgetting Unified? Exploring Concept Unlearning in Unified Multimodal Models** | Zhongkai Xue, Junkai Chen et al. | Unified multimodal models (UMMs) integrate image generation and visual understanding… | [📄 2611.04467](https://arxiv.org/abs/2611.04467) `cs.CV` |
| 2026-11-03 | **From Tokens to Trajectories: Parameter-Efficient Continuous Adaptation of Unified Multimodal Models** | Gayatri Deshmukh, Onkar Susladkar et al. | While discrete tokenization in Unified Multimodal Models (UMMs) establishes strong semantic rea… | [📄 2611.05451](https://arxiv.org/abs/2611.05451) `cs.CV` |
| 2026-11-03 | **YANAMI: A Large-Scale Multimodal Dataset and Benchmark for Multiturn Stateful Interaction** | Shengyu Wang, Tengyue Nong et al. | Unified Multimodal Models (UMMs) integrate visual understanding, generation… | [📄 2611.05280](https://arxiv.org/abs/2611.05280) `cs.CV` |
| 2026-11-02 | **HistoTx: Early fusion of H&E images and spatial transcriptomics at varying spatial transcriptomics resolution with self-supervised learning** | Alice Driessen, Emil Malmsten et al. | Spatial transcriptomics maps gene expression across tissue sections and… | [📄 2611.02681](https://arxiv.org/abs/2611.02681) `cs.LG` |
| 2026-11-02 | **Do Visual RL Gains Scale at Test Time? A Quantile View of Post-Training** | Austin Wang, Lexing Ying | Reinforcement learning (RL) post-training improves the single-sample quality of visual generati… | [📄 2611.02366](https://arxiv.org/abs/2611.02366) `cs.LG` |
| 2026-10-30 | **Latent Reasoning in Continuous Space for Unified Multimodal Models** | Byungwoo Jeon, Yoonwoo Jeong et al. | Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding… | [📄 2610.42149](https://arxiv.org/abs/2610.42149) `cs.CV` |
| 2025-06-01 | **BLIP3-o** | — | BLIP3 for omni generation | [📄 2506.12831](https://arxiv.org/abs/2506.12831) `catalog` |
| 2025-06-01 | **Show-o2** | — | Improved Show-o with enhanced generation | [📄 2506.15564](https://arxiv.org/abs/2506.15564) `catalog` |
| 2025-06-01 | **OmniGen2** | — | Unified image generation (OmniGen2) | [📄 2506.18871](https://arxiv.org/abs/2506.18871) `catalog` |
| 2025-05-01 | **BAGEL** | — | Bootstrapped reasoning with AR+Diffusion (ByteDance) | [📄 2505.14683](https://arxiv.org/abs/2505.14683) [💻](https://github.com/ByteDance-Seed/Bagel) `catalog` |
| 2025-05-01 | **TokLIP** | — | Tokenized CLIP features for generation | [📄 2505.05422](https://arxiv.org/abs/2505.05422) `catalog` |
| 2025-05-01 | **MMaDA** | — | Multimodal masked diffusion model | [📄 2505.15809](https://arxiv.org/abs/2505.15809) [💻](https://github.com/Gen-Verse/MMaDA) `catalog` |
| 2025-05-01 | **Selftok** | — | Self-supervised tokenization for generation | [📄 2505.19065](https://arxiv.org/abs/2505.19065) `catalog` |
| 2025-05-01 | **Muddit** | — | Multimodal unified discrete diffusion transformer | [📄 2505.16965](https://arxiv.org/abs/2505.16965) `catalog` |
| 2025-05-01 | **FUDOKI** | — | Discrete flow-based unified understanding and generation via discrete denoising | [📄 2505.05667](https://arxiv.org/abs/2505.05667) `catalog` |
| 2025-04-01 | **MetaQuery-XL** | — | Meta-query based unified model | [📄 2504.13979](https://arxiv.org/abs/2504.13979) `catalog` |
| 2025-03-01 | **Harmon** | — | Harmonizing visual generation and perception | [📄 2503.07897](https://arxiv.org/abs/2503.07897) `catalog` |
| 2025-03-01 | **VARGPT-v1.1** | — | Visual autoregressive GPT | [📄 2503.16278](https://arxiv.org/abs/2503.16278) `catalog` |
| 2025-03-01 | **UniDisc** | — | Unified discrete diffusion | [📄 2503.20853](https://arxiv.org/abs/2503.20853) `catalog` |
| 2025-03-01 | **HermesFlow** | — | Hermes flow-based unified generation | [📄 2503.12580](https://arxiv.org/abs/2503.12580) `catalog` |
| 2025-01-01 | **Janus-Pro** | — | Unified multimodal understanding and generation (DeepSeek) | [📄 2501.17811](https://arxiv.org/abs/2501.17811) `catalog` |
| 2025-01-01 | **MUSE-VL** | — | Multimodal understanding & synthesis | [📄 2501.06599](https://arxiv.org/abs/2501.06599) `catalog` |
| 2024-12-01 | **Liquid** | — | Language models are scalable multi-modal generators | [📄 2412.04332](https://arxiv.org/abs/2412.04332) `catalog` |
| 2024-12-01 | **LlamaFusion** | — | Llama for text and image fusion | [📄 2412.15188](https://arxiv.org/abs/2412.15188) `catalog` |
| 2024-12-01 | **SynerGen-VL** | — | Synergistic image understanding and generation with vision experts and token folding | [📄 2412.09604](https://arxiv.org/abs/2412.09604) `catalog` |
| 2024-10-01 | **Janus** | — | Decoupling visual encoding for unified multimodal understanding and generation | [📄 2410.13848](https://arxiv.org/abs/2410.13848) `catalog` |
| 2024-09-01 | **Emu3** | — | Next-token prediction for vision, language, and action | [📄 2409.18869](https://arxiv.org/abs/2409.18869) [💻](https://github.com/baaivision/Emu3) `catalog` |
| 2024-08-01 | **Transfusion** | — | Predict next token and diffuse | [📄 2408.11039](https://arxiv.org/abs/2408.11039) `catalog` |
| 2024-08-01 | **Show-o** | — | One single model for multimodal understanding and generation | [📄 2408.12528](https://arxiv.org/abs/2408.12528) [💻](https://github.com/showlab/Show-o) `catalog` |
| 2024-07-01 | **ANOLE** | — | Autoregressive native omni language model | [📄 2407.06135](https://arxiv.org/abs/2407.06135) `catalog` |
| 2024-05-01 | **Chameleon** | — | Early-fusion token-based mixed-modal model (Meta) | [📄 2405.09818](https://arxiv.org/abs/2405.09818) [💻](https://github.com/facebookresearch/chameleon) `catalog` |
| 2024-02-01 | **LWM** | — | Large world model | [📄 2402.08268](https://arxiv.org/abs/2402.08268) [💻](https://github.com/LargeWorldModel/LWM) `catalog` |
| 2023-10-01 | **SEED** | — | Multimodal seed tokenization | [📄 2310.01218](https://arxiv.org/abs/2310.01218) [💻](https://github.com/AILab-CVC/SEED) `catalog` |
| 2023-09-01 | **LaVIT** | — | Language-vision tokenizer | [📄 2309.04596](https://arxiv.org/abs/2309.04596) `catalog` |
| 2023-09-01 | **DreamLLM** | — | Synergistic multimodal comprehension and creation via interleaved text-image generation | [📄 2309.11499](https://arxiv.org/abs/2309.11499) `catalog` |
| 2023-07-01 | **Emu** | — | Emu: Generalist multimodal model | [📄 2307.05222](https://arxiv.org/abs/2307.05222) `catalog` |
<!-- table:end papers -->
