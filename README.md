# Awesome Native Multimodal Models

[![Papers](https://img.shields.io/badge/papers-400%2B-blue?style=flat-square)](https://arxiv.org)
[![Last Updated](https://img.shields.io/badge/updated-2026--03-green?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-orange?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)]()
[![Pages Build](https://github.com/your-username/Awesome-Native-Multimodal-Models/actions/workflows/deploy.yml/badge.svg)](https://github.com/your-username/Awesome-Native-Multimodal-Models/actions)

> **Native Multimodal** = shared computation paths + unified tokenization + end-to-end cross-modal training  
> (vs. modular adapters like LLaVA / InstructBLIP)

---

## 🌐 Interactive Visualizations

> Auto-generated and deployed to GitHub Pages on every push via [GitHub Actions](.github/workflows/deploy.yml).

| Visualization | Link | Description |
|---|---|---|
| 🌐 Architecture Taxonomy | [taxonomy.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/taxonomy.html) | D3.js collapsible tree: 5 branches, 12+ sub-categories, 100+ models |
| 📅 Model Timeline | [timeline.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/timeline.html) | Swim-lane timeline 2017–2026, 5 lanes, 100 models |
| 🏠 Landing Page | [index.html](https://your-username.github.io/Awesome-Native-Multimodal-Models/) | Overview + stats |

---

## 📁 Repository Structure

```
Awesome-Native-Multimodal-Models/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD: validate → build → deploy
├── scripts/
│   ├── data.py                 # 📦 All model data (single source of truth)
│   ├── generate_taxonomy.py    # 🌐 Builds docs/taxonomy.html
│   ├── generate_timeline.py    # 📅 Builds docs/timeline.html
│   └── generate_index.py       # 🏠 Builds docs/index.html
├── tests/
│   ├── test_data.py            # ✅ Validates data.py structure
│   └── test_html_output.py     # ✅ Validates generated HTML
├── docs/                       # 📤 GitHub Pages output (auto-generated)
│   ├── index.html
│   ├── taxonomy.html
│   └── timeline.html
├── assets/
│   ├── taxonomy_tree.png       # Static PNG fallback
│   └── timeline.png
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/your-username/Awesome-Native-Multimodal-Models.git
cd Awesome-Native-Multimodal-Models

# Install dependencies (stdlib only, no heavy deps)
pip install -r requirements.txt

# Run all generators
python scripts/generate_index.py
python scripts/generate_taxonomy.py
python scripts/generate_timeline.py

# Open in browser
open docs/index.html
```

---

## 🤖 GitHub Actions CI/CD

The workflow (`.github/workflows/deploy.yml`) runs on:
- **Push to `main`** when `scripts/**` changes
- **Weekly schedule** (Monday 08:00 UTC)
- **Manual trigger** (workflow_dispatch)

**Steps:**
1. `validate` — runs `tests/test_data.py` to check data integrity
2. `build` — generates all 3 HTML files, runs `tests/test_html_output.py`
3. `deploy` — pushes `docs/` to `gh-pages` branch via `peaceiris/actions-gh-pages`

### Setting up GitHub Pages

1. Go to **Settings → Pages**
2. Set Source: **Deploy from branch** → `gh-pages` → `/ (root)`
3. Save — your site will be live at `https://your-username.github.io/Awesome-Native-Multimodal-Models/`

---

## ➕ Adding a New Model

Edit `scripts/data.py` — there are **two places** to update:

### 1. Taxonomy Tree (`TAXONOMY_TREE`)
Find the right sub-category and add a leaf node:
```python
{"name": "YourModel", "year": 2025, "arxiv": "2501.XXXXX", "github": "https://github.com/..."},
```

### 2. Timeline (`TIMELINE_MODELS`)
Add a flat entry:
```python
{
    "name": "YourModel",
    "year": 2025, "month": 6,
    "category": "Unified",          # Pretraining | Tokenizer | Unified | Any2Any | Omni
    "arxiv": "2501.XXXXX",
    "github": "https://github.com/...",
    "landmark": False,              # True for breakthrough papers
    "desc": "One-line description",
},
```

Then commit & push — GitHub Actions will rebuild and redeploy automatically! 🎉

---

## 📊 Taxonomy Overview

```
Native Multimodal Models
├── Image & Video Tokenizers
│   ├── Discrete VQ (VQ-VAE, VQGAN, TiTok, LlamaGen…)
│   ├── Residual VQ / RQ (RQ-VAE, VAR, NFIG…)
│   ├── FSQ (FSQ, ElasticTok, VidTok, FlexTok…)
│   ├── LFQ (MAGVIT-v2, Open-MAGVIT2, FlowMo…)
│   ├── BSQ / PQ (BSQ-ViT, QLIP, ImageFolder…)
│   ├── Continuous VAE (VA-VAE, EQ-VAE, MAETok, FAR…)
│   └── Text-Aligned (LQAE, SPAE, V2L-Tokenizer…)
├── Unified U+G
│   ├── Diffusion-Based (UniDisc, MMaDA, Muddit…)
│   ├── AR Pixel-Encoding (Chameleon, Emu3, LWM, Liquid…)
│   ├── AR Semantic (SEED, LaVIT, Janus-Pro, BAGEL…)
│   └── Hybrid AR+Diff (Transfusion, Show-o/o2, LlamaFusion…)
├── Any-to-Any
│   ├── Discrete AR (NExT-GPT, AnyGPT, MIO, Ming-Omni…)
│   ├── Composable Diffusion (CoDi, CoDi-2, OmniFlow…)
│   └── Omni-AR Full-Modal (Unified-IO 2, X-VILA, M2-omni…)
├── Omni Models
│   ├── Proprietary (GPT-4o, Gemini 2.5/3.1 Pro…)
│   ├── Open-Source (Qwen2.5-Omni, VITA, MiniCPM-o…)
│   └── Speech-First (LLaMA-Omni, SALMONN-Omni…)
└── Pretraining Foundations
    ├── Contrastive (CLIP, ALIGN, SigLIP, EVA-CLIP…)
    ├── Generative (BLIP-2, BEiT-3, OFA, Flamingo…)
    └── VL Instruction (LLaVA, InternVL, Qwen2.5-VL…)
```

---

## 📜 License

[MIT License](LICENSE) — feel free to use, share, and contribute!
