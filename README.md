<div align="center">

# 🤖 Awesome Native Multimodal Models

<p align="center">
  <a href="https://github.com/your-username/Awesome-Native-Multimodal-Models/actions">
    <img src="https://github.com/your-username/Awesome-Native-Multimodal-Models/actions/workflows/deploy.yml/badge.svg" alt="Build & Deploy"/>
  </a>
  <img src="https://img.shields.io/badge/Papers-400%2B-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Models-111%2B-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Landmarks-26-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Updated-2026--03-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PRs-Welcome-ff69b4?style=for-the-badge" />
</p>

<p align="center">
  <b>A comprehensive, auto-validated collection of <em>Native Multimodal Models</em> —<br/>
  models with <em>unified tokenization</em>, <em>end-to-end cross-modal training</em>,<br/>
  and <em>shared computation paths</em> across text, image, audio, and video.<br/>
  Covering 2017–2026 · Interactive D3.js visualizations · 17-rule CI/CD validation.</b>
</p>

> 💡 **"Native Multimodal"** = shared computation paths + unified tokenization + end-to-end cross-modal training.
> Distinguished from modular MLLMs (e.g., LLaVA) that add a visual adapter on top of a frozen LLM.

🔗 **Related Repos:** &nbsp;
[Awesome-Unified-Multimodal-Models](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) ·
[John-Ge/Awesome-Native-Multimodal-Models](https://github.com/John-Ge/Awesome-Native-Multimodal-Models) ·
[Awesome-Multimodal-LLMs](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models)

</div>

---

## 🌐 Interactive Visualizations

> Auto-generated on every push via GitHub Actions · Hosted on GitHub Pages

| 📊 Page | 🔗 Link | Description |
|---------|---------|-------------|
| 🌲 Architecture Taxonomy | [taxonomy.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/taxonomy.html) | Collapsible D3.js tree · 5 branches · 111 leaf models · hover for paper links |
| 📅 Model Timeline | [timeline.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/timeline.html) | Swim-lane timeline 2017–2026 · zoom & pan · category filters · minimap |
| 🔍 Validation Report | [validation_report.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/validation_report.html) | Data quality dashboard · Chart.js · JSON export |
| 🏠 Index | [index.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/index.html) | Landing page with live stats |

### 🌲 Architecture Taxonomy (Static)
![Taxonomy Tree](assets/taxonomy_tree.png)

### 📅 Model Timeline (Static)
![Timeline](assets/timeline.png)

---

## 📑 Table of Contents

- [🤔 What is Native Multimodal?](#-what-is-native-multimodal)
- [📊 Statistics at a Glance](#-statistics-at-a-glance) 
- [🔥 Research Trends & Key Insights](#-research-trends--key-insights)
- [🔍 Survey Papers](#-survey-papers)
- [🌳 Architecture Taxonomy (111 leaves)](#-architecture-taxonomy)
- [🗺️ How to Choose / Research Roadmap](#️-how-to-choose--research-roadmap)
- [🔢 Image & Video Tokenizers](#-image--video-tokenizers)
  - [Discrete VQ Tokenizers](#discrete-vq-tokenizers)
  - [Residual Quantization (RQ)](#residual-quantization-rq)
  - [Finite Scalar Quantization (FSQ)](#finite-scalar-quantization-fsq)
  - [Lookup-Free Quantization (LFQ)](#lookup-free-quantization-lfq)
  - [Binary Spherical Quantization (BSQ)](#binary-spherical-quantization-bsq)
  - [Product Quantization (PQ)](#product-quantization-pq)
  - [Continuous VAE Tokenizers](#continuous-vae-tokenizers)
  - [Text-Aligned Tokenizers](#text-aligned-tokenizers)
- [🖼️ Unified Image Understanding & Generation](#️-unified-image-understanding--generation-models)
  - [Diffusion-Based Unified Models](#diffusion-based-unified-models)
  - [AR Pixel-Encoding Models](#ar-pixel-encoding-models)
  - [AR Semantic-Encoding Models](#ar-semantic-encoding-models)
  - [Hybrid AR + Diffusion Models](#hybrid-ar--diffusion-models)
- [🌐 Any-to-Any Multimodal Models](#-any-to-any-multimodal-models)
- [🌟 2025 Notable Papers Spotlight](#-2025-notable-papers-spotlight)
- [🎙️ Omni Models](#️-omni-models-audio--video--image--text)
- [🧠 Multimodal Pretraining Foundations](#-multimodal-pretraining-foundations)
- [📋 Tracked Model Tables (by category, 111 models)](#-tracked-model-tables-by-category)
- [⭐ Landmark Models Timeline (26 models)](#-landmark-models-timeline)
- [📈 Growth Trend](#-growth-trend)
- [🏆 Performance Leaderboards](#-performance-leaderboards)
- [📊 Benchmarks & Evaluation](#-benchmarks--evaluation)
- [🗂️ Datasets](#️-datasets)
- [🏗️ Repository Structure](#️-repository-structure)
- [🚀 Quick Start](#-quick-start)
- [➕ How to Add a Model](#-how-to-add-a-model)
- [🔬 Validation Rules](#-validation-rules)
- [⚙️ GitHub Actions CI/CD](#️-github-actions-cicd)
- [📌 Related Awesome Lists](#-related-awesome-lists)
- [🤝 Contributing](#-contributing)
- [📜 Citation](#-citation)
- [📄 License](#-license)

---

## 🤔 What is Native Multimodal?

**Native Multimodal Models** are models that natively handle multiple modalities — text, image, audio, video — within a **unified architecture**, as opposed to modular, adapter-based approaches.

| Aspect | Native Multimodal | Modular MLLM |
|--------|-------------------|--------------|
| Tokenization | ✅ Unified token space for all modalities | ❌ Separate encoders per modality |
| Computation | ✅ Shared Transformer across modalities | ❌ Frozen LLM + adapter layers |
| Training | ✅ End-to-end cross-modal pre-training | ❌ Two-stage adapter tuning |
| Generation | ✅ Native multi-modal output | ❌ External decoder required |
| Examples | Chameleon, Emu3, Janus-Pro, BAGEL | LLaVA, InstructBLIP, MiniGPT-4 |

> 🔑 Key insight: Native models learn **shared representations** across modalities from scratch,
> enabling emergent cross-modal reasoning not achievable by modular designs.

### 🔍 Is a Model "Native Multimodal"? Decision Flow

```
Is the model designed to process multiple modalities?
     │
     ├── NO  → Not a multimodal model
     │
     └── YES → Does it use a unified token space (visual tokens ↔ text tokens)?
                   │
                   ├── NO  → Modular MLLM (LLaVA, MiniGPT-4, InstructBLIP...)
                   │         [visual encoder frozen / adapter-based]
                   │
                   └── YES → Does it do end-to-end cross-modal training?
                                 │
                                 ├── NO  → Hybrid (CLIP-style contrastive only)
                                 │
                                 └── YES → ✅ NATIVE MULTIMODAL MODEL
                                           [Chameleon, Emu3, Janus-Pro, BAGEL...]
```

---

## 📊 Statistics at a Glance

| Metric | Value |
|--------|-------|
| 📚 Total tracked models | **111** |
| 🌿 Taxonomy leaf nodes | **111** |
| ⭐ Landmark models | **26** (23% of total) |
| 📄 Models with arXiv | **104** (94%) |
| 💻 Models with GitHub | **32** (29%) |
| 📅 Year range | **2017–2026** (9 years) |
| 🏗️ Categories | **5** |
| ✅ Validation rules | **17** |

**Category breakdown (tracked models):**

```
Pretraining Foundations  ████████████████            16 models  (18%)
Image & Video Tokenizers ████████████████████        17 models  (20%)
Unified U+G              ████████████████████████████ 27 models (31%)
Any-to-Any               ████████████                11 models  (13%)
Omni Models              ████████████████            16 models  (18%)
```

**Category breakdown (table):**

| Category | Tracked Models | Taxonomy Leaves |
|----------|---------------|-----------------|
| Pretraining Foundations | 0 | 0 |
| Image & Video Tokenizers | 0 | 0 |
| Unified Understanding + Generation | 0 | 0 |
| Any-to-Any Multimodal | 0 | 0 |
| Omni Models | 0 | 0 |

---

## 🔥 Research Trends & Key Insights

> Auto-computed from tracked model data · Last updated: March 2026

### 📈 The 2025 Explosion

The field underwent a **phase transition** in 2025: more native multimodal models were published than in all prior years combined.

```
2017 ▏█                              (1)
2018 ▏                               (0)
2019 ▏█                              (1)
2020 ▏                               (0)
2021 ▏███                            (3)
2022 ▏█████                          (5)
2023 ▏██████████                     (10)
2024 ▏█████████████████████████      (25)
2025 ▏█████████████████████████████████████████  (41) ← 47% of all models
2026 ▏█                              (1)
```

### 🏗️ Five Architectural Waves

| Wave | Period | Paradigm | Representative Models |
|------|--------|----------|-----------------------|
| **1st** | 2017–2021 | Discrete Visual Tokenization | VQ-VAE, VQGAN, CLIP |
| **2nd** | 2022–2023 | Foundation Pretraining | BLIP-2, Flamingo, CoDi, NExT-GPT |
| **3rd** | 2024 Q1–Q2 | Early-Fusion AR | Chameleon, LWM, Emu3, Transfusion |
| **4th** | 2024 Q3–2025 Q1 | Decoupled Semantic AR | Janus-Pro, ILLUME+, Show-o, BAGEL |
| **5th** | 2025 Q2+ | Omni + RL-Alignment | OmniGen2, Show-o2, BLIP3-o, Qwen3-Omni |

### 🔑 Key Technical Trends

**① Tokenizer Renaissance (2024–2025)**
- Shift from discrete VQ → continuous VAE → hybrid tokenizers
- 1D tokenizers (TiTok, FlexTok, UniTok) reduce token count by 4–16×
- Text-aligned tokenizers (QLIP, DualToken) bridge vision and language spaces natively

**② Decoupled Encoding Paradigm**
- Janus (2024): decouple visual encoder for understanding vs. generation
- Insight: a single shared encoder creates conflicting optimization objectives
- Trend: specialized heads + shared backbone → best of both worlds

**③ AR + Diffusion Hybrids Dominate (2025)**
- Show-o, Transfusion, BAGEL, BLIP3-o, LlamaFusion all combine AR tokens + diffusion
- AR handles text + semantic reasoning; Diffusion handles perceptual quality
- BAGEL (2025/05) demonstrates "emerging properties" from unified pretraining

**④ Proprietary → Open-Source Convergence**
- GPT-4o (2024/05): set the target; closed-source
- Qwen2.5-Omni (2025/03), InternVL3 (2025/04): rapidly closed the gap
- Gemini 3.1 Pro (2026/02): continued arms race

**⑤ RL Alignment for Unified Models**
- X-Omni (2025/07): RL makes discrete AR image generation competitive
- MiMo-VL (2025/06): RL for vision-language reasoning
- Trend: RLHF/GRPO extending from text-only to full multimodal models

### 🚀 Hottest Subfields (by 2025 paper velocity)

| Subfield | 2025 Papers | Key Challenge |
|----------|-------------|---------------|
| Hybrid AR+Diffusion Unified | 13 | Balancing discrete text + continuous visual |
| Visual Tokenizer Design | 11 | Reconstruction ↔ generation tradeoff |
| Omni Models (speech+vision) | 8 | Real-time streaming, low latency |
| AR Semantic Unified | 9 | Decoupled vs. shared encoder |
| Any-to-Any Full-Modal | 7 | Audio+video+3D beyond image+text |

### 💡 Open Research Problems

1. **Tokenizer-Model Co-design** — Current tokenizers are often trained independently; co-optimizing with the LLM backbone remains underexplored
2. **Long Video Understanding** — Most models handle images/short clips; million-frame video is unsolved
3. **3D & Embodied Modalities** — Audio + video + 3D point clouds + actions in one unified model
4. **Evaluation Gap** — No single benchmark covers understanding + generation + omni jointly
5. **Efficient Inference** — Most unified models are 7B+; sub-1B native multimodal remains challenging
6. **Data Curation at Scale** — High-quality interleaved image-text-audio data is scarce vs. text-only

---
## 🔍 Survey Papers

> 💡 **Recommended reading order for newcomers:**
> 1. VQ-VAE (tokenization fundamentals) → 2. CLIP (contrastive pretraining) → 
> 3. BLIP-2 (generative pretraining) → 4. Chameleon (early-fusion) → 
> 5. Janus-Pro (decoupled AR) → 6. BAGEL (hybrid unified) → 7. The surveys below

| Title | Venue | Date | Paper | Code |
|-------|-------|------|-------|------|
| A Comprehensive Survey of Multimodal Pretraining, Native Foundation Models, and Omni-Native Architectures | - | 2025 | [PDF](native-multimodal_survey.pdf) | - |
| **Unified Multimodal Understanding and Generation Models: A Survey** | arXiv | 2025/05 | [arXiv:2505.02567](https://arxiv.org/abs/2505.02567) | [GitHub](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) |
| A Survey on Large Multimodal Reasoning Models | arXiv | 2025/05 | [arXiv:2505.04921](https://arxiv.org/html/2505.04921v1) | - |
| Vision Encoders in Vision-Language Models: A Survey | Jina AI | 2025 | [PDF](https://jina.ai/vision-encoder-survey.pdf) | - |
| A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models | arXiv | 2025/02 | [arXiv:2502.17516](https://arxiv.org/html/2502.17516v1) | - |
| Representation Potentials of Foundation Models for Multimodal Tasks | arXiv | 2025/10 | [arXiv:2510.05184](https://arxiv.org/html/2510.05184v1) | - |
| Discrete Tokenization for Multimodal LLMs: A Survey | arXiv | 2025/07 | [arXiv:2507.22920](https://arxiv.org/pdf/2507.22920) | - |
| A Survey of Architectural Design in Large Vision-Language Models | TechRxiv | 2025 | [PDF](https://www.techrxiv.org) | - |
| A Comprehensive Survey of Efficient Multimodal Learning | TechRxiv | 2025 | [PDF](https://www.techrxiv.org/users/1011886/articles/1372030) | - |

---

## 🌳 Architecture Taxonomy

> Full taxonomy with {total_leaves} leaf models across 5 top-level branches.
> Interactive version: [taxonomy.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/taxonomy.html)

```
Native Multimodal Models
    ├── Image & Video Tokenizers
    │   ├── Discrete VQ
    │   │   ├── VQ-VAE
    │   │   ├── VQ-VAE-2
    │   │   ├── VQGAN
    │   │   ├── ViT-VQGAN
    │   │   ├── MaskGIT
    │   │   ├── MAGVIT
    │   │   ├── TiTok
    │   │   ├── UniCode
    │   │   ├── LlamaGen
    │   │   ├── TokenFlow
    │   │   ├── SimVQ
    │   │   └── SoftVQ-VAE
    │   ├── Residual VQ (RQ)
    │   │   ├── RQ-VAE
    │   │   ├── VAR
    │   │   └── NFIG
    │   ├── FSQ
    │   │   ├── FSQ
    │   │   ├── ElasticTok
    │   │   ├── VidTok
    │   │   └── FlexTok
    │   ├── LFQ
    │   │   ├── MAGVIT-v2
    │   │   ├── Open-MAGVIT2
    │   │   └── FlowMo
    │   ├── BSQ / PQ
    │   │   ├── BSQ-ViT
    │   │   ├── QLIP
    │   │   ├── ImageFolder
    │   │   └── XQ-GAN
    │   ├── Continuous VAE
    │   │   ├── VA-VAE
    │   │   ├── EQ-VAE
    │   │   ├── MAETok
    │   │   ├── FAR
    │   │   └── USP
    │   └── Text-Aligned
    │       ├── LQAE
    │       ├── SPAE
    │       ├── V2L-Tokenizer
    │       └── ViLex
    ├── Unified U+G
    │   ├── Diffusion-Based
    │   │   ├── UniDisc
    │   │   ├── MMaDA
    │   │   ├── Muddit
    │   │   └── FUDOKI
    │   ├── AR Pixel-Encoding
    │   │   ├── LWM
    │   │   ├── Chameleon
    │   │   ├── ANOLE
    │   │   ├── Emu3
    │   │   ├── Liquid
    │   │   ├── SynerGen-VL
    │   │   ├── Selftok
    │   │   ├── TokLIP
    │   │   └── Harmon
    │   ├── AR Semantic
    │   │   ├── SEED
    │   │   ├── LaVIT
    │   │   ├── Emu
    │   │   ├── DreamLLM
    │   │   ├── Janus
    │   │   ├── Janus-Pro
    │   │   ├── OmniGen2
    │   │   ├── MUSE-VL
    │   │   ├── MetaQuery-XL
    │   │   └── VARGPT-v1.1
    │   └── Hybrid AR+Diff
    │       ├── Transfusion
    │       ├── Show-o
    │       ├── LlamaFusion
    │       ├── BAGEL
    │       ├── BLIP3-o
    │       ├── Show-o2
    │       └── HermesFlow
    ├── Any-to-Any
    │   ├── Discrete AR
    │   │   ├── NExT-GPT
    │   │   ├── AnyGPT
    │   │   ├── MIO
    │   │   ├── Spider
    │   │   ├── Ming-Omni
    │   │   └── Qwen3-Omni
    │   ├── Composable Diffusion
    │   │   ├── CoDi
    │   │   ├── CoDi-2
    │   │   └── OmniFlow
    │   └── Omni-AR Full-Modal
    │       ├── Unified-IO 2
    │       ├── X-VILA
    │       ├── M2-omni
    │       └── InteractiveOmni-A2A
    ├── Omni Models
    │   ├── Proprietary
    │   │   ├── GPT-4o
    │   │   ├── Gemini 1.5 Pro
    │   │   ├── Gemini 2.0 Flash
    │   │   ├── Gemini 2.5 Pro
    │   │   ├── Gemini 3.1 Pro
    │   │   └── Step3
    │   ├── Open-Source
    │   │   ├── VITA
    │   │   ├── VITA-1.5
    │   │   ├── MiniCPM-o 2.6
    │   │   ├── MiniCPM-o 4.5
    │   │   ├── Qwen2.5-Omni
    │   │   ├── InternVL3
    │   │   ├── InternVL3-Omni
    │   │   ├── Seed1.5-VL
    │   │   └── NExT-OMNI
    │   └── Speech-First
    │       ├── LLaMA-Omni
    │       ├── SALMONN-Omni
    │       └── InteractiveOmni
    └── Pretraining Foundations
        ├── Contrastive
        │   ├── CLIP
        │   ├── ALIGN
        │   ├── SigLIP
        │   ├── EVA-CLIP
        │   └── SigLIP 2
        ├── Generative
        │   ├── BLIP-2
        │   ├── BEiT-3
        │   ├── OFA
        │   ├── Flamingo
        │   ├── i-Code
        │   └── CoCa
        └── VL Instruction
            ├── LLaVA
            ├── InternVL
            ├── Qwen2.5-VL
            └── MiMo-VL
```

---

## 🗺️ How to Choose / Research Roadmap

### For Researchers: Where to Start

```
What is your primary goal?
│
├── 📖 Understand the field from scratch?
│   └── Read: CLIP → BLIP-2 → Chameleon → Janus-Pro → BAGEL
│           (pretraining fundamentals → early-fusion → decoupled AR → hybrid)
│
├── 🔢 Work on Visual Tokenization?
│   ├── Discrete:   VQ-VAE → VQGAN → TiTok → MAGVIT-v2 → UniTok
│   ├── Continuous: VAE → VA-VAE → EQ-VAE → MAETok
│   └── Text-Aligned: LQAE → QLIP → DualToken
│
├── 🖼️ Unified Image Understanding + Generation?
│   ├── AR (pixel):    Chameleon → Emu3 → Liquid
│   ├── AR (semantic): Janus → Janus-Pro → VARGPT → MetaQuery-XL
│   ├── Diffusion:     UniDisc → MMaDA → FUDOKI
│   └── Hybrid:        Transfusion → Show-o → BAGEL → Show-o2
│
├── 🌐 Any-to-Any (text+image+audio+video)?
│   └── NExT-GPT → AnyGPT → MIO → Ming-Omni → Qwen3-Omni
│
└── 🎙️ Omni Real-Time Interaction?
    ├── Proprietary: GPT-4o → Gemini 2.5 Pro
    └── Open-Source: VITA → Qwen2.5-Omni → InternVL3 → MiniCPM-o
```

### Architecture Comparison: Key Design Axes

| Model | Visual Token | Text-Image Fusion | Generation Method | Modalities | Open? |
|-------|-------------|-------------------|-------------------|------------|-------|
| **Chameleon** | Discrete VQ (pixel) | Early fusion | AR next-token | T+I | ✅ |
| **Emu3** | Discrete VQ (pixel) | Early fusion | AR next-token | T+I+V | ✅ |
| **Janus-Pro** | Dual encoder | Decoupled | AR (VQGAN) | T+I | ✅ |
| **Transfusion** | Continuous | Late fusion | AR+Diffusion | T+I | ❌ |
| **Show-o** | Discrete+Continuous | Shared Transformer | AR+MaskDiff | T+I | ✅ |
| **BAGEL** | Continuous | Unified pretraining | AR+Diffusion | T+I | ✅ |
| **BLIP3-o** | Continuous CLIP | Hybrid | AR+Flow | T+I | ✅ |
| **Qwen2.5-Omni** | Continuous | Unified | AR+Diff | T+I+A+V | ✅ |
| **GPT-4o** | Unknown | Unknown | Unknown | T+I+A+V | ❌ |
| **NExT-GPT** | Discrete | Modular | AR (discrete) | T+I+A+V | ✅ |
| **OmniGen2** | Continuous | Semantic | Flow-based | T+I+multi | ✅ |
| **MMaDA** | Discrete | Unified diffusion | Masked Diffusion | T+I | ✅ |

> **Legend:** T=Text · I=Image · A=Audio · V=Video · AR=Autoregressive · Diff=Diffusion · MaskDiff=Masked Diffusion

---
## 🔢 Image & Video Tokenizers `50+ methods · 8 paradigms`

### Discrete VQ Tokenizers

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2017/11 | **VQ-VAE** | Neural Discrete Representation Learning | [arXiv:1711.00937](https://arxiv.org/abs/1711.00937) | - |
| 2019/06 | **VQ-VAE-2** | Generating Diverse High-Fidelity Images with VQ-VAE-2 | [arXiv:1906.00446](https://arxiv.org/abs/1906.00446) | - |
| 2020/12 | **VQGAN** | Taming Transformers for High-Resolution Image Synthesis | [arXiv:2012.09841](https://arxiv.org/abs/2012.09841) | [GitHub](https://github.com/CompVis/taming-transformers) |
| 2021/10 | **ViT-VQGAN** | Vector-Quantized Image Modeling with Improved VQGAN | [arXiv:2110.04627](https://arxiv.org/abs/2110.04627) | - |
| 2022/02 | **MaskGIT** | MaskGIT: Masked Generative Image Transformer | [arXiv:2202.04200](https://arxiv.org/abs/2202.04200) | - |
| 2022/09 | **MoVQ** | MoVQ: Modulating Quantized Vectors for High-Fidelity Image Generation | [arXiv:2209.09002](https://arxiv.org/abs/2209.09002) | - |
| 2022/12 | **MAGVIT** | MAGVIT: Masked Generative Video Transformer | [arXiv:2212.05199](https://arxiv.org/abs/2212.05199) | [GitHub](https://github.com/google-research/magvit) |
| 2024/03 | **UniCode** | UniCode: Learning a Unified Codebook for Multimodal LLMs | [arXiv:2403.09072](https://arxiv.org/abs/2403.09072) | - |
| 2024/05 | **Chameleon-VQ** | Chameleon: Mixed-Modal Early-Fusion Foundation Models | [arXiv:2405.09818](https://arxiv.org/abs/2405.09818) | [GitHub](https://github.com/facebookresearch/chameleon) |
| 2024/06 | **LlamaGen** | Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation | [arXiv:2406.06525](https://arxiv.org/abs/2406.06525) | [GitHub](https://github.com/FoundationVision/LlamaGen) |
| 2024/06 | **TiTok** | An Image is Worth 32 Tokens for Reconstruction and Generation | [arXiv:2406.07550](https://arxiv.org/abs/2406.07550) | [GitHub](https://github.com/bytedance/1d-tokenizer) |
| 2024/06 | **OmniTokenizer** | OmniTokenizer: A Joint Image-Video Tokenizer for Visual Generation | [arXiv:2406.09399](https://arxiv.org/abs/2406.09399) | [GitHub](https://github.com/FoundationVision/OmniTokenizer) |
| 2024/06 | **VQGAN-LC** | Scaling the Codebook Size of VQGAN to 100,000 | [arXiv:2406.11837](https://arxiv.org/abs/2406.11837) | - |
| 2024/09 | **MaskBit** | MaskBit: Embedding-free Image Generation via Bit Tokens | [arXiv:2409.16211](https://arxiv.org/abs/2409.16211) | [GitHub](https://github.com/markweberdev/maskbit) |
| 2024/10 | **DiGIT** | Stabilize the Latent Space for Image Autoregressive Modeling | [arXiv:2410.12490](https://arxiv.org/abs/2410.12490) | [GitHub](https://github.com/DAMO-NLP-SG/DiGIT) |
| 2024/10 | **RotationTrick** | Restructuring Vector Quantization with the Rotation Trick | [arXiv:2410.06424](https://arxiv.org/abs/2410.06424) | [GitHub](https://github.com/cfifty/rotation_trick) |
| 2024/10 | **BPE-VQ** | From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities | [arXiv:2410.02155](https://arxiv.org/abs/2410.02155) | - |
| 2024/11 | **FQGAN** | Factorized Visual Tokenization and Generation | [arXiv:2411.16681](https://arxiv.org/abs/2411.16681) | [GitHub](https://github.com/showlab/FQGAN) |
| 2024/11 | **VQ-KD** | Image Understanding Makes for A Good Tokenizer for Image Generation | [arXiv:2411.04406](https://arxiv.org/abs/2411.04406) | [GitHub](https://github.com/magic-research/vector_quantization) |
| 2024/11 | **SimVQ** | Addressing Representation Collapse in VQ Models with One Linear Layer | [arXiv:2411.02038](https://arxiv.org/abs/2411.02038) | [GitHub](https://github.com/youngsheen/SimVQ) |
| 2024/11 | **ALIT** | Adaptive Length Image Tokenization via Recurrent Allocation | [arXiv:2411.02393](https://arxiv.org/abs/2411.02393) | [GitHub](https://github.com/ShivamDuggal4/adaptive-length-tokenizer) |
| 2024/12 | **TokenFlow** | TokenFlow: Unified Image Tokenizer for Multimodal Understanding and Generation | [arXiv:2412.03069](https://arxiv.org/abs/2412.03069) | [GitHub](https://github.com/ByteFlow-AI/TokenFlow) |
| 2024/12 | **IBQ** | Scalable Image Tokenization with Index Backpropagation Quantization | [arXiv:2412.02692](https://arxiv.org/abs/2412.02692) | [GitHub](https://github.com/TencentARC/SEED-Voken) |
| 2024/12 | **SoftVQ-VAE** | SoftVQ-VAE: Efficient 1-Dimensional Continuous Tokenizer | [arXiv:2412.10958](https://arxiv.org/abs/2412.10958) | [GitHub](https://github.com/Hhhhhhao/continuous_tokenizer) |
| 2024/12 | **GSQ** | Scaling Image Tokenizers with Grouped Spherical Quantization | [arXiv:2412.02632](https://arxiv.org/abs/2412.02632) | [GitHub](https://github.com/HelmholtzAI-FZJ/flex_gen) |
| 2024/12 | **TexTok** | Language-Guided Image Tokenization for Generation | [arXiv:2412.05796](https://arxiv.org/abs/2412.05796) | [GitHub](https://kaiwenzha.github.io/textok/) |
| 2024/12 | **SIT** | Spectral Image Tokenizer | [arXiv:2412.09607](https://arxiv.org/abs/2412.09607) | - |
| 2024/12 | **CRT** | When Worse is Better: Navigating the Compression-Generation Tradeoff | [arXiv:2412.16326](https://arxiv.org/abs/2412.16326) | - |
| 2025/01 | **TA-TiTok** | Democratizing Text-to-Image Masked Generative Models with Compact 1D Tokens | [arXiv:2501.07730](https://arxiv.org/abs/2501.07730) | [GitHub](https://github.com/bytedance/1d-tokenizer) |
| 2025/01 | **One-D-Piece** | One-D-Piece: Image Tokenizer Meets Quality-Controllable Compression | [arXiv:2501.10064](https://arxiv.org/abs/2501.10064) | [GitHub](https://github.com/turingmotors/One-D-Piece) |
| 2025/02 | **UniTok** | UniTok: A Unified Tokenizer for Visual Generation and Understanding | [arXiv:2502.20321](https://arxiv.org/abs/2502.20321) | [GitHub](https://github.com/FoundationVision/UniTok) |
| 2025/03 | **DualToken** | DualToken: Towards Unifying Visual Understanding and Generation with Dual Visual Vocabularies | [arXiv:2503.14324](https://arxiv.org/abs/2503.14324) | [GitHub](https://github.com/songweii/DualToken) |
| 2025/03 | **SemHiTok** | SemHiTok: A Unified Image Tokenizer via Semantic-Guided Hierarchical Codebook | [arXiv:2503.06764](https://arxiv.org/abs/2503.06764) | - |
| 2025/03 | **V2Flow** | V2Flow: Unifying Visual Tokenization and LLM Vocabularies for AR Image Generation | [arXiv:2503.07493](https://arxiv.org/abs/2503.07493) | [GitHub](https://github.com/zhangguiwei610/V2Flow) |
| 2025/03 | **PCA Tokenizer** | Principal Components Enable A New Language of Images | [arXiv:2503.08685](https://arxiv.org/abs/2503.08685) | [GitHub](https://github.com/visual-gen/semanticist) |
| 2025/03 | **TokenSet** | Tokenize Image as a Set | [arXiv:2503.16425](https://arxiv.org/abs/2503.16425) | [GitHub](https://github.com/Gengzigang/TokenSet) |
| 2025/03 | **TokenBridge** | Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation | [arXiv:2503.16430](https://arxiv.org/abs/2503.16430) | [Project](https://yuqingwang1029.github.io/TokenBridge/) |
| 2025/03 | **CTF** | Improving Autoregressive Image Generation through Coarse-to-Fine Token Prediction | [arXiv:2503.16194](https://arxiv.org/abs/2503.16194) | [GitHub](https://github.com/GzyAftermath/CTF) |

### Residual Quantization (RQ)

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2022/03 | **RQ-VAE** | Autoregressive Image Generation using Residual Quantization | [arXiv:2203.01941](https://arxiv.org/abs/2203.01941) | [GitHub](https://github.com/kakaobrain/rq-vae-transformer) |
| 2024/04 | **VAR** | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | [arXiv:2404.02905](https://arxiv.org/abs/2404.02905) | [GitHub](https://github.com/FoundationVision/VAR) |
| 2025/03 | **NFIG** | NFIG: Autoregressive Image Generation with Next-Frequency Prediction | [arXiv:2503.07076](https://arxiv.org/abs/2503.07076) | - |

### Finite Scalar Quantization (FSQ)

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2023/09 | **FSQ** | Finite Scalar Quantization: VQ-VAE Made Simple | [arXiv:2309.15505](https://arxiv.org/abs/2309.15505) | [GitHub](https://github.com/google-research/google-research/tree/master/fsq) |
| 2024/10 | **ElasticTok** | ElasticTok: Adaptive Tokenization for Image and Video | [arXiv:2410.08368](https://arxiv.org/abs/2410.08368) | [GitHub](https://github.com/LargeWorldModel/ElasticTok) |
| 2024/12 | **VidTok** | VidTok: A Versatile and Open-Source Video Tokenizer | [arXiv:2412.13061](https://arxiv.org/abs/2412.13061) | [GitHub](https://github.com/microsoft/VidTok) |
| 2025/02 | **FlexTok** | FlexTok: Resampling Images into 1D Token Sequences of Flexible Length | [arXiv:2502.13967](https://arxiv.org/abs/2502.13967) | - |

### Lookup-Free Quantization (LFQ)

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2023/10 | **MAGVIT-v2** | Language Model Beats Diffusion: Tokenizer is Key to Visual Generation | [arXiv:2310.05737](https://arxiv.org/abs/2310.05737) | - |
| 2024/05 | **Libra** | Libra: Building Decoupled Vision System on Large Language Models | [arXiv:2405.10140](https://arxiv.org/abs/2405.10140) | [GitHub](https://github.com/YifanXu74/Libra) |
| 2024/09 | **Open-MAGVIT2** | Open-MAGVIT2: An Open-Source Project Toward Democratizing Auto-regressive Visual Generation | [arXiv:2409.04410](https://arxiv.org/abs/2409.04410) | [GitHub](https://github.com/TencentARC/SEED-Voken) |
| 2025/03 | **FlowMo** | Flow to the Mode: Mode-Seeking Diffusion Autoencoders for State-of-the-Art Image Tokenization | [arXiv:2503.11056](https://arxiv.org/abs/2503.11056) | [Project](https://kylesargent.github.io/flowmo) |

### Binary Spherical Quantization (BSQ)

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2024/06 | **BSQ-ViT** | Image and Video Tokenization with Binary Spherical Quantization | [arXiv:2406.07548](https://arxiv.org/abs/2406.07548) | [GitHub](https://github.com/zhaoyue-zephyrus/bsq-vit) |
| 2025/02 | **QLIP** | QLIP: Text-Aligned Visual Tokenization Unifies Auto-Regressive Multimodal Understanding and Generation | [arXiv:2502.05178](https://arxiv.org/abs/2502.05178) | [GitHub](https://github.com/NVlabs/QLIP) |

### Product Quantization (PQ)

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2024/10 | **ImageFolder** | ImageFolder: Autoregressive Image Generation with Folded Tokens | [arXiv:2410.01756](https://arxiv.org/abs/2410.01756) | [GitHub](https://github.com/lxa9867/ImageFolder) |
| 2024/12 | **XQ-GAN** | XQ-GAN: An Open-source Image Tokenization Framework for Autoregressive Generation | [arXiv:2412.01762](https://arxiv.org/abs/2412.01762) | [GitHub](https://github.com/lxa9867/ImageFolder) |

### Continuous VAE Tokenizers

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2013/12 | **VAE** | Auto-Encoding Variational Bayes | [arXiv:1312.6114](https://arxiv.org/abs/1312.6114) | - |
| 2024/12 | **Divot** | Divot: Diffusion Powers Video Tokenizer for Comprehension and Generation | [arXiv:2412.04432](https://arxiv.org/abs/2412.04432) | [GitHub](https://github.com/TencentARC/Divot) |
| 2025/01 | **VA-VAE** | Reconstruction vs. Generation: Taming Optimization Dilemma in Latent Diffusion Models | [arXiv:2501.01423](https://arxiv.org/abs/2501.01423) | [GitHub](https://github.com/hustvl/LightningDiT) |
| 2025/01 | **CAT** | CAT: Content-Adaptive Image Tokenization | [arXiv:2501.03120](https://arxiv.org/abs/2501.03120) | - |
| 2025/01 | **ViTok** | Learnings from Scaling Visual Tokenizers for Reconstruction and Generation | [arXiv:2501.09755](https://arxiv.org/abs/2501.09755) | [Project](https://vitok.github.io/) |
| 2025/02 | **EQ-VAE** | EQ-VAE: Equivariance Regularized Latent Space for Improved Generative Image Modeling | [arXiv:2502.09509](https://arxiv.org/abs/2502.09509) | [GitHub](https://github.com/zelaki/eqvae) |
| 2025/02 | **MAETok** | Masked Autoencoders Are Effective Tokenizers for Diffusion Models | [arXiv:2502.03444](https://arxiv.org/abs/2502.03444) | [GitHub](https://github.com/Hhhhhhao/continuous_tokenizer) |
| 2025/02 | **ReaLS** | Exploring Representation-Aligned Latent Space for Better Generation | [arXiv:2502.00359](https://arxiv.org/abs/2502.00359) | [GitHub](https://github.com/black-yt/ReaLS) |
| 2025/03 | **FAR** | Frequency Autoregressive Image Generation with Continuous Tokens | [arXiv:2503.05305](https://arxiv.org/abs/2503.05305) | [GitHub](https://github.com/yuhuUSTC/FAR) |
| 2025/03 | **USP** | USP: Unified Self-Supervised Pretraining for Image Generation and Understanding | [arXiv:2503.06132](https://arxiv.org/abs/2503.06132) | [GitHub](https://github.com/cxxgtxy/USP) |

### Text-Aligned Tokenizers

| Date | Method | Title | arXiv | Code |
|------|--------|-------|-------|------|
| 2023/02 | **LQAE** | Language Quantized AutoEncoders: Towards Unsupervised Text-Image Alignment | [arXiv:2302.00902](https://arxiv.org/abs/2302.00902) | - |
| 2023/06 | **SPAE** | SPAE: Semantic Pyramid AutoEncoder for Multimodal Generation with Frozen LLMs | [arXiv:2306.17842](https://arxiv.org/abs/2306.17842) | - |
| 2024/03 | **V2L-Tokenizer** | Beyond Text: Frozen Large Language Models in Visual Signal Comprehension | [arXiv:2403.07874](https://arxiv.org/abs/2403.07874) | [GitHub](https://github.com/zh460045050/V2L-Tokenizer) |
| 2024/12 | **ViLex** | Visual Lexicon: Rich Image Features in Language Space | [arXiv:2412.06774](https://arxiv.org/abs/2412.06774) | - |
| 2025/03 | **PCA Tokenizer** | Principal Components Enable A New Language of Images | [arXiv:2503.08685](https://arxiv.org/abs/2503.08685) | [GitHub](https://github.com/visual-gen/semanticist) |

---

## 🖼️ Unified Image Understanding & Generation Models `50+ models · 4 paradigms`

### Diffusion-Based Unified Models

| Name | Title | Venue | Date | Code | Demo |
|------|-------|-------|------|------|------|
| **Dual Diffusion** | Dual Diffusion for Unified Image Generation and Understanding | arXiv | 2024/12 | [GitHub](https://github.com/zijieli-Jlee/Dual-Diffusion) | - |
| **UniDisc** | Unified Multimodal Discrete Diffusion | arXiv | 2025/03 | [GitHub](https://github.com/alexanderswerdlow/unidisc) | [Project](https://unidisc.github.io/) |
| **MMaDA** | MMaDA: Multimodal Large Diffusion Language Models | arXiv | 2025/05 | [GitHub](https://github.com/Gen-Verse/MMaDA) | [Demo](https://huggingface.co/spaces/Gen-Verse/MMaDA) |
| **FUDOKI** | FUDOKI: Discrete Flow-based Unified Understanding and Generation | arXiv | 2025/05 | - | - |
| **Muddit** | Muddit: Liberating Generation Beyond Text-to-Image with a Unified Discrete Diffusion Model | arXiv | 2025/05 | [GitHub](https://github.com/M-E-AGI-Lab/Muddit) | - |
| **Lavida-O** | Lavida-O: Elastic Large Masked Diffusion Models for Unified Multimodal Understanding and Generation | arXiv | 2025/09 | [GitHub](https://github.com/jacklishufan/LaViDa-O) | - |
| **UniModel** | UniModel: A Visual-Only Framework for Unified Multimodal Understanding and Generation | arXiv | 2025/11 | - | - |

### AR Pixel-Encoding Models

| Name | Title | Venue | Date | Code | Demo |
|------|-------|-------|------|------|------|
| **LWM** | World Model on Million-Length Video And Language With Blockwise RingAttention | ICLR 2024 | 2024/02 | [GitHub](https://github.com/LargeWorldModel/LWM) | - |
| **Chameleon** | Chameleon: Mixed-Modal Early-Fusion Foundation Models | arXiv | 2024/05 | [GitHub](https://github.com/facebookresearch/chameleon) | - |
| **ANOLE** | ANOLE: An Open, Autoregressive, Native Large Multimodal Models for Interleaved Image-Text Generation | arXiv | 2024/07 | [GitHub](https://github.com/GAIR-NLP/anole) | - |
| **Emu3** | Emu3: Next-Token Prediction is All You Need | arXiv | 2024/09 | [GitHub](https://github.com/baaivision/Emu3) | [Demo](https://huggingface.co/spaces/BAAI/Emu3) |
| **MMAR** | MMAR: Towards Lossless Multi-Modal Auto-Regressive Probabilistic Modeling | arXiv | 2024/10 | - | - |
| **Orthus** | Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads | arXiv | 2024/11 | [GitHub](https://github.com/zhijie-group/Orthus) | - |
| **Liquid** | Liquid: Language Models are Scalable and Unified Multi-modal Generators | arXiv | 2024/12 | [GitHub](https://github.com/FoundationVision/Liquid) | [Demo](https://huggingface.co/spaces/Junfeng5/Liquid_demo) |
| **SynerGen-VL** | SynerGen-VL: Towards Synergistic Image Understanding and Generation with Vision Experts and Token Folding | arXiv | 2024/12 | - | - |
| **Selftok** | Selftok: Discrete Visual Tokens of Autoregression, by Diffusion, and for Reasoning | arXiv | 2025/05 | [GitHub](https://github.com/selftok-team/SelftokTokenizer) | - |
| **TokLIP** | TokLIP: Marry Visual Tokens to CLIP for Multimodal Comprehension and Generation | arXiv | 2025/05 | [GitHub](https://github.com/TencentARC/TokLIP) | - |
| **Harmon** | Harmonizing Visual Representations for Unified Multimodal Understanding and Generation | arXiv | 2025/03 | [GitHub](https://github.com/wusize/Harmon) | [Demo](https://huggingface.co/spaces/wusize/Harmon) |
| **UGen** | UGen: Unified Autoregressive Multimodal Model with Progressive Vocabulary Learning | arXiv | 2025/03 | - | - |
| **OneCAT** | OneCAT: Decoder-Only Auto-Regressive Model for Unified Understanding and Generation | arXiv | 2025/09 | [GitHub](https://github.com/onecat-ai/OneCAT) | - |
| **Emu3.5** | Emu3.5: Native Multimodal Models are World Learners | arXiv | 2025/10 | [GitHub](https://github.com/baaivision/Emu3.5) | - |
| **MammothModa2** | MammothModa2: A Unified AR-Diffusion Framework for Multimodal Understanding and Generation | arXiv | 2025/11 | [GitHub](https://github.com/bytedance/mammothmoda) | - |

### AR Semantic-Encoding Models

| Name | Title | Venue | Date | Code | Demo |
|------|-------|-------|------|------|------|
| **SEED** | Making Llama See and Draw with SEED Tokenizer | arXiv | 2023/10 | [GitHub](https://github.com/AILab-CVC/SEED/) | - |
| **LaVIT** | Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization | arXiv | 2023/09 | [GitHub](https://github.com/jy0205/LaVIT) | - |
| **DreamLLM** | DreamLLM: Synergistic Multimodal Comprehension and Creation | ICLR 2024 | 2023/09 | - | - |
| **Emu** | Generative Pretraining in Multimodality | ICLR 2024 | 2023/07 | - | - |
| **Emu2** | Generative Multimodal Models are In-Context Learners | CVPR 2024 | 2023/12 | - | - |
| **SEED-X** | SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation | arXiv | 2024/04 | - | - |
| **VILA-U** | VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation | arXiv | 2024/07 | - | - |
| **Video-LaVIT** | Video-LaVIT: Unified Video-Language Pre-training with Decoupled Visual-Motional Tokenization | arXiv | 2024/02 | - | - |
| **Janus** | Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation | arXiv | 2024/10 | [GitHub](https://github.com/deepseek-ai/Janus) | - |
| **JanusFlow** | JanusFlow: Harmonizing Autoregression and Rectified Flow for Unified Multimodal | arXiv | 2024/11 | [GitHub](https://github.com/deepseek-ai/Janus) | - |
| **Janus-Pro** | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | arXiv | 2025/01 | [GitHub](https://github.com/deepseek-ai/Janus) | [Demo](https://huggingface.co/spaces/deepseek-ai/Janus-Pro-7B) |
| **ILLUME** | ILLUME: Illuminating Your LLMs to See, Draw, and Self-Enhance | arXiv | 2024/11 | - | - |
| **ILLUME+** | ILLUME+: Illuminating Unified MLLM with Dual Visual Tokenization and Diffusion Refinement | arXiv | 2025/02 | - | - |
| **VARGPT** | VARGPT: Unified Understanding and Generation in a Visual Autoregressive MLLM | arXiv | 2025/01 | [GitHub](https://github.com/VARGPT-family/VARGPT) | - |
| **VARGPT-v1.1** | VARGPT-v1.1: Improve Fine-Grained Perception for Visual Autoregressive Generation | arXiv | 2025/03 | [GitHub](https://github.com/VARGPT-family/VARGPT) | - |
| **MetaQuery-XL** | MetaQuery: Expressive Visual Conditions for Multimodal Generation and Understanding | arXiv | 2025/03 | - | - |
| **TokenFlow-XL** | TokenFlow: Unified Image Tokenizer for Multimodal Understanding and Generation | CVPR 2025 | 2024/12 | [GitHub](https://github.com/ByteFlow-AI/TokenFlow) | - |
| **MUSE-VL** | MUSE-VL: Modeling Unified VLM through Semantic Discrete Encoding | arXiv | 2024/11 | - | - |
| **OmniGen** | OmniGen: Unified Image Generation | CVPR 2025 | 2024/09 | [GitHub](https://github.com/VectorSpaceLab/OmniGen) | - |
| **OmniGen2** | OmniGen2: Exploration to Advanced Multimodal Generation | [arXiv:2506.18871](https://arxiv.org/abs/2506.18871) | 2025/06 | [GitHub](https://github.com/VectorSpaceLab/OmniGen2) | [Demo](https://huggingface.co/spaces/OmniGen2/OmniGen2) |
| **OmniGen-AR** | OmniGen-AR: AutoRegressive Any-to-Image Generation | NeurIPS 2025 | 2025 | - | - |
| **Ovis-U1** | Ovis-U1 Technical Report | arXiv | 2025/06 | [GitHub](https://github.com/AIDC-AI/Ovis-U1) | [Demo](https://huggingface.co/spaces/AIDC-AI/Ovis-U1-3B) |
| **UniCode²** | UniCode²: Cascaded Large-scale Codebooks for Unified Multimodal Understanding and Generation | arXiv | 2025/06 | - | - |
| **Tar** | Vision as a Dialect: Unifying Visual Understanding and Generation via Text-Aligned Representations | arXiv | 2025/06 | [GitHub](https://github.com/csuhan/Tar) | [Demo](https://tar.csuhan.com/) |
| **UniWorld** | UniWorld: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation | arXiv | 2025/06 | [GitHub](https://github.com/PKU-YuanGroup/UniWorld-V1) | - |
| **UniFork** | UniFork: Exploring Modality Alignment for Unified Multimodal Understanding and Generation | arXiv | 2025/06 | [GitHub](https://github.com/tliby/UniFork) | - |
| **Pisces** | Pisces: An Auto-regressive Foundation Model for Image Understanding and Generation | arXiv | 2025/06 | - | - |
| **X-Omni** | X-Omni: RL Makes Discrete Autoregressive Image Generative Models Great Again | arXiv | 2025/07 | [GitHub](https://github.com/X-Omni-Team/X-Omni) | [Demo](https://huggingface.co/collections/X-Omni/x-omni-spaces-6888c64f38446f1efc402de7) |
| **Bifrost-1** | Bifrost-1: Bridging Multimodal LLMs and Diffusion Models with Patch-level CLIP Latents | arXiv | 2025/08 | [GitHub](https://github.com/HL-hanlin/Bifrost-1) | - |
| **Qwen-Image** | Qwen-Image Technical Report | arXiv | 2025/08 | [GitHub](https://github.com/QwenLM/Qwen-Image) | [Demo](https://huggingface.co/spaces/Qwen/Qwen-Image) |
| **Ming-UniVision** | Ming-UniVision: Joint Image Understanding and Generation with a Unified Continuous Tokenizer | arXiv | 2025/10 | [GitHub](https://github.com/inclusionAI/Ming-UniVision) | - |
| **OpenUni** | OpenUni: A Simple Baseline for Unified Multimodal Understanding and Generation | arXiv | 2025/05 | - | - |
| **UniGen** | UniGen: Enhanced Training & Test-Time Strategies for Unified Multimodal Understanding and Generation | arXiv | 2025/05 | - | - |

### Hybrid AR + Diffusion Models

| Name | Title | Venue | Date | Code | Demo |
|------|-------|-------|------|------|------|
| **Transfusion** | Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model | arXiv | 2024/08 | - | - |
| **Show-o** | Show-o: One Single Transformer to Unify Multimodal Understanding and Generation | ICLR 2025 | 2024/08 | [GitHub](https://github.com/showlab/Show-o) | - |
| **HermesFlow** | HermesFlow: Seamlessly Closing the Gap in Multimodal Understanding and Generation | arXiv | 2025/01 | - | - |
| **LlamaFusion** | LlamaFusion: Adapting Pretrained Language Models for Multimodal Generation | arXiv | 2024/11 | - | - |
| **D-DiT** | D-DiT: Diffusion Transformer with Dynamic Routing for Unified Multimodal Generation | arXiv | 2025/02 | - | - |
| **BAGEL** | BAGEL: Emerging Properties in Unified Multimodal Pretraining | [arXiv:2505.14683](https://arxiv.org/abs/2505.14683) | 2025/05 | [GitHub](https://github.com/ByteDance-Seed/Bagel) | [Demo](https://bagel-ai.org/) |
| **Hyper-BAGEL** | Hyper-Bagel: A Unified Acceleration Framework for Multimodal Understanding and Generation | arXiv | 2025/09 | [Project](https://hyper-bagel.github.io/) | - |
| **BLIP3-o** | BLIP3-o: A Family of Fully Open Unified Multimodal Models | arXiv | 2025/05 | [GitHub](https://github.com/JiuhaiChen/BLIP3o) | - |
| **BLIP3o-NEXT** | BLIP3o-NEXT: Next Frontier of Native Image Generation | arXiv | 2025/10 | - | - |
| **Show-o2** | Show-o2: Improved Native Unified Multimodal Models | NeurIPS 2025 | 2025/06 | [GitHub](https://github.com/showlab/Show-o) | [HuggingFace](https://huggingface.co/showlab/show-o2-1.5B) |
| **LatentLM** | Multimodal Latent Language Modeling with Next-Token Diffusion | arXiv | 2024/12 | - | - |
| **UniFluid** | UniFluid: Unified Autoregressive Visual Generation and Understanding with Continuous Tokens | arXiv | 2025/02 | - | - |
| **OmniMamba** | OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models | arXiv | 2025/02 | - | - |

---

## 🌐 Any-to-Any Multimodal Models `17 models`

| Name | Title | Venue | Date | Code | Demo |
|------|-------|-------|------|------|------|
| **CoDi** | Any-to-Any Generation via Composable Diffusion | NeurIPS 2023 | 2023/05 | [GitHub](https://github.com/microsoft/i-Code/tree/main/CoDi) | - |
| **NExT-GPT** | NExT-GPT: Any-to-Any Multimodal LLM | ICML 2024 | 2023/09 | [GitHub](https://github.com/NExT-GPT/NExT-GPT) | [Project](https://next-gpt.github.io/) |
| **AnyGPT** | AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling | ACL 2024 | 2024/02 | [GitHub](https://github.com/OpenMOSS/AnyGPT) | - |
| **Unified-IO 2** | Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action | CVPR 2024 | 2023/12 | [GitHub](https://github.com/allenai/unified-io-2) | - |
| **Video-LaVIT** | Video-LaVIT: Unified Video-Language Pre-training | arXiv | 2024/02 | - | - |
| **CoDi-2** | CoDi-2: In-Context Interleaved and Interactive Any-to-Any Generation | CVPR 2024 | 2023/11 | - | - |
| **X-VILA** | X-VILA: Cross-Modality Alignment and Large Multimodal Model | arXiv | 2024/05 | - | - |
| **MIO** | MIO: A Foundation Model on Multimodal Tokens | arXiv | 2024/09 | - | - |
| **Spider** | Spider: Any-to-Many Multimodal LLM | arXiv | 2024/11 | - | - |
| **OmniFlow** | OmniFlow: Any-to-Any Generation with Multi-Modal Rectified Flows | arXiv | 2024/12 | - | - |
| **M2-omni** | M2-Omni: Advancing Omni-MLLM for Competitive Performance with GPT-4o | arXiv | 2025/02 | - | - |
| **Ming-Omni** | Ming-Omni: A Unified Multimodal Model for Perception and Generation | NeurIPS 2025 | 2025/06 | [HuggingFace](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0) | - |
| **Qwen3-Omni** | Qwen3-Omni Technical Report | arXiv | 2025/09 | [GitHub](https://github.com/QwenLM/Qwen3-Omni) | - |
| **Ming-Flash-Omni** | Ming-Flash-Omni 2.0 | arXiv | 2025/10 | [HuggingFace](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0) | - |
| **LongCat-Flash-Omni** | LongCat-Flash-Omni | arXiv | 2025/11 | - | - |
| **ShapeLLM-Omni** | ShapeLLM-Omni: 3D Generation and Understanding Omni Model | NeurIPS 2025 | 2025/06 | [arXiv:2506.01853](https://arxiv.org/abs/2506.01853) | - |
| **InteractiveOmni** | InteractiveOmni: A Unified Omni-Modal Model for Audio-Visual Multi-Turn Dialogue | arXiv | 2025/10 | [arXiv:2510.13747](https://arxiv.org/abs/2510.13747) | - |

---

## 🌟 2025 Notable Papers Spotlight

> Curated highlights — architecturally novel or record-breaking models

| Quarter | Model | Why Notable | Links |
|---------|-------|-------------|-------|
| **2025 Q1** | **Janus-Pro** ⭐ | Decoupled dual-encoder design; SOTA unified AR | [arXiv](https://arxiv.org/abs/2501.17811) · [GitHub](https://github.com/deepseek-ai/Janus) · [Demo](https://huggingface.co/spaces/deepseek-ai/Janus-Pro-7B) |
| **2025 Q1** | **Qwen2.5-VL** ⭐ | Dynamic resolution + temporal grounding; top VQA scores | [arXiv](https://arxiv.org/abs/2502.13923) · [GitHub](https://github.com/QwenLM/Qwen2.5-VL) |
| **2025 Q1** | **QLIP** | Text-aligned BSQ tokenizer; unifies AR understanding+generation | [arXiv](https://arxiv.org/abs/2502.05178) · [GitHub](https://github.com/NVlabs/QLIP) |
| **2025 Q1** | **MMaDA** | Multimodal masked diffusion LM; text+image in one discrete space | [arXiv](https://arxiv.org/abs/2505.15809) · [GitHub](https://github.com/Gen-Verse/MMaDA) |
| **2025 Q1** | **UniDisc** | Fully discrete unified diffusion; no AR needed | [arXiv](https://arxiv.org/abs/2503.20853) · [GitHub](https://github.com/alexanderswerdlow/unidisc) |
| **2025 Q2** | **BAGEL** ⭐ | "Emerging properties" from large-scale unified pretraining | [arXiv](https://arxiv.org/abs/2505.14683) · [GitHub](https://github.com/ByteDance-Seed/Bagel) · [Demo](https://bagel-ai.org/) |
| **2025 Q2** | **InternVL3** | Native multimodal pretraining paradigm; open-source SOTA | [arXiv](https://arxiv.org/abs/2504.10479) · [GitHub](https://github.com/OpenGVLab/InternVL) |
| **2025 Q2** | **BLIP3-o** | Fully open unified model with CLIP latent diffusion | [arXiv](https://arxiv.org/abs/2505.09568) · [GitHub](https://github.com/JiuhaiChen/BLIP3o) |
| **2025 Q2** | **Show-o2** ⭐ | Improved discrete+continuous unified generation | [NeurIPS 2025] · [GitHub](https://github.com/showlab/Show-o) |
| **2025 Q2** | **OmniGen2** ⭐ | Advanced multi-task generation (editing, personalization, T2I) | [arXiv](https://arxiv.org/abs/2506.18871) · [GitHub](https://github.com/VectorSpaceLab/OmniGen2) · [Demo](https://huggingface.co/spaces/OmniGen2/OmniGen2) |
| **2025 Q2** | **Qwen2.5-Omni** ⭐ | Open-source GPT-4o level; real-time omni interaction | [arXiv](https://arxiv.org/abs/2503.20215) · [GitHub](https://github.com/QwenLM/Qwen2.5-Omni) |
| **2025 Q2** | **FlowMo** | Mode-seeking diffusion autoencoder; SOTA tokenization | [arXiv](https://arxiv.org/abs/2503.11056) · [Project](https://kylesargent.github.io/flowmo) |

---
## 🎙️ Omni Models (Audio + Video + Image + Text) `22 models`

### Proprietary / Semi-Open Models

| Name | Organization | Modalities | Date | Link |
|------|-------------|-----------|------|------|
| **GPT-4o** | OpenAI | text+image+audio+video | 2024/05 | [Blog](https://openai.com/index/hello-gpt-4o/) |
| **Gemini 1.5 Pro** | Google | text+image+audio+video | 2024/02 | [Blog](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) |
| **Gemini 2.0 Flash** | Google | text+image+audio+video+actions | 2024/12 | [Blog](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/) |
| **Gemini 2.5 Pro** | Google | text+image+audio+video | 2025/03 | [Blog](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| **Gemini 3.1 Pro** | Google | text+image+audio+video | 2026/02 | [Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/) |

### Open-Source Omni Models

| Name | Title | Venue | Date | Code | Demo |
|------|-------|-------|------|------|------|
| **VITA** | VITA: Towards Open-Source Interactive Omni Multimodal LLM | arXiv | 2024/08 | [GitHub](https://github.com/VITA-MLLM/VITA) | - |
| **VITA-1.5** | VITA-1.5: Towards GPT-4o Level Real-Time Vision and Speech Interaction | arXiv | 2025/01 | [GitHub](https://github.com/VITA-MLLM/VITA) | - |
| **VITA-E** | VITA-E: Efficient Omni Multimodal Large Language Model | arXiv | 2025/10 | [GitHub](https://github.com/Tencent/VITA/tree/VITA-E) | - |
| **VITA-VLA** | VITA-VLA: Embodied Vision-Language-Action Omni Model | arXiv | 2025 | - | - |
| **MiniCPM-o 2.6** | MiniCPM-o 2.6: A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming | arXiv | 2025/01 | [GitHub](https://github.com/OpenBMB/MiniCPM-o) | [Demo](https://minicpm-omni.openbmb.cn/) |
| **MiniCPM-o 4.5** | MiniCPM-o 4.5 | HuggingFace | 2025 | [HuggingFace](https://huggingface.co/openbmb/MiniCPM-o-4_5) | [Demo](https://minicpm-omni.openbmb.cn/) |
| **Qwen2.5-Omni** | Qwen2.5-Omni Technical Report | arXiv | 2025/03 | [GitHub](https://github.com/QwenLM/Qwen2.5-Omni) | [HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) |
| **Qwen3-Omni** | Qwen3-Omni Technical Report | arXiv | 2025/09 | [GitHub](https://github.com/QwenLM/Qwen3-Omni) | - |
| **NExT-OMNI** | NExT-OMNI: Unified Omni Multimodal Model | arXiv | 2025/10 | [GitHub](https://github.com/QwenLM/NExT-OMNI) | - |
| **InternVL3** | InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models | arXiv | 2025/04 | [GitHub](https://github.com/OpenGVLab/InternVL) | - |
| **InternVL3.5** | InternVL3.5: Advancing Open-Source Multimodal Models | arXiv | 2025/08 | [GitHub](https://github.com/OpenGVLab/InternVL) | - |
| **Seed1.5-VL** | Seed1.5-VL: A Powerful Vision-Language Foundation Model | arXiv | 2025 | [GitHub](https://github.com/ByteDance-Seed/Seed1.5-VL) | - |
| **MiMo-VL** | MiMo-VL Technical Report (Xiaomi) | arXiv | 2025/06 | [HuggingFace](https://huggingface.co/XiaomiMiMo/MiMo-VL-7B-RL) | - |
| **OmniVinci** | OmniVinci: Creative Omni Model | arXiv | 2025/10 | [GitHub](https://github.com/NVlabs/OmniVinci) | - |
| **LLaMA-Omni** | LLaMA-Omni: Seamless Speech Interaction with Large Language Models | arXiv | 2024/09 | [GitHub](https://github.com/ictnlp/LLaMA-Omni) | - |
| **SALMONN-Omni** | SALMONN-Omni: A Codec-Free LLM for Full-Duplex Speech Understanding and Generation | NeurIPS 2025 | 2025 | - | - |
| **InteractiveOmni** | InteractiveOmni: A Unified Omni-Modal Model for Audio-Visual Multi-Turn Dialogue | arXiv | 2025/10 | [arXiv:2510.13747](https://arxiv.org/abs/2510.13747) | - |
| **Step3** | Step3: Cost-Effective Multimodal Intelligence (StepFun, 321B MoE, 38B active) | - | 2025 | [Project](https://stepfun.ai/research/en/step3) | - |

---

## 🧠 Multimodal Pretraining Foundations `28+ models · 3 paradigms`

### Contrastive Pretraining

| Name | Title | Venue | Date | Code |
|------|-------|-------|------|------|
| **CLIP** | Learning Transferable Visual Models From Natural Language Supervision | ICML 2021 | 2021/02 | [GitHub](https://github.com/openai/CLIP) |
| **ALIGN** | Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision | ICML 2021 | 2021/02 | - |
| **SigLIP** | Sigmoid Loss for Language Image Pre-Training | ICCV 2023 | 2023/03 | [GitHub](https://github.com/google-research/big_vision) |
| **SigLIP 2** | SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding | arXiv | 2025 | - |
| **EVA-CLIP** | EVA-CLIP: Improved Training Techniques for CLIP at Scale | arXiv | 2023 | [GitHub](https://github.com/baaivision/EVA) |
| **MACD** | Multimodal Alignment via Contrastive Disentanglement | arXiv | 2024 | - |
| **ViKL** | Vision-Language Knowledge Learning via Contrastive Alignment | arXiv | 2024 | - |

### Generative & Masked Pretraining

| Name | Title | Venue | Date | Code |
|------|-------|-------|------|------|
| **BLIP** | BLIP: Bootstrapping Language-Image Pre-training | ICML 2022 | 2022/01 | [GitHub](https://github.com/salesforce/BLIP) |
| **BLIP-2** | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and LLMs | ICML 2023 | 2023/01 | [GitHub](https://github.com/salesforce/LAVIS/tree/main/projects/blip2) |
| **InstructBLIP** | InstructBLIP: Towards General Visual-Language Models with Instruction Tuning | NeurIPS 2023 | 2023/05 | [GitHub](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip) |
| **BEiT-3** | Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks | CVPR 2023 | 2022/08 | [GitHub](https://github.com/microsoft/unilm/tree/master/beit3) |
| **OFA** | OFA: Unifying Architectures, Tasks, and Modalities Through a Simple Sequence-to-Sequence Learning Framework | ICML 2022 | 2022/02 | [GitHub](https://github.com/OFA-Sys/OFA) |
| **Flamingo** | Flamingo: a Visual Language Model for Few-Shot Learning | NeurIPS 2022 | 2022/04 | - |
| **i-Code** | i-Code: An Integrative and Composable Multimodal Learning Framework | AAAI 2023 | 2022/05 | - |
| **i-Code V2** | i-Code V2: An Autoregressive Generation Framework over Vision-Language-Speech Data | arXiv | 2023 | - |
| **CoCa** | CoCa: Contrastive Captioners are Image-Text Foundation Models | TMLR | 2022 | - |
| **GIT** | GIT: A Generative Image-to-text Transformer for Vision and Language | TMLR | 2022 | [GitHub](https://github.com/microsoft/GenerativeImage2Text) |

### Vision-Language Understanding (MLLM Backbones)

| Name | Title | Venue | Date | Code |
|------|-------|-------|------|------|
| **LLaVA** | Visual Instruction Tuning | NeurIPS 2023 | 2023/04 | [GitHub](https://github.com/haotian-liu/LLaVA) |
| **LLaVA-1.5** | Improved Baselines with Visual Instruction Tuning | CVPR 2024 | 2023/10 | [GitHub](https://github.com/haotian-liu/LLaVA) |
| **LLaVA-OneVision** | LLaVA-OneVision: Easy Visual Task Transfer | arXiv | 2024/08 | [GitHub](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| **InternVL** | InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks | CVPR 2024 | 2023/12 | [GitHub](https://github.com/OpenGVLab/InternVL) |
| **InternVL2** | InternVL2: Better than the Best | arXiv | 2024 | [GitHub](https://github.com/OpenGVLab/InternVL) |
| **InternVL3** | InternVL3: Native Multimodal Pre-Training Paradigm | arXiv | 2025/04 | [GitHub](https://github.com/OpenGVLab/InternVL) |
| **Qwen-VL** | Qwen-VL: A Versatile Vision-Language Model | arXiv | 2023/08 | [GitHub](https://github.com/QwenLM/Qwen-VL) |
| **Qwen2-VL** | Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution | arXiv | 2024/09 | [GitHub](https://github.com/QwenLM/Qwen2-VL) |
| **Qwen2.5-VL** | Qwen2.5-VL Technical Report | arXiv | 2025/01 | [GitHub](https://github.com/QwenLM/Qwen2.5-VL) |
| **Seed1.5-VL** | Seed1.5-VL: A Powerful Vision-Language Foundation Model | arXiv | 2025 | [GitHub](https://github.com/ByteDance-Seed/Seed1.5-VL) |
| **MiMo-VL** | MiMo-VL Technical Report | arXiv | 2025/06 | [HuggingFace](https://huggingface.co/XiaomiMiMo/MiMo-VL-7B-RL) |

---

## 📅 Quick Index by Year

> Click a model name to find it in the tables below · ⭐ = landmark


### 2026 (1 models)

- ⭐ **Gemini 3.1 Pro** `2026/02` · _Omni Models_ · [GitHub](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)

### 2025 (47 models)

- ⭐ **Janus-Pro** `2025/01` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2501.17811)
- **MUSE-VL** `2025/01` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2501.06599)
- **MiniCPM-o 2.6** `2025/01` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2501.15481)
- **SALMONN-Omni** `2025/01` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2501.10801)
- **Spider** `2025/01` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2501.03461)
- **VA-VAE** `2025/01` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2501.01423) · [GitHub](https://github.com/hustvl/LightningDiT)
- **VITA-1.5** `2025/01` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2501.12599)
- **EQ-VAE** `2025/02` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2502.09509) · [GitHub](https://github.com/zelaki/eqvae)
- **FlexTok** `2025/02` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2502.13967)
- **Gemini 2.0 Flash** `2025/02` · _Omni Models_ · [GitHub](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/)
- **M2-omni** `2025/02` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2502.18778)
- **MAETok** `2025/02` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2502.03444) · [GitHub](https://github.com/Hhhhhhao/continuous_tokenizer)
- **QLIP** `2025/02` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2502.05178)
- ⭐ **Qwen2.5-VL** `2025/02` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2502.13923)
- **SigLIP 2** `2025/02` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2502.14786)
- **FAR** `2025/03` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2503.05305) · [GitHub](https://github.com/yuhuUSTC/FAR)
- **FlowMo** `2025/03` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2503.11056)
- ⭐ **Gemini 2.5 Pro** `2025/03` · _Omni Models_ · [GitHub](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/)
- **Harmon** `2025/03` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2503.07897)
- **HermesFlow** `2025/03` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2503.12580)
- **InteractiveOmni** `2025/03` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2503.17366)
- **NFIG** `2025/03` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2503.07076)
- ⭐ **Qwen2.5-Omni** `2025/03` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2503.20215)
- **USP** `2025/03` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2503.06132) · [GitHub](https://github.com/cxxgtxy/USP)
- **UniDisc** `2025/03` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2503.20853)
- **VARGPT-v1.1** `2025/03` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2503.16278)
- **InternVL3** `2025/04` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2504.10479)
- **InternVL3-Omni** `2025/04` · _Omni Models_ · [GitHub](https://github.com/OpenGVLab/InternVL)
- **MetaQuery-XL** `2025/04` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2504.13979)
- ⭐ **BAGEL** `2025/05` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2505.14683) · [GitHub](https://github.com/ByteDance-Seed/Bagel)
- **FUDOKI** `2025/05` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2505.05667)
- **MMaDA** `2025/05` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2505.15809) · [GitHub](https://github.com/Gen-Verse/MMaDA)
- **MiMo-VL** `2025/05` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2505.18411)
- ⭐ **Ming-Omni** `2025/05` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2505.02471)
- **Muddit** `2025/05` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2505.16965)
- **Seed1.5-VL** `2025/05` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2505.07062)
- **Selftok** `2025/05` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2505.19065)
- **TokLIP** `2025/05` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2505.05422)
- **BLIP3-o** `2025/06` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2506.12831)
- **NExT-OMNI** `2025/06` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2506.08838)
- ⭐ **OmniGen2** `2025/06` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2506.18871)
- **Qwen3-Omni** `2025/06` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2506.00513)
- ⭐ **Show-o2** `2025/06` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2506.15564)
- **Step3** `2025/06` · _Omni Models_ · [GitHub](https://stepfun.ai/research/en/step3)
- **InteractiveOmni-A2A** `2025/10` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2510.13747)
- **MiniCPM-o 4.5** `2025/11` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2511.07905)
- **OmniFlow** `2025/12` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2412.01169)

### 2024 (37 models)

- **CoDi-2** `2024/01` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2311.18775)
- **AnyGPT** `2024/02` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2402.12226)
- **EVA-CLIP** `2024/02` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2402.04252)
- ⭐ **Gemini 1.5 Pro** `2024/02` · _Omni Models_ · [GitHub](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/)
- **InternVL** `2024/02` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2312.14238)
- **LWM** `2024/02` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2402.08268) · [GitHub](https://github.com/LargeWorldModel/LWM)
- **UniCode** `2024/03` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2403.09072)
- **Unified-IO 2** `2024/03` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2312.17172)
- **V2L-Tokenizer** `2024/03` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2403.07874) · [GitHub](https://github.com/zh460045050/V2L-Tokenizer)
- ⭐ **VAR** `2024/04` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2404.02905) · [GitHub](https://github.com/FoundationVision/VAR)
- ⭐ **Chameleon** `2024/05` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2405.09818) · [GitHub](https://github.com/facebookresearch/chameleon)
- ⭐ **GPT-4o** `2024/05` · _Omni Models_ · [GitHub](https://openai.com/index/hello-gpt-4o/)
- **X-VILA** `2024/05` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2405.19335)
- **BSQ-ViT** `2024/06` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2406.07548) · [GitHub](https://github.com/zhaoyue-zephyrus/bsq-vit)
- **LlamaGen** `2024/06` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2406.06525) · [GitHub](https://github.com/FoundationVision/LlamaGen)
- ⭐ **TiTok** `2024/06` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2406.07550) · [GitHub](https://github.com/bytedance/1d-tokenizer)
- **ANOLE** `2024/07` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2407.06135)
- ⭐ **Show-o** `2024/08` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2408.12528) · [GitHub](https://github.com/showlab/Show-o)
- ⭐ **Transfusion** `2024/08` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2408.11039)
- **VITA** `2024/08` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2408.05505)
- ⭐ **Emu3** `2024/09` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2409.18858) · [GitHub](https://github.com/baaivision/Emu3)
- **LLaMA-Omni** `2024/09` · _Omni Models_ · [arXiv](https://arxiv.org/abs/2409.06666)
- **MIO** `2024/09` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2409.17692)
- **Open-MAGVIT2** `2024/09` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2409.04410) · [GitHub](https://github.com/TencentARC/SEED-Voken)
- **ElasticTok** `2024/10` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2410.08368)
- **ImageFolder** `2024/10` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2410.01756) · [GitHub](https://github.com/lxa9867/ImageFolder)
- **Janus** `2024/10` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2410.13848)
- **MAGVIT-v2** `2024/10` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2310.05737)
- **SimVQ** `2024/11` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2411.02038) · [GitHub](https://github.com/youngsheen/SimVQ)
- **Liquid** `2024/12` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2412.04332)
- **LlamaFusion** `2024/12` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2412.15188)
- **SoftVQ-VAE** `2024/12` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2412.10958) · [GitHub](https://github.com/Hhhhhhao/continuous_tokenizer)
- **SynerGen-VL** `2024/12` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2412.09604)
- **TokenFlow** `2024/12` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2412.03069) · [GitHub](https://github.com/ByteFlow-AI/TokenFlow)
- **ViLex** `2024/12` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2412.06774)
- **VidTok** `2024/12` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2412.13061) · [GitHub](https://github.com/microsoft/VidTok)
- **XQ-GAN** `2024/12` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2412.01762) · [GitHub](https://github.com/lxa9867/ImageFolder)

### 2023 (13 models)

- ⭐ **BLIP-2** `2023/01` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2301.12597)
- **LQAE** `2023/02` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2302.00902)
- **SigLIP** `2023/03` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2303.15343)
- ⭐ **LLaVA** `2023/04` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2304.08485)
- ⭐ **CoDi** `2023/05` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2305.11846)
- **SPAE** `2023/06` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2306.17842)
- **Emu** `2023/07` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2307.05222)
- **DreamLLM** `2023/09` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2309.11499)
- **FSQ** `2023/09` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2309.15505)
- **LaVIT** `2023/09` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2309.04596)
- ⭐ **NExT-GPT** `2023/09` · _Any-to-Any Multimodal_ · [arXiv](https://arxiv.org/abs/2309.05519)
- **SEED** `2023/10` · _Unified Understanding + Generation_ · [arXiv](https://arxiv.org/abs/2310.01218) · [GitHub](https://github.com/AILab-CVC/SEED)
- ⭐ **MAGVIT** `2023/12` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2212.05199)

### 2022 (7 models)

- **MaskGIT** `2022/02` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2202.04200)
- **OFA** `2022/02` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2202.03052)
- **RQ-VAE** `2022/03` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2203.01941)
- ⭐ **Flamingo** `2022/04` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2204.14198)
- **CoCa** `2022/05` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2205.01068)
- **i-Code** `2022/05` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2205.01818)
- **BEiT-3** `2022/08` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2208.10442)

### 2021 (4 models)

- ⭐ **CLIP** `2021/01` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2103.00020)
- **ALIGN** `2021/02` · _Pretraining Foundations_ · [arXiv](https://arxiv.org/abs/2102.05918)
- **ViT-VQGAN** `2021/10` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2110.04627)
- ⭐ **VQGAN** `2021/12` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/2012.09841) · [GitHub](https://github.com/CompVis/taming-transformers)

### 2019 (1 models)

- **VQ-VAE-2** `2019/06` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/1906.00446)

### 2017 (1 models)

- ⭐ **VQ-VAE** `2017/11` · _Image & Video Tokenizers_ · [arXiv](https://arxiv.org/abs/1711.00937)

---

---

## 📋 Tracked Model Tables by Category

> Data sourced from `scripts/data.py` · {total_timeline} models tracked · Interactive view at [timeline.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/timeline.html)

### Multimodal Pretraining Foundations

_No models in this category._

### Image & Video Tokenizers

_No models in this category._

### Unified Understanding + Generation (U+G)

_No models in this category._

### Any-to-Any Models

_No models in this category._

### Omni Models (Audio · Video · Image · Text)

_No models in this category._

---

## ⭐ Landmark Models Timeline (26 models)

> Landmark models are architecturally significant milestones.
> ⭐ = landmark · Interactive timeline: [timeline.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/timeline.html)

| Date | Model | Category | arXiv | GitHub |
|------|-------|----------|-------|--------|
| 2017/11 | **VQ-VAE** | Tokenizer | [1711.00937](https://arxiv.org/abs/1711.00937) | - |
| 2021/01 | **CLIP** | Pretraining | [2103.00020](https://arxiv.org/abs/2103.00020) | - |
| 2021/12 | **VQGAN** | Tokenizer | [2012.09841](https://arxiv.org/abs/2012.09841) | [GitHub](https://github.com/CompVis/taming-transformers) |
| 2022/04 | **Flamingo** | Pretraining | [2204.14198](https://arxiv.org/abs/2204.14198) | - |
| 2023/01 | **BLIP-2** | Pretraining | [2301.12597](https://arxiv.org/abs/2301.12597) | - |
| 2023/04 | **LLaVA** | Pretraining | [2304.08485](https://arxiv.org/abs/2304.08485) | - |
| 2023/05 | **CoDi** | Any2Any | [2305.11846](https://arxiv.org/abs/2305.11846) | - |
| 2023/09 | **NExT-GPT** | Any2Any | [2309.05519](https://arxiv.org/abs/2309.05519) | - |
| 2023/12 | **MAGVIT** | Tokenizer | [2212.05199](https://arxiv.org/abs/2212.05199) | - |
| 2024/02 | **Gemini 1.5 Pro** | Omni | - | [GitHub](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) |
| 2024/04 | **VAR** | Tokenizer | [2404.02905](https://arxiv.org/abs/2404.02905) | [GitHub](https://github.com/FoundationVision/VAR) |
| 2024/05 | **Chameleon** | Unified | [2405.09818](https://arxiv.org/abs/2405.09818) | [GitHub](https://github.com/facebookresearch/chameleon) |
| 2024/05 | **GPT-4o** | Omni | - | [GitHub](https://openai.com/index/hello-gpt-4o/) |
| 2024/06 | **TiTok** | Tokenizer | [2406.07550](https://arxiv.org/abs/2406.07550) | [GitHub](https://github.com/bytedance/1d-tokenizer) |
| 2024/08 | **Transfusion** | Unified | [2408.11039](https://arxiv.org/abs/2408.11039) | - |
| 2024/08 | **Show-o** | Unified | [2408.12528](https://arxiv.org/abs/2408.12528) | [GitHub](https://github.com/showlab/Show-o) |
| 2024/09 | **Emu3** | Unified | [2409.18858](https://arxiv.org/abs/2409.18858) | [GitHub](https://github.com/baaivision/Emu3) |
| 2025/01 | **Janus-Pro** | Unified | [2501.17811](https://arxiv.org/abs/2501.17811) | - |
| 2025/02 | **Qwen2.5-VL** | Pretraining | [2502.13923](https://arxiv.org/abs/2502.13923) | - |
| 2025/03 | **Qwen2.5-Omni** | Omni | [2503.20215](https://arxiv.org/abs/2503.20215) | - |
| 2025/03 | **Gemini 2.5 Pro** | Omni | - | [GitHub](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| 2025/05 | **BAGEL** | Unified | [2505.14683](https://arxiv.org/abs/2505.14683) | [GitHub](https://github.com/ByteDance-Seed/Bagel) |
| 2025/05 | **Ming-Omni** | Any2Any | [2505.02471](https://arxiv.org/abs/2505.02471) | - |
| 2025/06 | **Show-o2** | Unified | [2506.15564](https://arxiv.org/abs/2506.15564) | - |
| 2025/06 | **OmniGen2** | Unified | [2506.18871](https://arxiv.org/abs/2506.18871) | - |
| 2026/02 | **Gemini 3.1 Pro** | Omni | - | [GitHub](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/) |

---

## 📈 Growth Trend

| Year | New Models | Cumulative |
|------|-----------|------------|
| 2017 | +1 | 1 |
| 2019 | +1 | 2 |
| 2021 | +4 | 6 |
| 2022 | +7 | 13 |
| 2023 | +13 | 26 |
| 2024 | +37 | 63 |
| 2025 | +47 | 110 |
| 2026 | +1 | 111 |

> 🚀 **Key insight:** 2025 saw an explosion of unified multimodal models, with more than all previous years combined.

---

## 🏆 Performance Leaderboards

### Image Understanding (Unified Models Only)

| Model | Params | POPE↑ | MME-P↑ | MMBench↑ | SEED↑ | MMMU↑ | MM-Vet↑ | TextVQA↑ |
|-------|--------|-------|--------|----------|-------|-------|---------|----------|
| MetaQuery-XL | 7B | - | 1685.2 | 83.5 | 76.9 | 58.6 | **66.6** | - |
| VARGPT-v1.1 | 7B | 89.1 | 1684.1 | 81.0 | 76.0 | 48.5 | - | 82.0 |
| Janus-Pro | 7B | 87.4 | 1567.1 | 79.2 | 72.1 | 41.0 | 50.0 | - |
| ILLUME+ | 3B | 87.6 | 1414.0 | **80.8** | 73.3 | 44.3 | 40.3 | 69.9 |
| LlamaFusion | 8B | - | 1603.7 | - | - | 41.7 | - | - |
| MUSE-VL | 32B | - | 1581.6 | **81.8** | 71.0 | 50.1 | - | - |
| TokenFlow-XL | 14B | 87.8 | - | 76.8 | 72.6 | 43.2 | - | 62.3 |
| Janus-Pro | 1.5B | 86.2 | 1444.0 | 75.5 | 68.3 | 36.3 | 39.8 | - |
| VARGPT | 7B | 87.3 | 1488.8 | 67.6 | 67.9 | 36.4 | - | 54.1 |
| QLIP | 7B | 86.1 | 1498.3 | - | - | - | 33.3 | 55.2 |
| UniTok | 7B | 83.2 | 1448 | - | - | - | 33.9 | 51.6 |
| Emu3 | 8B | 85.2 | 1243.8 | 58.5 | 68.2 | 31.6 | - | 64.7 |
| Show-o | 1.3B | 84.5 | 1232.9 | - | - | 27.4 | - | - |
| Chameleon | 30B | - | 575.3 | 32.5 | 48.5 | 38.8 | - | - |

### Image Generation — GenEval (Overall Score ↑)

| Model | Params | Single | Two Obj | Count | Colors | Position | Color Attr | **Overall** |
|-------|--------|--------|---------|-------|--------|----------|-----------|------------|
| MetaQuery-XL | 7B | - | - | - | - | - | - | **0.80** |
| **Janus-Pro** | **7B** | **0.99** | **0.89** | **0.59** | **0.90** | **0.79** | **0.66** | **0.80** |
| ILLUME+ | 3B | 0.99 | 0.88 | 0.62 | 0.84 | 0.42 | 0.53 | **0.72** |
| HermesFlow | 1.3B | 0.98 | 0.84 | 0.66 | 0.82 | 0.32 | 0.52 | **0.69** |
| Show-o | 1.3B | 0.98 | 0.80 | 0.66 | 0.84 | 0.31 | 0.50 | **0.68** |
| DALL-E 3 | - | 0.96 | 0.87 | 0.47 | 0.83 | 0.43 | 0.45 | **0.67** |
| D-DiT | 2B | 0.97 | 0.80 | 0.54 | 0.76 | 0.32 | 0.50 | **0.65** |
| SD3 | 2B | 0.98 | 0.74 | 0.63 | 0.67 | 0.34 | 0.36 | **0.62** |
| Transfusion | - | - | - | - | - | - | - | **0.63** |
| JanusFlow | 1.3B | 0.97 | 0.59 | 0.45 | 0.83 | 0.53 | 0.42 | **0.63** |
| SDXL | 2.6B | 0.98 | 0.74 | 0.39 | 0.85 | 0.15 | 0.23 | **0.55** |
| Emu3-Gen | 8B | 0.98 | 0.71 | 0.34 | 0.81 | 0.17 | 0.21 | **0.54** |
| Chameleon | 34B | - | - | - | - | - | - | **0.39** |

### Image Generation Quality — MJHQ-30K FID (↓ is better)

| Model | Params | Resolution | **FID ↓** |
|-------|--------|-----------|----------|
| Playground v2.5 | - | - | **4.48** |
| Liquid | 7B | 512 | **5.47** |
| PixArt-α | 0.6B | - | 6.14 |
| ILLUME+ | 3B | - | 6.00 |
| MetaQuery-XL | 7B | - | 6.02 |
| SynerGen-VL | 2.4B | - | 6.10 |
| MUSE-VL | 7B | 256 | 7.73 |
| VILA-U | 7B | 384 | 7.69 |
| SD-XL | 2B | - | 9.55 |
| JanusFlow | 1.3B | - | 9.51 |
| Janus | 1.3B | - | 10.10 |
| Show-o | 1.3B | - | 15.18 |
| LWM | 7B | - | 17.77 |

---

## 📊 Benchmarks & Evaluation

### Understanding Benchmarks

| Benchmark | Task | Paper |
|-----------|------|-------|
| **POPE** | Hallucination / Object Existence Probing | [arXiv:2305.10355](https://arxiv.org/abs/2305.10355) |
| **MME** | Comprehensive Multimodal LLM Evaluation | [arXiv:2306.13394](https://arxiv.org/abs/2306.13394) |
| **MMBench** | All-around Multimodal Player Evaluation | [arXiv:2307.06281](https://arxiv.org/abs/2307.06281) |
| **SEED-Bench** | Generative Comprehension Benchmark | [arXiv:2307.16125](https://arxiv.org/abs/2307.16125) |
| **MMMU** | Massive Multi-Discipline Multimodal Reasoning | [arXiv:2311.16502](https://arxiv.org/abs/2311.16502) |
| **MM-Vet** | Integrated Multimodal Capabilities Evaluation | [arXiv:2308.02490](https://arxiv.org/abs/2308.02490) |
| **VQAv2** | Visual Question Answering v2 | [arXiv:1612.00837](https://arxiv.org/abs/1612.00837) |
| **GQA** | Real-World Visual Reasoning | [arXiv:1902.09506](https://arxiv.org/abs/1902.09506) |
| **TextVQA** | VQA on Text-in-Image | [arXiv:1904.08920](https://arxiv.org/abs/1904.08920) |
| **ChartQA** | Chart Understanding and Reasoning | [arXiv:2203.10244](https://arxiv.org/abs/2203.10244) |
| **MMStar** | Evaluating Large Vision-Language Models | [arXiv:2403.20330](https://arxiv.org/abs/2403.20330) |
| **MathVista** | Mathematical Reasoning in Visual Contexts | [arXiv:2310.02255](https://arxiv.org/abs/2310.02255) |
| **Video-MME** | Multi-modal LLMs in Video Analysis | [arXiv:2405.21075](https://arxiv.org/abs/2405.21075) |
| **General-Bench** | General-Purpose Multimodal Models | arXiv 2025/05 |

### Generation Benchmarks

| Benchmark | Task | Paper |
|-----------|------|-------|
| **GenEval** | Object-Focused Text-to-Image Alignment | [arXiv:2310.11513](https://arxiv.org/abs/2310.11513) |
| **MJHQ-30K** | Image Quality (FID-based) | - |
| **T2I-CompBench** | Compositional Text-to-Image Generation | [arXiv:2307.06350](https://arxiv.org/abs/2307.06350) |
| **T2I-CompBench++** | Enhanced Compositional T2I | arXiv 2025/03 |
| **DPG-Bench** | Dense Prompt Generation Quality | - |
| **DrawBench** | Photorealistic T2I Evaluation | NeurIPS 2022 |
| **PartiPrompts** | Content-Rich T2I Evaluation | arXiv |
| **MMIG-Bench** | Multi-Modal Image Generation Interpretability | arXiv 2025/05 |
| **WorldGenBench** | Reasoning-Driven T2I Generation | arXiv 2025/05 |
| **DreamBench++** | Human-Aligned Personalized Generation | arXiv 2025/03 |
| **VTBench** | Evaluating Visual Tokenizers for AR Generation | arXiv 2025/05 |
| **RealUnify** | Comprehensive Unified U+G Evaluation | arXiv |
| **KRIS-Bench** | Next-Generation Intelligent Image Editing | arXiv 2025/05 |
| **ImgEdit-Bench** | Unified Image Editing Benchmark | arXiv 2025/05 |
| **ByteMorph-Bench** | Non-Rigid Motion Image Editing | arXiv 2025/06 |
| **WISE** | World Knowledge Informative Semantic Evaluation | arXiv 2025/05 |

### Interleaved Generation Benchmarks

| Benchmark | Task | Paper |
|-----------|------|-------|
| **InterleavedBench** | Interleaved Image-Text Generation | arXiv |
| **ISG** | Interleaved Scene Generation | arXiv |
| **MMIE** | Massive Multimodal Interleaved Evaluation | arXiv |
| **UniBench / UniEval** | Holistic Unified Model Evaluation | arXiv 2025/05 |

### Omni / Audio-Video Benchmarks

| Benchmark | Task | Paper |
|-----------|------|-------|
| **OmniBench** | Universal Omni-Language Model Evaluation | [arXiv:2409.15272](https://arxiv.org/abs/2409.15272) |
| **OmniPlay** | Benchmarking Omni-Modal Models | [arXiv:2508.04361](https://arxiv.org/html/2508.04361v2) |
| **AIR-Bench** | Audio-Language Model Evaluation | arXiv |
| **EmbodiedBench** | Embodied Agents on Diverse Real-World Tasks | ICML 2025 |
| **MMSearch-R1** | LMMs with Search Capabilities | [arXiv:2506.20670](https://arxiv.org/abs/2506.20670) |

---

## 🗂️ Datasets

### Pretraining / Understanding Datasets

| Dataset | Scale | Type | Link |
|---------|-------|------|------|
| **LAION-5B** | 5.85B pairs | Image-Text | [HuggingFace](https://huggingface.co/datasets/laion/laion2B-en) |
| **LAION-Aesthetics** | ~600M | Image-Text (Aesthetic) | - |
| **COYO-700M** | 700M | Image-Text | [GitHub](https://github.com/kakaobrain/coyo-dataset) |
| **DataComp-1B** | 1B | CLIP Training | [arXiv:2304.14108](https://arxiv.org/abs/2304.14108) |
| **ShareGPT4V** | 1.2M | GPT-4V Captioned | [arXiv:2311.12793](https://arxiv.org/abs/2311.12793) |
| **LLaVA-Pretrain** | 595K | CC3M Filtered | [HuggingFace](https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain) |
| **ALLaVA-4V** | 1.4M | Instruction | - |
| **Infinity-MM** | 40M+ | Multi-Source | [arXiv:2410.18558](https://arxiv.org/abs/2410.18558) |
| **OmniCorpus** | 8.6B tokens | Omni-Modal | [arXiv:2406.08418](https://arxiv.org/abs/2406.08418) |
| **Honey-Data-15M** | 15M | Understanding | 2025/11 |
| **AudioSet** | 2M clips | Audio | [Paper](https://research.google.com/audioset/) |

### Text-to-Image Generation Datasets

| Dataset | Scale | Type | Link |
|---------|-------|------|------|
| **CC-12M** | 12M | Conceptual | [arXiv:2102.08981](https://arxiv.org/abs/2102.08981) |
| **JourneyDB** | 4M | Midjourney Prompts | [arXiv:2307.00716](https://arxiv.org/abs/2307.00716) |
| **MARIO-10M** | 10M | Visual Text | - |
| **FLUX-Reason-6M** | 6M | T2I Reasoning | 2025/09 |
| **Echo-4o-Image** | - | GPT-4o Synthesized | 2025/08 |
| **TextAtlas5M** | 5M | Dense Text Gen | 2025/02 |
| **BLIP3o-60k** | 60K | Curated Multimodal | 2025/05 |

### Image Editing Datasets

| Dataset | Scale | Type | Link |
|---------|-------|------|------|
| **InstructPix2Pix** | 313K | Instruction Edit | [GitHub](https://github.com/timothybrooks/instruct-pix2pix) |
| **MagicBrush** | 10K | Manual Annotation | [arXiv:2306.10012](https://arxiv.org/abs/2306.10012) |
| **ByteMorph-6M** | 6M | Non-Rigid Motion | 2025/06 |
| **ImgEdit** | 1.2M | Unified Editing | 2025/05 |
| **X2Edit** | 3.7M | Instruction-Driven | 2025/08 |
| **Pico-Banana-400K** | 400K | Text-Guided | 2025/10 |

### Interleaved Image-Text Datasets

| Dataset | Scale | Type | Link |
|---------|-------|------|------|
| **MMC4** | 103M images | Interleaved Web | [arXiv:2304.06939](https://arxiv.org/abs/2304.06939) |
| **OBELICS** | 141M images | Open Interleaved | [arXiv:2306.16527](https://arxiv.org/abs/2306.16527) |
| **CoMM** | - | Compositional | - |
| **ShareGPT-4o-Image** | - | GPT-4o Level | 2025/06 |
| **MetaQuery Instruct 2.4M** | 2.4M | Cross-Modal | 2025/06 |
| **Graph200K** | 200K | Visual ICL | 2025/03 |

---

## 🏗️ Repository Structure

```
Awesome-Native-Multimodal-Models/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD: validate → test → build → deploy
├── scripts/
│   ├── data.py                 # ★ Single source of truth (TAXONOMY_TREE + TIMELINE_MODELS)
│   ├── validate.py             # 17-rule validation engine
│   ├── generate_taxonomy.py    # D3.js collapsible tree → docs/taxonomy.html
│   ├── generate_timeline.py    # Swim-lane timeline → docs/timeline.html
│   ├── generate_index.py       # Landing page → docs/index.html
│   └── generate_report.py      # Quality dashboard → docs/validation_report.html
├── tests/
│   ├── test_data.py            # Unit tests for TAXONOMY_TREE & TIMELINE_MODELS
│   └── test_html_output.py     # Tests for generated HTML files
├── docs/                       # GitHub Pages output (auto-generated)
│   ├── index.html
│   ├── taxonomy.html
│   ├── timeline.html
│   ├── validation_report.html
│   └── validation.json
├── assets/
│   ├── taxonomy_tree.png       # Static taxonomy visualization
│   └── timeline.png            # Static timeline visualization
├── README.md                   # This file
├── requirements.txt
└── LICENSE
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Awesome-Native-Multimodal-Models.git
cd Awesome-Native-Multimodal-Models

# 2. Install dependencies
pip install -r requirements.txt

# 3. Validate data integrity (must pass 0 errors before any PR)
python scripts/validate.py
# → For strict mode (fail on warnings):
python scripts/validate.py --strict
# → Export JSON report:
python scripts/validate.py --json

# 4. Generate interactive HTML visualizations
python scripts/generate_taxonomy.py    # → docs/taxonomy.html
python scripts/generate_timeline.py   # → docs/timeline.html
python scripts/generate_index.py      # → docs/index.html
python scripts/generate_report.py     # → docs/validation_report.html

# 5. Run unit tests
python -m pytest tests/ -v

# 6. Open visualizations locally
open docs/taxonomy.html     # macOS
# xdg-open docs/taxonomy.html  # Linux
# start docs/taxonomy.html     # Windows
```

---

## ➕ How to Add a Model

All data lives in **`scripts/data.py`**. To add a new model:

### Step 1 — Add to `TIMELINE_MODELS`

```python
{
    "name": "YourModel",
    "year": 2025,
    "month": 6,
    "category": "Unified U+G",       # One of: Image & Video Tokenizers, Unified U+G,
                                      #         Any-to-Any, Omni Models, Pretraining Foundations
    "arxiv": "2506.XXXXX",            # arXiv ID (YYMM.NNNNN format)
    "github": "https://github.com/...",
    "desc": "One concise sentence describing what makes this model novel.",
    "landmark": False,                # True only for architecturally significant milestones
},
```

### Step 2 — Add to `TAXONOMY_TREE`

Navigate to the appropriate branch and add a leaf node:

```python
{
    "name": "YourModel",
    "year": 2025,
    "arxiv": "2506.XXXXX",
    "github": "https://github.com/...",
    "desc": "...",
    "landmark": False,
},
```

### Step 3 — Validate

```bash
python scripts/validate.py
# Must show: Errors: 0
```

### Step 4 — Submit PR

Open a Pull Request with:
- [ ] Model added to both `TIMELINE_MODELS` and `TAXONOMY_TREE`
- [ ] arXiv ID in correct format (`YYMM.NNNNN`)
- [ ] One-sentence description in `desc`
- [ ] `python scripts/validate.py` → 0 errors
- [ ] Brief PR description of the model's significance

---

## 🔬 Validation Rules

| Rule ID | Severity | Description |
|---------|----------|-------------|
| TL-001 | ERROR | Timeline model missing required `name` field |
| TL-002 | ERROR | Timeline model missing required `year` field |
| TL-003 | ERROR | Timeline model missing required `category` field |
| TL-004 | ERROR | `year` must be an integer |
| TL-005 | ERROR | `year` must be between 2010 and 2030 |
| TL-006 | ERROR | `category` must be one of the 5 defined categories |
| TL-007 | WARNING | arXiv ID format should be `YYMM.NNNNN` |
| TL-008 | WARNING | `desc` field is empty — please add a one-sentence description |
| TL-009 | WARNING | No arXiv ID and no GitHub URL — model has no reference |
| TL-010 | WARNING | GitHub URL should be HTTPS |
| TL-011 | WARNING | arXiv year does not match model year |
| TL-012 | INFO | arXiv present but GitHub URL missing |
| TX-001 | ERROR | Duplicate leaf name in taxonomy tree |
| TX-002 | ERROR | Duplicate arXiv ID in taxonomy tree |
| TX-003 | ERROR | Model name appears in multiple sub-categories |
| CV-001 | WARNING | Model in timeline but not in taxonomy |
| CV-002 | WARNING | Model in taxonomy but not in timeline |

> 🎯 **Quality Score Interpretation:**
> - 90–100: Excellent (all descriptions + GitHub links filled)
> - 70–89: Good (minor gaps)
> - 40–69: Fair (some models lack descriptions or references)
> - 0–39: Critical (significant data quality issues)

**Usage:**
```bash
python scripts/validate.py              # Standard (fails on errors only)
python scripts/validate.py --strict     # Fails on warnings too
python scripts/validate.py --json       # Write docs/validation.json
```

Live validation dashboard: [validation_report.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/validation_report.html)

---

## ⚙️ GitHub Actions CI/CD

The pipeline runs automatically on every push, PR, and weekly schedule.

```yaml
Triggers:
  push:        main branch, when scripts/** or tests/** change
  pull_request: validate + build only (no deploy)
  schedule:    Every Monday 08:00 UTC
  workflow_dispatch: Manual trigger (optional --strict mode)

Pipeline (4 stages):
  1. validate-data  → python scripts/validate.py  (must pass: 0 errors)
  2. unit-tests     → pytest tests/ -v
  3. build          → generate 5 HTML files + validation.json
  4. deploy         → push docs/ to gh-pages branch → GitHub Pages
```

**Artifacts produced:** `taxonomy.html`, `timeline.html`, `validation_report.html`, `index.html`, `validation.json`

---

## 📌 Related Awesome Lists

| Repository | Description |
|-----------|-------------|
| [BradyFU/Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) | The most comprehensive MLLM awesome list |
| [AIDC-AI/Awesome-Unified-Multimodal-Models](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) | Unified understanding+generation models with survey |
| [John-Ge/Awesome-Native-Multimodal-Models](https://github.com/John-Ge/Awesome-Native-Multimodal-Models) | Native models for vision-language with benchmark tables |
| [friedrichor/Awesome-Multimodal-Papers](https://github.com/friedrichor/Awesome-Multimodal-Papers) | General multimodal papers list |
| [showlab/Awesome-MLLM-Hallucination](https://github.com/showlab/Awesome-MLLM-Hallucination) | Hallucination in MLLMs |
| [zli12321/Vision-Language-Models-Overview](https://github.com/zli12321/Vision-Language-Models-Overview) | VLMs overview including Qwen, InternVL |
| [Kwai-YuanQi/MM-RLHF](https://github.com/Kwai-YuanQi/MM-RLHF) | Multimodal RLHF alignment dataset & methods |

---

## 🤝 Contributing

We warmly welcome contributions! Please follow these steps:

1. **Fork** this repository
2. **Add your entry** following the existing table format:
   ```markdown
   | **ModelName** | Full paper title | Venue | YYYY/MM | [GitHub](url) | [Demo](url) |
   ```
3. Make sure to include all available links (paper, code, demo)
4. Submit a **Pull Request** with a brief description

**Contribution Guidelines:**
- Keep entries sorted by date (newest first within each section)
- Verify all links are working before submitting
- For new sections, open an Issue first to discuss
- All data changes must go through `scripts/data.py` (single source of truth)

### 💡 Pro Tips for Contributors

> **Finding missing models:** Check [Papers With Code — Image Generation](https://paperswithcode.com/task/image-generation) and [Hugging Face papers](https://huggingface.co/papers) for recent releases not yet listed.

> **Setting `landmark: True`:** Use this sparingly — only for models that introduced a genuinely new architectural paradigm (e.g., first discrete AR unified model, first hybrid AR+Diffusion). Currently ~30% of models; target is ~15%.

> **Category selection guide:**
> - `Tokenizer` → model's primary contribution is the visual tokenizer itself
> - `Unified` → model does image understanding **and** generation (no audio)
> - `Any2Any` → model handles 3+ modalities including audio/video
> - `Omni` → real-time/streaming omni-modal interaction
> - `Pretraining` → contribution is the pretraining recipe/backbone

---

## 📜 Citation

If you find this list useful in your research, please consider starring ⭐ the repository and citing relevant works.

```bibtex
@misc{awesome-native-multimodal-models,
  title  = {Awesome Native Multimodal Models},
  author = {Your Name},
  year   = {2026},
  url    = {https://github.com/your-username/Awesome-Native-Multimodal-Models}
}
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>
    ⭐ Star this repo if you find it helpful! | Last updated: March 2026 | 400+ papers covered<br/>
    Data sourced from <code>scripts/data.py</code> · Visualized with D3.js v7 & Chart.js v4<br/>
    Auto-generated by CI/CD pipeline · 111 models · 111 taxonomy leaves · 26 landmarks
  </sub>
</div>
