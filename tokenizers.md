# 🔢 Image & Video Tokenizers · 图像与视频分词器

> 一句话：**先把像素变成能进 Transformer 的词。**
> 离散码本、连续隐空间、文本对齐，三条路线都在回答同一件事：视觉证据用多少 token、丢多少细节、能不能和文字待在同一个词表里。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/spark-tokenizers-dark.svg">
  <img src="../assets/spark-tokenizers-light.svg" alt="Image & Video Tokenizers 近 12 周论文发布趋势">
</picture>

[← 返回总览](../README.md) · [统一理解与生成 →](unified-ug.md)

---

## 1. 为什么分词器是 native 的第一块地基

Native multimodal 的定义里有一条是 **unified tokenization**。如果图像还是「冻结 ViT + 投影层」，模型就还在 modular MLLM 那边。分词器决定了：

| 设计选择 | 它卡住的下游能力 |
| :-- | :-- |
| 离散 VQ / LFQ / BSQ | 能不能用纯 next-token 生成图像 |
| 连续 VAE | 能不能把扩散头接到同一条骨干上 |
| 1D / token folding | 上下文窗口够不够喂长视频 |
| 文本对齐 tokenizer | 视觉 token 和词表能不能真的混排 |

## 2. 方法谱系

| 谱系 | 核心机制 | 代表 | 主要代价 |
| :-- | :-- | :-- | :-- |
| **Discrete VQ** | 最近邻查码本 | VQ-VAE, VQGAN, TiTok | 码本崩溃、利用率低 |
| **Residual / FSQ / LFQ / BSQ** | 少查表、多约束 | VAR, FSQ, MAGVIT-v2, QLIP | 实现细节敏感，开源复现成本高 |
| **Continuous VAE** | 连续隐变量 | VA-VAE, EQ-VAE, MAETok | 和离散 AR 对接要额外对齐 |
| **Text-Aligned** | 视觉码本贴到词表 | LQAE, SPAE, DualToken | 重建质量和语义对齐互相抢 |

## 3. 🏛 奠基与必读

> 由 `scripts/seed_classics.py` 按 arXiv ID 校验后自动填充；ID 失效会自动剔除，不留死链。

