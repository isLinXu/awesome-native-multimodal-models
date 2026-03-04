"""
data.py — Shared model data for Awesome-Native-Multimodal-Models visualizations.
All model records, taxonomy tree, and benchmark data live here.
"""

# ─────────────────────────────────────────────────────────────────────────────
# TAXONOMY TREE  (hierarchical dict consumed by generate_taxonomy.py)
# ─────────────────────────────────────────────────────────────────────────────
TAXONOMY_TREE = {
    "name": "Native Multimodal Models",
    "description": "Models with unified tokenization & end-to-end cross-modal training",
    "children": [
        {
            "name": "Image & Video Tokenizers",
            "color": "#4ECDC4",
            "description": "Discrete and continuous visual tokenization methods",
            "children": [
                {
                    "name": "Discrete VQ",
                    "color": "#45B7D1",
                    "description": "Vector-Quantized tokenizers",
                    "children": [
                        {"name": "VQ-VAE", "year": 2017, "arxiv": "1711.00937", "github": ""},
                        {"name": "VQ-VAE-2", "year": 2019, "arxiv": "1906.00446", "github": ""},
                        {"name": "VQGAN", "year": 2021, "arxiv": "2012.09841", "github": "https://github.com/CompVis/taming-transformers"},
                        {"name": "ViT-VQGAN", "year": 2022, "arxiv": "2110.04627", "github": ""},
                        {"name": "MaskGIT", "year": 2022, "arxiv": "2202.04200", "github": ""},
                        {"name": "MAGVIT", "year": 2023, "arxiv": "2212.05199", "github": "https://github.com/google-research/magvit"},
                        {"name": "TiTok", "year": 2024, "arxiv": "2406.07550", "github": "https://github.com/bytedance/1d-tokenizer"},
                        {"name": "UniCode", "year": 2024, "arxiv": "2403.09072", "github": ""},
                        {"name": "LlamaGen", "year": 2024, "arxiv": "2406.06525", "github": "https://github.com/FoundationVision/LlamaGen"},
                        {"name": "TokenFlow", "year": 2024, "arxiv": "2412.03069", "github": "https://github.com/ByteFlow-AI/TokenFlow"},
                        {"name": "SimVQ", "year": 2024, "arxiv": "2411.02038", "github": "https://github.com/youngsheen/SimVQ"},
                        {"name": "SoftVQ-VAE", "year": 2024, "arxiv": "2412.10958", "github": ""},
                    ],
                },
                {
                    "name": "Residual VQ (RQ)",
                    "color": "#96CEB4",
                    "description": "Residual quantization tokenizers",
                    "children": [
                        {"name": "RQ-VAE", "year": 2022, "arxiv": "2203.01941", "github": "https://github.com/kakaobrain/rq-vae-transformer"},
                        {"name": "VAR", "year": 2024, "arxiv": "2404.02905", "github": "https://github.com/FoundationVision/VAR"},
                        {"name": "NFIG", "year": 2025, "arxiv": "2503.07076", "github": ""},
                    ],
                },
                {
                    "name": "FSQ",
                    "color": "#FFEAA7",
                    "description": "Finite Scalar Quantization",
                    "children": [
                        {"name": "FSQ", "year": 2023, "arxiv": "2309.15505", "github": ""},
                        {"name": "ElasticTok", "year": 2024, "arxiv": "2410.08368", "github": "https://github.com/LargeWorldModel/ElasticTok"},
                        {"name": "VidTok", "year": 2024, "arxiv": "2412.13061", "github": "https://github.com/microsoft/VidTok"},
                        {"name": "FlexTok", "year": 2025, "arxiv": "2502.13967", "github": ""},
                    ],
                },
                {
                    "name": "LFQ",
                    "color": "#DDA0DD",
                    "description": "Lookup-Free Quantization",
                    "children": [
                        {"name": "MAGVIT-v2", "year": 2024, "arxiv": "2310.05737", "github": ""},
                        {"name": "Open-MAGVIT2", "year": 2024, "arxiv": "2409.04410", "github": ""},
                        {"name": "FlowMo", "year": 2025, "arxiv": "2503.11056", "github": "https://github.com/kylesargent/flowmo"},
                    ],
                },
                {
                    "name": "BSQ / PQ",
                    "color": "#F0A500",
                    "description": "Binary/Product Quantization",
                    "children": [
                        {"name": "BSQ-ViT", "year": 2024, "arxiv": "2406.07548", "github": "https://github.com/zhaoyue-zephyrus/bsq-vit"},
                        {"name": "QLIP", "year": 2025, "arxiv": "2502.05178", "github": "https://github.com/NVlabs/QLIP"},
                        {"name": "ImageFolder", "year": 2024, "arxiv": "2410.01756", "github": "https://github.com/lxa9867/ImageFolder"},
                        {"name": "XQ-GAN", "year": 2024, "arxiv": "2412.01762", "github": ""},
                    ],
                },
                {
                    "name": "Continuous VAE",
                    "color": "#74B9FF",
                    "description": "Continuous latent space tokenizers",
                    "children": [
                        {"name": "VA-VAE", "year": 2025, "arxiv": "2501.01423", "github": "https://github.com/hustvl/LightningDiT"},
                        {"name": "EQ-VAE", "year": 2025, "arxiv": "2502.09509", "github": "https://github.com/zelaki/eqvae"},
                        {"name": "MAETok", "year": 2025, "arxiv": "2502.03444", "github": ""},
                        {"name": "FAR", "year": 2025, "arxiv": "2503.05305", "github": ""},
                        {"name": "USP", "year": 2025, "arxiv": "2503.06132", "github": ""},
                    ],
                },
                {
                    "name": "Text-Aligned",
                    "color": "#A29BFE",
                    "description": "Language-aligned visual tokenizers",
                    "children": [
                        {"name": "LQAE", "year": 2023, "arxiv": "2302.00902", "github": ""},
                        {"name": "SPAE", "year": 2023, "arxiv": "2306.17842", "github": ""},
                        {"name": "V2L-Tokenizer", "year": 2024, "arxiv": "2403.07874", "github": "https://github.com/zh460045050/V2L-Tokenizer"},
                        {"name": "ViLex", "year": 2024, "arxiv": "2412.06774", "github": ""},
                    ],
                },
            ],
        },
        {
            "name": "Unified U+G",
            "color": "#FF6B6B",
            "description": "Unified Understanding + Generation models",
            "children": [
                {
                    "name": "Diffusion-Based",
                    "color": "#FF8E8E",
                    "description": "Diffusion-based unified models",
                    "children": [
                        {"name": "UniDisc", "year": 2025, "arxiv": "2503.20853", "github": "https://github.com/alexanderswerdlow/unidisc"},
                        {"name": "MMaDA", "year": 2025, "arxiv": "2505.15809", "github": "https://github.com/Gen-Verse/MMaDA"},
                        {"name": "Muddit", "year": 2025, "arxiv": "2505.16965", "github": "https://github.com/M-E-AGI-Lab/Muddit"},
                        {"name": "FUDOKI", "year": 2025, "arxiv": "2505.05667", "github": ""},
                    ],
                },
                {
                    "name": "AR Pixel-Encoding",
                    "color": "#FFB3B3",
                    "description": "Autoregressive pixel-level models",
                    "children": [
                        {"name": "LWM", "year": 2024, "arxiv": "2402.08268", "github": "https://github.com/LargeWorldModel/LWM"},
                        {"name": "Chameleon", "year": 2024, "arxiv": "2405.09818", "github": "https://github.com/facebookresearch/chameleon"},
                        {"name": "ANOLE", "year": 2024, "arxiv": "2407.06135", "github": "https://github.com/GAIR-NLP/anole"},
                        {"name": "Emu3", "year": 2024, "arxiv": "2409.18858", "github": "https://github.com/baaivision/Emu3"},
                        {"name": "Liquid", "year": 2024, "arxiv": "2412.04332", "github": "https://github.com/FoundationVision/Liquid"},
                        {"name": "SynerGen-VL", "year": 2024, "arxiv": "2412.09604", "github": ""},
                        {"name": "Selftok", "year": 2025, "arxiv": "2505.19065", "github": ""},
                        {"name": "TokLIP", "year": 2025, "arxiv": "2505.05422", "github": "https://github.com/TencentARC/TokLIP"},
                        {"name": "Harmon", "year": 2025, "arxiv": "2503.07897", "github": "https://github.com/wusize/Harmon"},
                    ],
                },
                {
                    "name": "AR Semantic",
                    "color": "#FFC8C8",
                    "description": "Semantic-level autoregressive models",
                    "children": [
                        {"name": "SEED", "year": 2023, "arxiv": "2310.01218", "github": "https://github.com/AILab-CVC/SEED"},
                        {"name": "LaVIT", "year": 2023, "arxiv": "2309.04596", "github": "https://github.com/jy0205/LaVIT"},
                        {"name": "Emu", "year": 2023, "arxiv": "2307.05222", "github": ""},
                        {"name": "DreamLLM", "year": 2024, "arxiv": "2309.11499", "github": ""},
                        {"name": "Janus", "year": 2024, "arxiv": "2410.13848", "github": "https://github.com/deepseek-ai/Janus"},
                        {"name": "Janus-Pro", "year": 2025, "arxiv": "2501.17811", "github": "https://github.com/deepseek-ai/Janus"},
                        {"name": "OmniGen2", "year": 2025, "arxiv": "2506.18871", "github": ""},
                        {"name": "MUSE-VL", "year": 2025, "arxiv": "2501.06599", "github": ""},
                        {"name": "MetaQuery-XL", "year": 2025, "arxiv": "2504.13979", "github": ""},
                        {"name": "VARGPT-v1.1", "year": 2025, "arxiv": "2503.16278", "github": ""},
                    ],
                },
                {
                    "name": "Hybrid AR+Diff",
                    "color": "#FFD9D9",
                    "description": "Hybrid autoregressive + diffusion models",
                    "children": [
                        {"name": "Transfusion", "year": 2024, "arxiv": "2408.11039", "github": ""},
                        {"name": "Show-o", "year": 2024, "arxiv": "2408.12528", "github": "https://github.com/showlab/Show-o"},
                        {"name": "LlamaFusion", "year": 2024, "arxiv": "2412.15188", "github": ""},
                        {"name": "BAGEL", "year": 2025, "arxiv": "2505.14683", "github": "https://github.com/ByteDance-Seed/Bagel"},
                        {"name": "BLIP3-o", "year": 2025, "arxiv": "2506.12831", "github": ""},
                        {"name": "Show-o2", "year": 2025, "arxiv": "2506.15564", "github": "https://github.com/showlab/Show-o"},
                        {"name": "HermesFlow", "year": 2025, "arxiv": "2503.12580", "github": ""},
                    ],
                },
            ],
        },
        {
            "name": "Any-to-Any",
            "color": "#A8E6CF",
            "description": "Full cross-modal generation models",
            "children": [
                {
                    "name": "Discrete AR",
                    "color": "#C8F5E2",
                    "description": "Discrete autoregressive any-to-any",
                    "children": [
                        {"name": "NExT-GPT", "year": 2023, "arxiv": "2309.05519", "github": ""},
                        {"name": "AnyGPT", "year": 2024, "arxiv": "2402.12226", "github": ""},
                        {"name": "MIO", "year": 2024, "arxiv": "2409.17692", "github": ""},
                        {"name": "Spider", "year": 2025, "arxiv": "2501.03461", "github": ""},
                        {"name": "Ming-Omni", "year": 2025, "arxiv": "2505.02471", "github": ""},
                        {"name": "Qwen3-Omni", "year": 2025, "arxiv": "2506.00513", "github": ""},
                    ],
                },
                {
                    "name": "Composable Diffusion",
                    "color": "#D5FAF0",
                    "description": "Composable diffusion any-to-any",
                    "children": [
                        {"name": "CoDi", "year": 2023, "arxiv": "2305.11846", "github": ""},
                        {"name": "CoDi-2", "year": 2024, "arxiv": "2311.18775", "github": ""},
                        {"name": "OmniFlow", "year": 2025, "arxiv": "2412.01169", "github": ""},
                    ],
                },
                {
                    "name": "Omni-AR Full-Modal",
                    "color": "#E8FFF8",
                    "description": "Full-modal omni autoregressive",
                    "children": [
                        {"name": "Unified-IO 2", "year": 2024, "arxiv": "2312.17172", "github": ""},
                        {"name": "X-VILA", "year": 2024, "arxiv": "2405.19335", "github": ""},
                        {"name": "M2-omni", "year": 2025, "arxiv": "2502.18778", "github": ""},
                        {"name": "InteractiveOmni", "year": 2025, "arxiv": "2503.17366", "github": ""},
                    ],
                },
            ],
        },
        {
            "name": "Omni Models",
            "color": "#DDA0DD",
            "description": "Audio + Video + Image + Text unified models",
            "children": [
                {
                    "name": "Proprietary",
                    "color": "#E8C5E8",
                    "description": "Commercial omni models",
                    "children": [
                        {"name": "GPT-4o", "year": 2024, "arxiv": "", "github": ""},
                        {"name": "Gemini 1.5 Pro", "year": 2024, "arxiv": "", "github": ""},
                        {"name": "Gemini 2.0 Flash", "year": 2025, "arxiv": "", "github": ""},
                        {"name": "Gemini 2.5 Pro", "year": 2025, "arxiv": "", "github": ""},
                        {"name": "Gemini 3.1 Pro", "year": 2026, "arxiv": "", "github": ""},
                    ],
                },
                {
                    "name": "Open-Source",
                    "color": "#F0D5F0",
                    "description": "Open-source omni models",
                    "children": [
                        {"name": "VITA", "year": 2024, "arxiv": "2408.05505", "github": ""},
                        {"name": "VITA-1.5", "year": 2025, "arxiv": "2501.12599", "github": ""},
                        {"name": "MiniCPM-o 2.6", "year": 2025, "arxiv": "2501.15481", "github": "https://github.com/OpenBMB/MiniCPM-o"},
                        {"name": "MiniCPM-o 4.5", "year": 2025, "arxiv": "2511.07905", "github": "https://github.com/OpenBMB/MiniCPM-o"},
                        {"name": "Qwen2.5-Omni", "year": 2025, "arxiv": "2503.20215", "github": ""},
                        {"name": "InternVL3", "year": 2025, "arxiv": "2504.10479", "github": ""},
                        {"name": "Seed1.5-VL", "year": 2025, "arxiv": "2505.07062", "github": ""},
                        {"name": "NExT-OMNI", "year": 2025, "arxiv": "2506.08838", "github": ""},
                    ],
                },
                {
                    "name": "Speech-First",
                    "color": "#F8E8F8",
                    "description": "Speech-centric omni models",
                    "children": [
                        {"name": "LLaMA-Omni", "year": 2024, "arxiv": "2409.06666", "github": ""},
                        {"name": "SALMONN-Omni", "year": 2025, "arxiv": "2501.10801", "github": ""},
                        {"name": "InteractiveOmni", "year": 2025, "arxiv": "2503.17366", "github": ""},
                    ],
                },
            ],
        },
        {
            "name": "Pretraining Foundations",
            "color": "#FAD7A0",
            "description": "Foundation models for multimodal pretraining",
            "children": [
                {
                    "name": "Contrastive",
                    "color": "#FDE8C8",
                    "description": "Contrastive learning foundations",
                    "children": [
                        {"name": "CLIP", "year": 2021, "arxiv": "2103.00020", "github": ""},
                        {"name": "ALIGN", "year": 2021, "arxiv": "2102.05918", "github": ""},
                        {"name": "SigLIP", "year": 2023, "arxiv": "2303.15343", "github": ""},
                        {"name": "EVA-CLIP", "year": 2024, "arxiv": "2402.04252", "github": ""},
                        {"name": "SigLIP 2", "year": 2025, "arxiv": "2502.14786", "github": ""},
                    ],
                },
                {
                    "name": "Generative",
                    "color": "#FEF0DC",
                    "description": "Generative pretraining models",
                    "children": [
                        {"name": "BLIP-2", "year": 2023, "arxiv": "2301.12597", "github": ""},
                        {"name": "BEiT-3", "year": 2023, "arxiv": "2208.10442", "github": ""},
                        {"name": "OFA", "year": 2022, "arxiv": "2202.03052", "github": ""},
                        {"name": "Flamingo", "year": 2022, "arxiv": "2204.14198", "github": ""},
                        {"name": "i-Code", "year": 2023, "arxiv": "2205.01818", "github": ""},
                        {"name": "CoCa", "year": 2022, "arxiv": "2205.01068", "github": ""},
                    ],
                },
                {
                    "name": "VL Instruction",
                    "color": "#FFF4E8",
                    "description": "Vision-Language instruction tuning",
                    "children": [
                        {"name": "LLaVA", "year": 2023, "arxiv": "2304.08485", "github": ""},
                        {"name": "InternVL", "year": 2024, "arxiv": "2312.14238", "github": ""},
                        {"name": "Qwen2.5-VL", "year": 2025, "arxiv": "2502.13923", "github": ""},
                        {"name": "MiMo-VL", "year": 2025, "arxiv": "2505.18411", "github": ""},
                    ],
                },
            ],
        },
    ],
}


