# 🧠 Pretraining Foundations · 预训练底座

> 一句话：**统一架构不是从零长出来的。**
> 对比学习、生成式预训练、视觉指令微调，是后面 Chameleon / Janus / BAGEL 的配方来源。这条赛道收「为什么这样训」。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/spark-pretraining-dark.svg">
  <img src="../assets/spark-pretraining-light.svg" alt="Pretraining Foundations 近 12 周论文发布趋势">
</picture>

[← 返回总览](../README.md) · [图像与视频分词器 →](tokenizers.md)

---

## 1. 三层地基

```
对比学习     CLIP / ALIGN / SigLIP     把图和文拉到同一空间
    │
生成式预训练  BLIP-2 / Flamingo / CoCa  让视觉条件能驱动语言模型
    │
指令微调     LLaVA / InternVL / Qwen-VL 把底座变成能对话的助手
    │
    ▼
Native 统一模型开始自己训视觉 token，而不再只接冻结塔
```

LLaVA 一类模块化 MLLM **不是** native，但它们是对照基线和数据配方的来源，所以仍收在这里。判断一条工作算不算 native，看 [总览里的决策流](../README.md#-什么是-native-multimodal)。

## 2. 🏛 奠基与必读

> 由 `scripts/seed_classics.py` 按 arXiv ID 校验后自动填充；ID 失效会自动剔除，不留死链。

<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2021-02-26 | **Learning Transferable Visual Models From Natural Language Supervision** | Alec Radford, Jong Wook Kim et al. | CLIP：对比图文预训练，几乎所有后续 VLM 的视觉塔都从这里长出来 | [📄 2103.00020](https://arxiv.org/abs/2103.00020) |
| 2022-04-29 | **Flamingo: a Visual Language Model for Few-Shot Learning** | Jean-Baptiste Alayrac, Jeff Donahue et al. | Flamingo：把冻结视觉编码器接到 LLM 上的 few-shot 范式 | [📄 2204.14198](https://arxiv.org/abs/2204.14198) |
| 2023-01-30 | **BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models** | Junnan Li, Dongxu Li et al. | BLIP-2：Q-Former 桥接冻结视觉塔与冻结 LLM，生成式预训练的关键一步 | [📄 2301.12597](https://arxiv.org/abs/2301.12597) |
| 2023-04-17 | **Visual Instruction Tuning** | Haotian Liu, Chunyuan Li et al. | LLaVA：视觉指令微调把 VLM 变成能对话的助手 | [📄 2304.08485](https://arxiv.org/abs/2304.08485) |
| 2025-02-19 | **Qwen2.5-VL Technical Report** | Shuai Bai, Keqin Chen et al. | Qwen2.5-VL：动态分辨率 + 时序定位，开源 VL 底座的 2025 标杆 | [📄 2502.13923](https://arxiv.org/abs/2502.13923) |
<!-- table:end classics -->

## 3. 📄 自动跟踪的最新论文

> 每日由 GitHub Actions 从 arXiv 抓取、打分、去重后写入；按提交日期倒序，表内最多保留 200 条，更早的仍留在 `data/papers.json`。

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2026-10-24 | **What Remains OOD? OODConceptBench for Open-World Concept Recognition in Vision-Language Models** | Zhiran Luo, Zhiyong Yang et al. | In the era of large-scale pretrained models, zero-shot generalization has increasingly blurred… | [📄 2610.33564](https://arxiv.org/abs/2610.33564) `cs.CV` |
| 2026-10-23 | **Image Clustering with Vision-Language Model Embeddings** | João P. Matos-Carvalho, Nuno Fachada | Pretrained vision-language models provide image representations whose suitability for clusterin… | [📄 2610.33265](https://arxiv.org/abs/2610.33265) `cs.CV` |
| 2026-10-20 | **When Does Sharing Work? Scaling a Shared SigLIP2 Across Image, Video, Audio, and Audio-Visual Representations** | Xiaofei Sun, Peng Wang et al. | Contrastive pretraining has advanced image-text understanding, yet image, video… | [📄 2611.05406](https://arxiv.org/abs/2611.05406) `cs.CV` |
| 2026-10-20 | **Progressive Subset Selection and Cascaded Consistency for Unsupervised Vision-Language Model Adaptation** | Hao Yan, Guanghui Wang | Pretrained Vision-Language Models (PVLMs) achieve strong zero-shot recognition but often suffer… | [📄 2610.27515](https://arxiv.org/abs/2610.27515) `cs.CV` |
| 2026-10-20 | **Convergent Performance, Divergent Mechanisms in LoRA-Adapted Vision Foundation Models for Brain MRI** | Cecilia Diana-Albelda, Fiona Kekwick et al. | Adapting Vision Foundation Models (VFMs) to medical imaging via LoRA has become standard practi… | [📄 2610.28255](https://arxiv.org/abs/2610.28255) `cs.CV` |
| 2026-10-16 | **Generative Text Modelling and Language-Guided Visual Attention for Deciphering Palimpsests** | Robin Hollifeldt, Tianru Zhang et al. | Recovering obscured text in palimpsests, i.e. the manuscripts where the original writing (under… | [📄 2610.24060](https://arxiv.org/abs/2610.24060) `cs.CV` |
| 2026-10-15 | **Retrofitting Recurrent Vision-Language Models from Pretrained Backbones** | Madhav Iyengar, Andreas Geiger et al. | Recent work shows that depth recurrence can be retrofitted into pretrained language models… | [📄 2610.22075](https://arxiv.org/abs/2610.22075) `cs.CV` |
| 2026-10-15 | **VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models** | Qi Lu, Jiarun Li et al. | Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-languag… | [📄 2610.21306](https://arxiv.org/abs/2610.21306) `cs.CV` |
| 2026-10-14 | **More Than Seeing: Vision as Scalable Anchors in Native Multimodal Pre-Training** | Haoyuan Wu, Aoqi Wu et al. | Native multimodal pre-training trains a single model from scratch on text and multimodal data… | [📄 2610.19443](https://arxiv.org/abs/2610.19443) `cs.CL` |
| 2026-10-13 | **End-to-End Vision-Language-Action Policies for Autonomous Lunar Rover Docking** | Sitan Huang, Grace Gao | Surface navigation on the Moon is subject to extreme illumination contrast and deployment-time… | [📄 2610.19224](https://arxiv.org/abs/2610.19224) `cs.RO` |
| 2026-10-13 | **MARTS: A Modular Agricultural Robot for Targeted Spraying of Diseased Tomato Plants in Greenhouses** | Rajmeet Singh, Manveen Kaur et al. | Broadcast spraying remains the dominant method of disease control in greenhouse tomato producti… | [📄 2610.18123](https://arxiv.org/abs/2610.18123) `cs.RO` |
| 2026-10-09 | **A4-MR: Abnormality Aware Anatomical Alignment for MR** | Noel D'souza, Zhijian Yang et al. | Recent advances in large-scale foundation models have enabled strong generalization across a wi… | [📄 2610.13056](https://arxiv.org/abs/2610.13056) `cs.CV` |
| 2026-10-06 | **Image Bitstream Fine-grained Understanding for Privacy-Friendly AIoT** | Zhen Yu, Wenyang Liu et al. | Image Bitstream Fine-grained Understanding (IBFU) aims to directly perform fine-grained classif… | [📄 2610.08414](https://arxiv.org/abs/2610.08414) `cs.CV` |
| 2026-09-29 | **PixelUMM: Encoder-Free Unified Image and Video Understanding and Generation** | Cong Wei, Xuanchi Ren et al. | Unified Multimodal Models (UMMs) often rely on separate visual representations for understandin… | [📄 2609.38597](https://arxiv.org/abs/2609.38597) `cs.CV` |
| 2026-09-28 | **AdaKerNet: Neural Kernel Decoding for Task-Adaptive Prediction with Multimodal Large Models** | Konstantinos D. Polyzos, Eleni Oikonomou et al. | Large foundation models have been introduced with the promise of efficient adaptation to downst… | [📄 2609.36368](https://arxiv.org/abs/2609.36368) `cs.LG` |
| 2026-09-27 | **Informative Viewpoint Selection for Episodic-Memory Embodied Question Answering using Omnidirectional Images** | Kaname Kitamura, Asako Kanezaki | Embodied Question Answering (EQA) requires agents to answer natural language questions about su… | [📄 2609.33288](https://arxiv.org/abs/2609.33288) `cs.CV` |
| 2026-11-05 | **Describe Your Facial Expressions by Linking Image Encoders and Large Language Models** | Yujian Yuan, Jiabei Zeng et al. | A novel task of describing human facial expressions of a facial image in natural language… | [📄 2611.08138](https://arxiv.org/abs/2611.08138) `cs.CV` |
| 2026-11-04 | **Grounding in the Dark: Text-Only Training for Zero-Shot Video Temporal Localization** | Divyanshu Mishra, Sabine Sternig et al. | Video-LLMs are typically trained on paired video-text data for temporal tasks… | [📄 2611.06149](https://arxiv.org/abs/2611.06149) `cs.CV` |
| 2026-11-02 | **Findings-aware Language-Image Pretraining for CT Volume Interpretation** | Takuro Shimaya, Junya Inoh et al. | Computed tomography (CT) provides diverse patient information and various clinical tasks… | [📄 2611.02327](https://arxiv.org/abs/2611.02327) `cs.CV` |
| 2026-11-02 | **PixelBench: Can LLMs Understand and Generate Images Pixel by Pixel?** | Haoquan Zhang, Feiyang Liu et al. | Large language models (LLMs) can generate visual assets through text-based formats such as SVG… | [📄 2611.02540](https://arxiv.org/abs/2611.02540) `cs.CV` |
| 2026-11-02 | **Align Once to Explain: Feature Alignment for Scalable B-cosification of Foundational Vision Transformers** | Raphael Maser, Siddhartha Gairola et al. | Foundational vision models have become the de facto standard for many vision tasks due to their… | [📄 2611.03438](https://arxiv.org/abs/2611.03438) `cs.CV` |
| 2025-05-01 | **Seed1.5-VL** | — | Seed1.5 Vision-Language foundation model | [📄 2505.07062](https://arxiv.org/abs/2505.07062) `catalog` |
| 2025-05-01 | **MiMo-VL** | — | MiMo Vision-Language model | [📄 2505.18411](https://arxiv.org/abs/2505.18411) `catalog` |
| 2025-04-01 | **InternVL3** | — | InternVL3 with enhanced capabilities (VL backbone) | [📄 2504.10479](https://arxiv.org/abs/2504.10479) `catalog` |
| 2025-02-01 | **SigLIP 2** | — | Improved SigLIP with multi-resolution | [📄 2502.14786](https://arxiv.org/abs/2502.14786) `catalog` |
| 2025-02-01 | **Qwen2.5-VL** | — | Qwen2.5 Vision-Language model | [📄 2502.13923](https://arxiv.org/abs/2502.13923) `catalog` |
| 2024-02-01 | **EVA-CLIP** | — | Improved EVA-based CLIP (18B params) | [📄 2402.04252](https://arxiv.org/abs/2402.04252) `catalog` |
| 2024-02-01 | **InternVL** | — | Scaling vision foundation model | [📄 2312.14238](https://arxiv.org/abs/2312.14238) `catalog` |
| 2023-04-01 | **LLaVA** | — | Large Language and Vision Assistant | [📄 2304.08485](https://arxiv.org/abs/2304.08485) `catalog` |
| 2023-03-01 | **SigLIP** | — | Sigmoid loss for language-image pretraining | [📄 2303.15343](https://arxiv.org/abs/2303.15343) `catalog` |
| 2023-01-01 | **BLIP-2** | — | Bootstrapping vision-language pretraining | [📄 2301.12597](https://arxiv.org/abs/2301.12597) `catalog` |
| 2022-08-01 | **BEiT-3** | — | Multimodal foundation model via masked data modeling | [📄 2208.10442](https://arxiv.org/abs/2208.10442) `catalog` |
| 2022-05-01 | **CoCa** | — | Contrastive captioners | [📄 2205.01068](https://arxiv.org/abs/2205.01068) `catalog` |
| 2022-05-01 | **i-Code** | — | Integrative and composable multimodal learning framework for text, speech, and image | [📄 2205.01818](https://arxiv.org/abs/2205.01818) `catalog` |
| 2022-04-01 | **Flamingo** | — | Few-shot visual language model (DeepMind) | [📄 2204.14198](https://arxiv.org/abs/2204.14198) `catalog` |
| 2022-02-01 | **OFA** | — | Unified sequence-to-sequence pretraining | [📄 2202.03052](https://arxiv.org/abs/2202.03052) `catalog` |
| 2021-02-01 | **ALIGN** | — | Large-scale alignment using noisy data (Google) | [📄 2102.05918](https://arxiv.org/abs/2102.05918) `catalog` |
| 2021-01-01 | **CLIP** | — | Contrastive Language-Image Pretraining (OpenAI) | [📄 2103.00020](https://arxiv.org/abs/2103.00020) `catalog` |
<!-- table:end papers -->