<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2017-11-02 | **Neural Discrete Representation Learning** | Aaron van den Oord, Oriol Vinyals et al. | VQ-VAE：离散视觉表征的起点，几乎所有 VQ tokenizer 都从这里分叉 | [📄 1711.00937](https://arxiv.org/abs/1711.00937) |
| 2020-12-17 | **Taming Transformers for High-Resolution Image Synthesis** | Patrick Esser, Robin Rombach et al. | VQGAN：把感知损失接到 VQ 上，AR 图像生成真正能看 | [📄 2012.09841](https://arxiv.org/abs/2012.09841) |
| 2022-12-10 | **MAGVIT: Masked Generative Video Transformer** | Lijun Yu, Yong Cheng et al. | MAGVIT：把 tokenizer 从图像推进到视频 | [📄 2212.05199](https://arxiv.org/abs/2212.05199) |
| 2024-04-03 | **Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction** | Keyu Tian, Yi Jiang et al. | VAR：next-scale prediction，把空间层级写进 AR 建模 | [📄 2404.02905](https://arxiv.org/abs/2404.02905) |
| 2024-06-11 | **An Image is Worth 32 Tokens for Reconstruction and Generation** | Qihang Yu, Mark Weber et al. | TiTok：1D tokenizer，把二维码本压到几十个 token | [📄 2406.07550](https://arxiv.org/abs/2406.07550) |
<!-- table:end classics -->

## 4. 📄 自动跟踪的最新论文

> 每日由 GitHub Actions 从 arXiv 抓取、打分、去重后写入；按提交日期倒序，表内最多保留 200 条，更早的仍留在 `data/papers.json`。

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2026-10-27 | **Whole-Body Humanoid Control via Stochastic Motion Tokenization** | Michael Drolet, Oleg Arenz et al. | While velocity-commanded RL policies are effective for controlling quadrupeds… | [📄 2610.36452](https://arxiv.org/abs/2610.36452) `cs.RO` |
| 2026-10-26 | **MedVTok: A General-Purpose Medical Visual Tokenizer** | Chenglong Ma, Yuanfeng Ji et al. | Multimodal medical AI requires a common visual interface for encoding heterogeneous imaging evi… | [📄 2610.35842](https://arxiv.org/abs/2610.35842) `eess.IV` |
| 2026-10-24 | **Patch-Derived or Register Tokens? Comparing Variable-Length Image Tokenizers** | Philipp Schenkel, Tobias Schürmann et al. | Image tokenizers convert pixels into compact latent sequences for efficient generative modeling… | [📄 2610.33540](https://arxiv.org/abs/2610.33540) `cs.CV` |
| 2026-10-21 | **Expandable Modality Experts for Medical Vision-Language Learning** | DM BAPPY, Eunsu Kim et al. | Learning across medical imaging modalities requires making use of images without paired text an… | [📄 2610.29881](https://arxiv.org/abs/2610.29881) `cs.CV` |
| 2026-10-19 | **RoAR-VAE: Improving Latent Diffusability through Robust Prediction** | Yang Yue, Fangyun Wei et al. | An effective visual tokenizer must preserve image fidelity while producing latents that downstr… | [📄 2610.26216](https://arxiv.org/abs/2610.26216) `cs.CV` |
| 2026-10-16 | **A Language-Informed Loss for Visual Generation** | Suchir Agarwal, Keshigeyan Chandrasegaran et al. | End-to-end visual generation with pixel-space loss has recently achieved competitive performanc… | [📄 2610.23653](https://arxiv.org/abs/2610.23653) `cs.CV` |
| 2026-10-14 | **Intern Lumina U2: A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding and Image Generation** | Qian Yu, Zongyang Qiu et al. | Unified multimodal generation covers discrete, continuous, and hybrid paradigms… | [📄 2610.20818](https://arxiv.org/abs/2610.20818) `cs.CV` |
| 2026-10-09 | **MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement** | Chenge Li, Yefei He et al. | Efficient visual tokenization requires balancing representation compactness with the preservati… | [📄 2610.13181](https://arxiv.org/abs/2610.13181) `cs.CV` |
| 2026-10-07 | **QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation** | Yucheng Mao, Zeyuan Chen et al. | QuadTok, a novel framework for visual tokenization and autoregressive image generation… | [📄 2610.10497](https://arxiv.org/abs/2610.10497) `cs.CV` |
| 2026-09-29 | **NesTok: Nested Self-Aligned 1D Tokenizer for Autoregressive Image Generation** | Jiawei Zhang, Shuhao Liu et al. | One-dimensional (1D) variable-length visual tokenizers enable adaptive compression by varying t… | [📄 2609.36756](https://arxiv.org/abs/2609.36756) `cs.CV` |
| 2026-11-05 | **Towards Practical 20 kbps Generative Video Compression via Adaptive Tokenization and Entropy Modeling** | Jiancheng Zhao, Jixiang Luo et al. | Video compression at ultra-low bitrates remains challenging due to the loss of perceptually imp… | [📄 2611.08099](https://arxiv.org/abs/2611.08099) `cs.CV` |
| 2026-11-03 | **TEMPO: Time Series Understanding via Discrete Tokenization** | Riccardo Maggioni | Time-series interpretation often requires both numerical observations and textual context… | [📄 2611.04482](https://arxiv.org/abs/2611.04482) `cs.CL` |
| 2026-10-30 | **MoETok: Sparse Expert Routing for 1D Visual Tokenizers** | Jiahao Guo, Bao Tang et al. | Modern visual tokenizers aim to preserve fine-grained visual details while learning high-level… | [📄 2610.41992](https://arxiv.org/abs/2610.41992) `cs.CV` |
| 2025-03-01 | **FlowMo** | — | Flow-based tokenizer | [📄 2503.11056](https://arxiv.org/abs/2503.11056) `catalog` |
| 2025-03-01 | **NFIG** | — | Non-uniform flow image generation tokenizer | [📄 2503.07076](https://arxiv.org/abs/2503.07076) `catalog` |
| 2025-03-01 | **FAR** | — | Frequency autoregressive generation with continuous tokens in frequency domain | [📄 2503.05305](https://arxiv.org/abs/2503.05305) [💻](https://github.com/yuhuUSTC/FAR) `catalog` |
| 2025-03-01 | **USP** | — | Unified self-supervised pretraining shared by image generation and understanding | [📄 2503.06132](https://arxiv.org/abs/2503.06132) [💻](https://github.com/cxxgtxy/USP) `catalog` |
| 2025-02-01 | **QLIP** | — | Quantized language-image pretraining | [📄 2502.05178](https://arxiv.org/abs/2502.05178) `catalog` |
| 2025-02-01 | **FlexTok** | — | Flexible image tokenization | [📄 2502.13967](https://arxiv.org/abs/2502.13967) `catalog` |
| 2025-02-01 | **EQ-VAE** | — | Equivariant tokenizer | [📄 2502.09509](https://arxiv.org/abs/2502.09509) [💻](https://github.com/zelaki/eqvae) `catalog` |
| 2025-02-01 | **MAETok** | — | Masked autoencoders as effective continuous tokenizers for diffusion models | [📄 2502.03444](https://arxiv.org/abs/2502.03444) [💻](https://github.com/Hhhhhhao/continuous_tokenizer) `catalog` |
| 2025-01-01 | **VA-VAE** | — | Resolves reconstruction-generation tradeoff in latent diffusion via improved VAE training | [📄 2501.01423](https://arxiv.org/abs/2501.01423) [💻](https://github.com/hustvl/LightningDiT) `catalog` |
| 2024-12-01 | **TokenFlow** | — | Unified image tokenizer | [📄 2412.03069](https://arxiv.org/abs/2412.03069) [💻](https://github.com/ByteFlow-AI/TokenFlow) `catalog` |
| 2024-12-01 | **VidTok** | — | Video tokenizer (Microsoft) | [📄 2412.13061](https://arxiv.org/abs/2412.13061) [💻](https://github.com/microsoft/VidTok) `catalog` |
| 2024-12-01 | **SoftVQ-VAE** | — | Efficient 1D continuous tokenizer combining VQ and VAE advantages | [📄 2412.10958](https://arxiv.org/abs/2412.10958) [💻](https://github.com/Hhhhhhao/continuous_tokenizer) `catalog` |
| 2024-12-01 | **ViLex** | — | Visual lexicon encoding rich image features in the language token space | [📄 2412.06774](https://arxiv.org/abs/2412.06774) `catalog` |
| 2024-12-01 | **XQ-GAN** | — | Open-source image tokenization framework with extended quantization for AR generation | [📄 2412.01762](https://arxiv.org/abs/2412.01762) [💻](https://github.com/lxa9867/ImageFolder) `catalog` |
| 2024-11-01 | **SimVQ** | — | Addresses representation collapse in VQ models with a single linear layer | [📄 2411.02038](https://arxiv.org/abs/2411.02038) [💻](https://github.com/youngsheen/SimVQ) `catalog` |
| 2024-10-01 | **MAGVIT-v2** | — | LFQ-based video tokenizer | [📄 2310.05737](https://arxiv.org/abs/2310.05737) `catalog` |
| 2024-10-01 | **ElasticTok** | — | Adaptive token length tokenizer | [📄 2410.08368](https://arxiv.org/abs/2410.08368) `catalog` |
| 2024-10-01 | **ImageFolder** | — | Autoregressive image generation with product-quantized folded tokens | [📄 2410.01756](https://arxiv.org/abs/2410.01756) [💻](https://github.com/lxa9867/ImageFolder) `catalog` |
| 2024-09-01 | **Open-MAGVIT2** | — | Open-source reproduction of MAGVIT-v2 LFQ tokenizer for democratizing visual generation | [📄 2409.04410](https://arxiv.org/abs/2409.04410) [💻](https://github.com/TencentARC/SEED-Voken) `catalog` |
| 2024-06-01 | **TiTok** | — | 1D tokenizer for images | [📄 2406.07550](https://arxiv.org/abs/2406.07550) [💻](https://github.com/bytedance/1d-tokenizer) `catalog` |
| 2024-06-01 | **LlamaGen** | — | Demonstrates autoregressive LLMs beat diffusion for scalable image generation | [📄 2406.06525](https://arxiv.org/abs/2406.06525) [💻](https://github.com/FoundationVision/LlamaGen) `catalog` |
| 2024-06-01 | **BSQ-ViT** | — | Binary spherical quantization for image/video tokenization with simple binary codes | [📄 2406.07548](https://arxiv.org/abs/2406.07548) [💻](https://github.com/zhaoyue-zephyrus/bsq-vit) `catalog` |
| 2024-04-01 | **VAR** | — | Visual autoregressive modeling | [📄 2404.02905](https://arxiv.org/abs/2404.02905) [💻](https://github.com/FoundationVision/VAR) `catalog` |
| 2024-03-01 | **UniCode** | — | Unified codebook for multimodal LLMs enabling joint image-text tokenization | [📄 2403.09072](https://arxiv.org/abs/2403.09072) `catalog` |
| 2024-03-01 | **V2L-Tokenizer** | — | Frozen LLM-based visual tokenizer mapping images to text token space | [📄 2403.07874](https://arxiv.org/abs/2403.07874) [💻](https://github.com/zh460045050/V2L-Tokenizer) `catalog` |
| 2023-12-01 | **MAGVIT** | — | Masked generative video transformer | [📄 2212.05199](https://arxiv.org/abs/2212.05199) `catalog` |
| 2023-09-01 | **FSQ** | — | Finite scalar quantization | [📄 2309.15505](https://arxiv.org/abs/2309.15505) `catalog` |
| 2023-06-01 | **SPAE** | — | Semantic pyramid autoencoder enabling multimodal generation with frozen LLMs | [📄 2306.17842](https://arxiv.org/abs/2306.17842) `catalog` |
| 2023-02-01 | **LQAE** | — | Language-quantized autoencoders for unsupervised text-image alignment | [📄 2302.00902](https://arxiv.org/abs/2302.00902) `catalog` |
| 2022-03-01 | **RQ-VAE** | — | Residual quantization VAE | [📄 2203.01941](https://arxiv.org/abs/2203.01941) `catalog` |
| 2022-02-01 | **MaskGIT** | — | Masked generative image transformer using bidirectional masked token prediction | [📄 2202.04200](https://arxiv.org/abs/2202.04200) `catalog` |
| 2021-12-01 | **VQGAN** | — | Taming Transformers for image synthesis | [📄 2012.09841](https://arxiv.org/abs/2012.09841) [💻](https://github.com/CompVis/taming-transformers) `catalog` |
| 2021-10-01 | **ViT-VQGAN** | — | Vector-quantized image modeling with improved VQGAN training | [📄 2110.04627](https://arxiv.org/abs/2110.04627) `catalog` |
| 2019-06-01 | **VQ-VAE-2** | — | Hierarchical VQ-VAE | [📄 1906.00446](https://arxiv.org/abs/1906.00446) `catalog` |
| 2017-11-01 | **VQ-VAE** | — | Neural discrete representation learning | [📄 1711.00937](https://arxiv.org/abs/1711.00937) `catalog` |
<!-- table:end papers -->