# ─────────────────────────────────────────────────────────────────────────────
# TIMELINE DATA  (flat list consumed by generate_timeline.py)
# ─────────────────────────────────────────────────────────────────────────────
TIMELINE_MODELS = [
    # Pre-training Foundations
    {"name": "CLIP",         "year": 2021, "month": 1,  "category": "Pretraining", "arxiv": "2103.00020", "landmark": True,  "desc": "Contrastive Language-Image Pretraining (OpenAI)"},
    {"name": "ALIGN",        "year": 2021, "month": 2,  "category": "Pretraining", "arxiv": "2102.05918", "landmark": False, "desc": "Large-scale alignment using noisy data (Google)"},
    {"name": "OFA",          "year": 2022, "month": 2,  "category": "Pretraining", "arxiv": "2202.03052", "landmark": False, "desc": "Unified sequence-to-sequence pretraining"},
    {"name": "Flamingo",     "year": 2022, "month": 4,  "category": "Pretraining", "arxiv": "2204.14198", "landmark": True,  "desc": "Few-shot visual language model (DeepMind)"},
    {"name": "CoCa",         "year": 2022, "month": 5,  "category": "Pretraining", "arxiv": "2205.01068", "landmark": False, "desc": "Contrastive captioners"},
    {"name": "BEiT-3",       "year": 2022, "month": 8,  "category": "Pretraining", "arxiv": "2208.10442", "landmark": False, "desc": "Multimodal foundation model via masked data modeling"},
    {"name": "BLIP-2",       "year": 2023, "month": 1,  "category": "Pretraining", "arxiv": "2301.12597", "landmark": True,  "desc": "Bootstrapping vision-language pretraining"},
    {"name": "LLaVA",        "year": 2023, "month": 4,  "category": "Pretraining", "arxiv": "2304.08485", "landmark": True,  "desc": "Large Language and Vision Assistant"},
    {"name": "SigLIP",       "year": 2023, "month": 3,  "category": "Pretraining", "arxiv": "2303.15343", "landmark": False, "desc": "Sigmoid loss for language-image pretraining"},
    {"name": "EVA-CLIP",     "year": 2024, "month": 2,  "category": "Pretraining", "arxiv": "2402.04252", "landmark": False, "desc": "Improved EVA-based CLIP (18B params)"},
    {"name": "InternVL",     "year": 2024, "month": 2,  "category": "Pretraining", "arxiv": "2312.14238", "landmark": False, "desc": "Scaling vision foundation model"},
    {"name": "SigLIP 2",     "year": 2025, "month": 2,  "category": "Pretraining", "arxiv": "2502.14786", "landmark": False, "desc": "Improved SigLIP with multi-resolution"},
    {"name": "Qwen2.5-VL",   "year": 2025, "month": 2,  "category": "Pretraining", "arxiv": "2502.13923", "landmark": True,  "desc": "Qwen2.5 Vision-Language model"},
    {"name": "InternVL3",    "year": 2025, "month": 4,  "category": "Pretraining", "arxiv": "2504.10479", "landmark": False, "desc": "InternVL3 with enhanced capabilities"},
    {"name": "Seed1.5-VL",   "year": 2025, "month": 5,  "category": "Pretraining", "arxiv": "2505.07062", "landmark": False, "desc": "Seed1.5 Vision-Language foundation model"},
    {"name": "MiMo-VL",      "year": 2025, "month": 5,  "category": "Pretraining", "arxiv": "2505.18411", "landmark": False, "desc": "MiMo Vision-Language model"},

    # Tokenizers
    {"name": "VQ-VAE",       "year": 2017, "month": 11, "category": "Tokenizer",   "arxiv": "1711.00937", "landmark": True,  "desc": "Neural discrete representation learning"},
    {"name": "VQ-VAE-2",     "year": 2019, "month": 6,  "category": "Tokenizer",   "arxiv": "1906.00446", "landmark": False, "desc": "Hierarchical VQ-VAE"},
    {"name": "VQGAN",        "year": 2021, "month": 12, "category": "Tokenizer",   "arxiv": "2012.09841", "landmark": True,  "desc": "Taming Transformers for image synthesis", "github": "https://github.com/CompVis/taming-transformers"},
    {"name": "RQ-VAE",       "year": 2022, "month": 3,  "category": "Tokenizer",   "arxiv": "2203.01941", "landmark": False, "desc": "Residual quantization VAE"},
    {"name": "MAGVIT",       "year": 2023, "month": 12, "category": "Tokenizer",   "arxiv": "2212.05199", "landmark": True,  "desc": "Masked generative video transformer"},
    {"name": "FSQ",          "year": 2023, "month": 9,  "category": "Tokenizer",   "arxiv": "2309.15505", "landmark": False, "desc": "Finite scalar quantization"},
    {"name": "VAR",          "year": 2024, "month": 4,  "category": "Tokenizer",   "arxiv": "2404.02905", "landmark": True,  "desc": "Visual autoregressive modeling", "github": "https://github.com/FoundationVision/VAR"},
    {"name": "TiTok",        "year": 2024, "month": 6,  "category": "Tokenizer",   "arxiv": "2406.07550", "landmark": True,  "desc": "1D tokenizer for images", "github": "https://github.com/bytedance/1d-tokenizer"},
    {"name": "MAGVIT-v2",    "year": 2024, "month": 10, "category": "Tokenizer",   "arxiv": "2310.05737", "landmark": False, "desc": "LFQ-based video tokenizer"},
    {"name": "ElasticTok",   "year": 2024, "month": 10, "category": "Tokenizer",   "arxiv": "2410.08368", "landmark": False, "desc": "Adaptive token length tokenizer"},
    {"name": "TokenFlow",    "year": 2024, "month": 12, "category": "Tokenizer",   "arxiv": "2412.03069", "landmark": False, "desc": "Unified image tokenizer", "github": "https://github.com/ByteFlow-AI/TokenFlow"},
    {"name": "VidTok",       "year": 2024, "month": 12, "category": "Tokenizer",   "arxiv": "2412.13061", "landmark": False, "desc": "Video tokenizer (Microsoft)", "github": "https://github.com/microsoft/VidTok"},
    {"name": "QLIP",         "year": 2025, "month": 2,  "category": "Tokenizer",   "arxiv": "2502.05178", "landmark": False, "desc": "Quantized language-image pretraining"},
    {"name": "FlexTok",      "year": 2025, "month": 2,  "category": "Tokenizer",   "arxiv": "2502.13967", "landmark": False, "desc": "Flexible image tokenization"},
    {"name": "FlowMo",       "year": 2025, "month": 3,  "category": "Tokenizer",   "arxiv": "2503.11056", "landmark": False, "desc": "Flow-based tokenizer"},
    {"name": "NFIG",         "year": 2025, "month": 3,  "category": "Tokenizer",   "arxiv": "2503.07076", "landmark": False, "desc": "Non-uniform flow image generation tokenizer"},
    {"name": "EQ-VAE",       "year": 2025, "month": 2,  "category": "Tokenizer",   "arxiv": "2502.09509", "landmark": False, "desc": "Equivariant tokenizer", "github": "https://github.com/zelaki/eqvae"},

    # Unified U+G
    {"name": "SEED",         "year": 2023, "month": 10, "category": "Unified",     "arxiv": "2310.01218", "landmark": False, "desc": "Multimodal seed tokenization", "github": "https://github.com/AILab-CVC/SEED"},
    {"name": "LaVIT",        "year": 2023, "month": 9,  "category": "Unified",     "arxiv": "2309.04596", "landmark": False, "desc": "Language-vision tokenizer"},
    {"name": "Emu",          "year": 2023, "month": 7,  "category": "Unified",     "arxiv": "2307.05222", "landmark": False, "desc": "Emu: Generalist multimodal model"},
    {"name": "LWM",          "year": 2024, "month": 2,  "category": "Unified",     "arxiv": "2402.08268", "landmark": False, "desc": "Large world model", "github": "https://github.com/LargeWorldModel/LWM"},
    {"name": "Chameleon",    "year": 2024, "month": 5,  "category": "Unified",     "arxiv": "2405.09818", "landmark": True,  "desc": "Early-fusion token-based mixed-modal model (Meta)", "github": "https://github.com/facebookresearch/chameleon"},
    {"name": "Transfusion",  "year": 2024, "month": 8,  "category": "Unified",     "arxiv": "2408.11039", "landmark": True,  "desc": "Predict next token and diffuse"},
    {"name": "Show-o",       "year": 2024, "month": 8,  "category": "Unified",     "arxiv": "2408.12528", "landmark": True,  "desc": "One single model for multimodal understanding and generation", "github": "https://github.com/showlab/Show-o"},
    {"name": "ANOLE",        "year": 2024, "month": 7,  "category": "Unified",     "arxiv": "2407.06135", "landmark": False, "desc": "Autoregressive native omni language model"},
    {"name": "Emu3",         "year": 2024, "month": 9,  "category": "Unified",     "arxiv": "2409.18858", "landmark": True,  "desc": "Next-token prediction for vision, language, and action", "github": "https://github.com/baaivision/Emu3"},
    {"name": "Liquid",       "year": 2024, "month": 12, "category": "Unified",     "arxiv": "2412.04332", "landmark": False, "desc": "Language models are scalable multi-modal generators"},
    {"name": "LlamaFusion",  "year": 2024, "month": 12, "category": "Unified",     "arxiv": "2412.15188", "landmark": False, "desc": "Llama for text and image fusion"},
    {"name": "Janus",        "year": 2024, "month": 10, "category": "Unified",     "arxiv": "2410.13848", "landmark": False, "desc": "Decoupling visual encoding for unified multimodal understanding and generation"},
    {"name": "Janus-Pro",    "year": 2025, "month": 1,  "category": "Unified",     "arxiv": "2501.17811", "landmark": True,  "desc": "Unified multimodal understanding and generation (DeepSeek)"},
    {"name": "MUSE-VL",      "year": 2025, "month": 1,  "category": "Unified",     "arxiv": "2501.06599", "landmark": False, "desc": "Multimodal understanding & synthesis"},
    {"name": "Harmon",       "year": 2025, "month": 3,  "category": "Unified",     "arxiv": "2503.07897", "landmark": False, "desc": "Harmonizing visual generation and perception"},
    {"name": "MetaQuery-XL", "year": 2025, "month": 4,  "category": "Unified",     "arxiv": "2504.13979", "landmark": False, "desc": "Meta-query based unified model"},
    {"name": "VARGPT-v1.1",  "year": 2025, "month": 3,  "category": "Unified",     "arxiv": "2503.16278", "landmark": False, "desc": "Visual autoregressive GPT"},
    {"name": "BAGEL",        "year": 2025, "month": 5,  "category": "Unified",     "arxiv": "2505.14683", "landmark": True,  "desc": "Bootstrapped reasoning with AR+Diffusion (ByteDance)", "github": "https://github.com/ByteDance-Seed/Bagel"},
    {"name": "TokLIP",       "year": 2025, "month": 5,  "category": "Unified",     "arxiv": "2505.05422", "landmark": False, "desc": "Tokenized CLIP features for generation"},
    {"name": "MMaDA",        "year": 2025, "month": 5,  "category": "Unified",     "arxiv": "2505.15809", "landmark": False, "desc": "Multimodal masked diffusion model", "github": "https://github.com/Gen-Verse/MMaDA"},
    {"name": "BLIP3-o",      "year": 2025, "month": 6,  "category": "Unified",     "arxiv": "2506.12831", "landmark": False, "desc": "BLIP3 for omni generation"},
    {"name": "Show-o2",      "year": 2025, "month": 6,  "category": "Unified",     "arxiv": "2506.15564", "landmark": True,  "desc": "Improved Show-o with enhanced generation"},
    {"name": "OmniGen2",     "year": 2025, "month": 6,  "category": "Unified",     "arxiv": "2506.18871", "landmark": True,  "desc": "Unified image generation (OmniGen2)"},
    {"name": "Selftok",      "year": 2025, "month": 5,  "category": "Unified",     "arxiv": "2505.19065", "landmark": False, "desc": "Self-supervised tokenization for generation"},
    {"name": "UniDisc",      "year": 2025, "month": 3,  "category": "Unified",     "arxiv": "2503.20853", "landmark": False, "desc": "Unified discrete diffusion"},
    {"name": "Muddit",       "year": 2025, "month": 5,  "category": "Unified",     "arxiv": "2505.16965", "landmark": False, "desc": "Multimodal unified discrete diffusion transformer"},
    {"name": "HermesFlow",   "year": 2025, "month": 3,  "category": "Unified",     "arxiv": "2503.12580", "landmark": False, "desc": "Hermes flow-based unified generation"},

    # Any-to-Any
    {"name": "CoDi",         "year": 2023, "month": 5,  "category": "Any2Any",     "arxiv": "2305.11846", "landmark": True,  "desc": "Any-to-any generation via composable diffusion"},
    {"name": "NExT-GPT",     "year": 2023, "month": 9,  "category": "Any2Any",     "arxiv": "2309.05519", "landmark": True,  "desc": "Any-to-any multimodal LLM"},
    {"name": "AnyGPT",       "year": 2024, "month": 2,  "category": "Any2Any",     "arxiv": "2402.12226", "landmark": False, "desc": "Unified multimodal LLM with discrete sequence modeling"},
    {"name": "Unified-IO 2", "year": 2024, "month": 3,  "category": "Any2Any",     "arxiv": "2312.17172", "landmark": False, "desc": "Unified I/O for diverse tasks"},
    {"name": "CoDi-2",       "year": 2024, "month": 1,  "category": "Any2Any",     "arxiv": "2311.18775", "landmark": False, "desc": "Improved CoDi with in-context generation"},
    {"name": "MIO",          "year": 2024, "month": 9,  "category": "Any2Any",     "arxiv": "2409.17692", "landmark": False, "desc": "Multimodal interleaved output model"},
    {"name": "OmniFlow",     "year": 2025, "month": 12, "category": "Any2Any",     "arxiv": "2412.01169", "landmark": False, "desc": "Omni flow for any-to-any generation"},
    {"name": "Spider",       "year": 2025, "month": 1,  "category": "Any2Any",     "arxiv": "2501.03461", "landmark": False, "desc": "Spider any-to-any model"},
    {"name": "Ming-Omni",    "year": 2025, "month": 5,  "category": "Any2Any",     "arxiv": "2505.02471", "landmark": True,  "desc": "Ming all-modal omni model"},
    {"name": "Qwen3-Omni",   "year": 2025, "month": 6,  "category": "Any2Any",     "arxiv": "2506.00513", "landmark": False, "desc": "Qwen3 omni model"},
    {"name": "M2-omni",      "year": 2025, "month": 2,  "category": "Any2Any",     "arxiv": "2502.18778", "landmark": False, "desc": "M2 omni multimodal model"},

    # Omni Models
    {"name": "GPT-4o",           "year": 2024, "month": 5,  "category": "Omni", "arxiv": "", "landmark": True,  "desc": "GPT-4 Omni (OpenAI) - audio, vision, text"},
    {"name": "VITA",             "year": 2024, "month": 8,  "category": "Omni", "arxiv": "2408.05505", "landmark": False, "desc": "Open-source interactive omni model"},
    {"name": "LLaMA-Omni",       "year": 2024, "month": 9,  "category": "Omni", "arxiv": "2409.06666", "landmark": False, "desc": "Seamless speech interaction with LLaMA"},
    {"name": "Gemini 1.5 Pro",   "year": 2024, "month": 2,  "category": "Omni", "arxiv": "", "landmark": True,  "desc": "Gemini 1.5 Pro (Google) - long context multimodal"},
    {"name": "Qwen2.5-Omni",     "year": 2025, "month": 3,  "category": "Omni", "arxiv": "2503.20215", "landmark": True,  "desc": "Qwen2.5 omnivore multimodal model"},
    {"name": "VITA-1.5",         "year": 2025, "month": 1,  "category": "Omni", "arxiv": "2501.12599", "landmark": False, "desc": "VITA 1.5 with improved capabilities"},
    {"name": "MiniCPM-o 2.6",    "year": 2025, "month": 1,  "category": "Omni", "arxiv": "2501.15481", "landmark": False, "desc": "MiniCPM omni model 2.6"},
    {"name": "Gemini 2.0 Flash",  "year": 2025, "month": 2,  "category": "Omni", "arxiv": "", "landmark": False, "desc": "Gemini 2.0 Flash (Google)"},
    {"name": "SALMONN-Omni",     "year": 2025, "month": 1,  "category": "Omni", "arxiv": "2501.10801", "landmark": False, "desc": "Speech audio language music omni model"},
    {"name": "Gemini 2.5 Pro",   "year": 2025, "month": 3,  "category": "Omni", "arxiv": "", "landmark": True,  "desc": "Gemini 2.5 Pro (Google) - state-of-the-art"},
    {"name": "InternVL3",        "year": 2025, "month": 4,  "category": "Omni", "arxiv": "2504.10479", "landmark": False, "desc": "InternVL3 omni-capable model"},
    {"name": "MiniCPM-o 4.5",    "year": 2025, "month": 11, "category": "Omni", "arxiv": "2511.07905", "landmark": False, "desc": "MiniCPM omni 4.5 - enhanced"},
    {"name": "NExT-OMNI",        "year": 2025, "month": 6,  "category": "Omni", "arxiv": "2506.08838", "landmark": False, "desc": "NExT-OMNI all-modal model"},
    {"name": "Gemini 3.1 Pro",   "year": 2026, "month": 2,  "category": "Omni", "arxiv": "", "landmark": True,  "desc": "Gemini 3.1 Pro (Google) - latest flagship"},
    {"name": "InteractiveOmni",  "year": 2025, "month": 3,  "category": "Omni", "arxiv": "2503.17366", "landmark": False, "desc": "Interactive omni model"},
    {"name": "Step3",            "year": 2025, "month": 6,  "category": "Omni", "arxiv": "", "landmark": False, "desc": "Step3 omni model"},
]

# ─────────────────────────────────────────────────────────────────────────────
# META CONFIG
# ─────────────────────────────────────────────────────────────────────────────
META = {
    "title": "Awesome Native Multimodal Models",
    "subtitle": "Interactive Visualizations — Architecture Taxonomy & Model Timeline",
    "paper_count": "400+",
    "last_updated": "2026-03",
    "github_url": "https://github.com/your-username/Awesome-Native-Multimodal-Models",
    "categories": {
        "Pretraining": {"color": "#FAD7A0", "label": "Pretraining Foundations"},
        "Tokenizer":   {"color": "#4ECDC4", "label": "Image & Video Tokenizers"},
        "Unified":     {"color": "#FF6B6B", "label": "Unified U+G"},
        "Any2Any":     {"color": "#A8E6CF", "label": "Any-to-Any"},
        "Omni":        {"color": "#DDA0DD", "label": "Omni Models"},
    },
}
