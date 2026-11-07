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
| 2026-10-29 | **Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities** | Yunhang Shen, Zhangquan Chen et al. | Youtu-Parsing-Omni, an omni-modal parser that converts documents, images, audio… | [📄 2610.39301](https://arxiv.org/abs/2610.39301) `cs.CV` |
| 2026-10-28 | **JYVA at BeTraC: Audio-Based Medical Note Generation with SOAP Section-Specific Queries** | Youness Dkhissi, Valentin Vielzeuf et al. | Our submission to the Beyond Transcription Challenge (BeTraC) on medical note generation from d… | [📄 2610.40695](https://arxiv.org/abs/2610.40695) `cs.SD` |
| 2026-10-28 | **Efficient Agentic Audio-Visual Question Answering through Toolset Pruning and Modality Consolidation** | Yi Wang, Tianzi Wang et al. | Fine-grained audio-visual question answering (AVQA) requires models to resolve complex cross-mo… | [📄 2610.38960](https://arxiv.org/abs/2610.38960) `cs.AI` |
| 2026-10-27 | **Live-OPSD: On-Policy Self-Distillation for Proactive Streaming Large Video Models** | Kaixuan Du, Xin Wan et al. | Streaming multimodal assistants must make response decisions while events are still unfolding… | [📄 2610.36959](https://arxiv.org/abs/2610.36959) `cs.LG` |
| 2026-10-27 | **Who Knows What - and What Does It Support? Perspective-Bounded Evidence Calibration for Multimodal Theory of Mind** | Ziqi Liao, Jiaqi Shen et al. | Theory of Mind (ToM), the ability to infer others' beliefs, goals, and intentions… | [📄 2610.36824](https://arxiv.org/abs/2610.36824) `cs.AI` |
| 2026-10-26 | **Heard Enough to Act: Early Tool Calling in Spoken Dialogue Systems** | Yizhou Peng, Chen Chen et al. | Latency-sensitive spoken agents must know not only which tool to call… | [📄 2610.34653](https://arxiv.org/abs/2610.34653) `cs.CL` |
| 2026-10-26 | **Adapting LLM-SC to Living Sacred Heritage: Domain-Specific Extraction, Semantic Networks and Human Evaluation on Pashupatinath Temple Reviews** | Pujan Pant, Sagar Newpane et al. | Large language model (LLM) pipelines can turn visitor reviews into structured data… | [📄 2610.35685](https://arxiv.org/abs/2610.35685) `cs.CL` |
| 2026-10-25 | **Does the Outfit Change the Price? Context Halo in Vision-Language Model Valuation of an Identical Low-Cost Necklace** | Brianne Lee | A chunky gold-tone chain necklace bought online for 2.43 USD was photographed four ways: worn w… | [📄 2610.34591](https://arxiv.org/abs/2610.34591) `cs.CL` |
| 2026-10-23 | **A Broader Look into MLLM's Retrieval Heads** | Jia Wang, Yuqing Li et al. | Locating relevant evidence in long inputs is a core capability of Multimodal Large Language Mod… | [📄 2610.32411](https://arxiv.org/abs/2610.32411) `cs.CL` |
| 2026-10-23 | **Acoustic and Lexical Signals for Native Language Identification of Language Learners** | Ahmet Yavuz Uluslu, Mengjie Qian et al. | Spoken native language (L1) identification for second language learners has traditionally relie… | [📄 2610.32382](https://arxiv.org/abs/2610.32382) `cs.CL` |
| 2026-10-23 | **CEMIR vs. FISER: a comparative study of reasoning-based and enrichment-based approaches to pragmatic intent recognition** | Ziya Hosseynzadeh, Farjad Fallah et al. | Intent recognition in human-robot interaction requires agents to resolve ambiguous natural lang… | [📄 2610.32022](https://arxiv.org/abs/2610.32022) `cs.AI` |
| 2026-10-22 | **Efficient Omni-modal Large Language Model Inference via Per-Query Modality Selection** | Shuqi Liu, Yuzhou Cao et al. | Omni-modal large language models (Omni-LLMs) can jointly process a broad range of modalities… | [📄 2610.31768](https://arxiv.org/abs/2610.31768) `cs.LG` |
| 2026-10-22 | **TRIAD: Benchmarking Omni-Modal Ambiguity in Multimodal Large Language Models** | Zhaolu Kang, Yidi Wang et al. | Ambiguity is a central feature of natural communication: a sentence, image… | [📄 2610.30841](https://arxiv.org/abs/2610.30841) `cs.CL` |
| 2026-10-22 | **Omni-UBench: Benchmarking Omni-Modal LLM-based Guardrails Across Safety, Utility, and Reliability** | Junhao Wang, Yidou Chen et al. | Advances in Omni-modal Large Language Models (OLLMs) have enabled increasingly seamless human-A… | [📄 2610.31713](https://arxiv.org/abs/2610.31713) `cs.CR` |
| 2026-10-22 | **DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model** | Zixian Gao, Lixin Xiu et al. | A live esports broadcast needs a director who chooses which camera goes on air and a caster who… | [📄 2610.31734](https://arxiv.org/abs/2610.31734) `cs.CV` |
| 2026-10-22 | **Query-Conditioned Liquid Temporal Grounding for Long-Form Audio** | Yuelan Cheng, Yonggang Zhu et al. | Long-form temporal audio grounding (TAG) is challenging because target events often occupy only… | [📄 2610.31252](https://arxiv.org/abs/2610.31252) `cs.SD` |
| 2026-10-21 | **Agentic Music Post-Production** | Jaywon Koo, Junghyun Koo et al. | MixAgent, an agentic pipeline for music post-production that follows the workflow of audio engi… | [📄 2610.29093](https://arxiv.org/abs/2610.29093) `cs.SD` |
| 2026-10-21 | **MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents** | Hong Ting Tsang, Boyi Zhang et al. | Omni-modal assistants must remember not only what users say… | [📄 2610.29249](https://arxiv.org/abs/2610.29249) `cs.CL` |
| 2026-10-21 | **Omnilingual-MsASR: Benchmarking Multimodal, Multilingual, Long-Form Multi-Speaker ASR of Omni Large Language Models** | Yuan Ge, Pei Zhang et al. | Omni-modal large language models (LLMs) have achieved remarkable progress in audio and video un… | [📄 2610.29455](https://arxiv.org/abs/2610.29455) `cs.CL` |
| 2026-10-21 | **Balancing Foundation Models and Trait-Specific Learning for Forehead-Crease Recognition** | Geetanjali Sharma, Aryan Jain et al. | Biometric recognition often degrades under partial facial vis- ibility… | [📄 2610.29495](https://arxiv.org/abs/2610.29495) `cs.CV` |
| 2026-10-20 | **DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents** | Yuxuan Li, Xiangchen Guan et al. | Full-duplex speech agents must update persistent memory while listening and speaking… | [📄 2610.27581](https://arxiv.org/abs/2610.27581) `cs.AI` |
| 2026-10-20 | **DIVE: Benchmarking Full-Duplex Interaction with Visual Engagement in Continuous Streams** | Yuhang Chen, Guangyue Liu et al. | Recent advances in multimodal large language models (MLLMs) have substantially improved spoken… | [📄 2610.28405](https://arxiv.org/abs/2610.28405) `cs.AI` |
| 2026-10-20 | **SKAD: Sketch-Guided Audio-Contrastive Decoding for Reasoning in Large Audio-Language Models** | Junyu Wang, Peiyuan Jiang et al. | Large Audio-Language Models (LALMs) have shown increasing potential in audio understanding and… | [📄 2610.28146](https://arxiv.org/abs/2610.28146) `eess.AS` |
| 2026-10-19 | **Focused Omni-Modal GUI Agents** | Fuyao Zhang, Wenwen He et al. | Graphical User Interface (GUI) agents increasingly act over streaming omni-modal observations s… | [📄 2610.26203](https://arxiv.org/abs/2610.26203) `cs.CV` |
| 2026-10-19 | **OmniGround: Strengthening Omni-Modal Temporal Grounding via Attention-Consistency Training** | Zixuan Chen, Depeng Wang et al. | Omni-modal large language models can jointly understand video, audio, and text… | [📄 2610.25929](https://arxiv.org/abs/2610.25929) `cs.CV` |
| 2026-10-19 | **Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs** | Zijian Liu, Chaoyou Fu et al. | Recent Omni LLMs (OLLMs) have demonstrated remarkable capabilities in joint audio-visual reason… | [📄 2610.27103](https://arxiv.org/abs/2610.27103) `cs.AI` [💻](https://github.com/ZiiJianLiu/Omni-Woodpecker) |
| 2026-10-19 | **Scaling Parameter-Efficient Fine-Tuning for Brain Encoding** | Zhuofan Josh Ying, Guanglong Sun et al. | Brain encoding models aim to predict neural responses to stimuli… | [📄 2610.26802](https://arxiv.org/abs/2610.26802) `cs.LG` |
| 2026-10-19 | **Standing on the Shoulders of Giants: Enhancing LLM Agents for Automated Fact-Checking with Human Expert Skills** | Xinwen Chen, Haorui He et al. | Automated fact-checking (AFC) systems powered by large language model (LLM) agents still face c… | [📄 2610.25777](https://arxiv.org/abs/2610.25777) `cs.AI` |
| 2026-10-19 | **Train An Imaginative Agent** | Jiaxin Ge, Junyi Zhang et al. | A seemingly reasonable push in Sokoban can make the puzzle unsolvable… | [📄 2610.26845](https://arxiv.org/abs/2610.26845) `cs.AI` |
| 2026-10-17 | **Long Listening Thoughts: Eliciting Open Auditory Reasoning with Deliberative Perception and Cognitive Refinement** | Jaeyeon Kim, Chao-Han Huck Yang et al. | Long Listening Thoughts (LLT), a framework for constructing post-training datasets that improve… | [📄 2610.24409](https://arxiv.org/abs/2610.24409) `cs.SD` |
| 2026-10-16 | **Jarvis: Coordination Deserves a Brain of Its Own in Agentic Interactive Models** | Yuxiang Wang, Shengbo Cai et al. | Interactive models increasingly hand complex reasoning and tool use to a slow brain in the back… | [📄 2610.23804](https://arxiv.org/abs/2610.23804) `cs.SD` |
| 2026-10-16 | **Perceive, Solve, Reason: Progressive Capability Formation in Time Series-LLMs** | Xin Qiu, Junlong Tong et al. | Large language models (LLMs) can now perceive, describe, and reason about images and audio… | [📄 2610.23521](https://arxiv.org/abs/2610.23521) `cs.CL` |
| 2026-10-15 | **PW-Pruning: Phase-Aware Expert Selection for Speech-Centric Omni-Modal Models** | Junjie Cao, Fengping Tian et al. | Sparse routing reduces per-token computation but leaves the full expert bank resident in memory… | [📄 2610.26891](https://arxiv.org/abs/2610.26891) `eess.AS` |
| 2026-10-15 | **Full-Duplex Interaction with Speech, Expressions and Gestures** | Siyin Wang, Wenyi Yu et al. | Human face-to-face conversation requires coordinating speech… | [📄 2610.21452](https://arxiv.org/abs/2610.21452) `eess.AS` |
| 2026-10-15 | **When Reasoning Is Not Enough: Proactive Inquiry for Cross-Modal Safety in Multimodal Large Language Models** | Wei Cai, Jian Zhao et al. | Multimodal large language models (MLLMs) can act unsafely when individually benign images and t… | [📄 2610.22068](https://arxiv.org/abs/2610.22068) `cs.AI` |
| 2026-10-15 | **When Models Misread Ink: Auditing VLMs for Arabic Calligraphy Recognition** | Niaz Mohaiman Abtahi, Evan Maksud et al. | Arabic calligraphy is a high-stakes cultural visual domain for Muslim communities… | [📄 2610.22018](https://arxiv.org/abs/2610.22018) `cs.CV` |
| 2026-10-15 | **Beyond Generation: Using Multimodal LLMs as Detectors of LLM-Generated Deepfake Facial Images** | Olivia Salamon, Virginia N. L. Franqueira et al. | As image generation models become increasingly capable of producing highly realistic content… | [📄 2610.21760](https://arxiv.org/abs/2610.21760) `cs.CV` |
| 2026-10-15 | **MYOPIA: Understanding the Limits of Tree-Based Reasoning in Vision-Language Models** | Islam Mesabah, Sary Elmansoury et al. | Decision trees can make vision-language model (VLM) classification interpretable by replacing a… | [📄 2610.21573](https://arxiv.org/abs/2610.21573) `cs.CV` |
| 2026-10-14 | **Designing Textual Interfaces To Enhance Llm Reasoning On Audio-Visual Question Answering** | Yi Wang, Tianzi Wang et al. | Automatic prompt optimization (APO) has shown strong effectiveness for text-based LLMs and LLM… | [📄 2610.20085](https://arxiv.org/abs/2610.20085) `cs.AI` |
| 2026-10-14 | **Soloist: A Generative Model for Blind Voice Separation in the Wild** | Chen Yang, ChuFan Yu et al. | Real-world voice separation must recover individual voices from overlapping speech… | [📄 2610.19716](https://arxiv.org/abs/2610.19716) `cs.SD` |
| 2026-10-13 | **Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation** | Nikolay Semenov, Artem Riabinin et al. | Kandinsky S2V 1.0, an open family of speech-to-video models for controllable audio-driven human… | [📄 2610.19290](https://arxiv.org/abs/2610.19290) `cs.CV` |
| 2026-10-13 | **OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding** | Xuyang Liu, Shihao Wang et al. | With the rapid development of multimodal large language models (MLLMs)… | [📄 2610.18829](https://arxiv.org/abs/2610.18829) `cs.CV` |
| 2026-10-13 | **Beyond Aggregate Accuracy: Item-Level Transitions in Prompt Optimization** | Chinmoy Mitra, Tarek Mahmud | Automatic prompt optimization (APO) uses feedback from model responses to improve prompts autom… | [📄 2610.19084](https://arxiv.org/abs/2610.19084) `cs.LG` |
| 2026-10-12 | **D2: High-Capability Full-Duplex Spoken Language Models from Half-Duplex Backbones** | Cheng-Kuang Chang, Alexander H. Liu et al. | Full-duplex spoken language models (FD-SLMs) support simultaneous listening and speaking… | [📄 2610.17124](https://arxiv.org/abs/2610.17124) `cs.CL` |
| 2026-10-12 | **Omni-Modal LLMs Know More Than They Say** | Na Min An, Taekyung Kim et al. | Omni-modal large language models (Omni-LLMs) extend LLMs to process heterogeneous modalities (e… | [📄 2610.16135](https://arxiv.org/abs/2610.16135) `cs.CL` |
| 2026-10-12 | **SyncReward: Human-Aligned Synchronization Reward for Audio-Visual Generation** | Kaisi Guan, Ying Ba et al. | Recent years have witnessed rapid progress in joint audio--visual generation… | [📄 2610.16338](https://arxiv.org/abs/2610.16338) `cs.CV` |
| 2026-10-12 | **PitchIn: Natural-Language Vocal Coaching from Unstructured Community Feedback** | Hayeon Bang, Hounsu Kim et al. | Effective vocal coaching connects performance issues with corrective advice… | [📄 2610.17036](https://arxiv.org/abs/2610.17036) `cs.SD` |
| 2026-10-12 | **ScreenASR-Bench: A Tiered Benchmark for Speech Recognition with Visual Context** | Mingwei Fu, Zheshu Song et al. | Current ASR models perform well on general benchmarks but still struggle with acoustically ambi… | [📄 2610.16260](https://arxiv.org/abs/2610.16260) `cs.AI` |
| 2026-10-12 | **Estimating Uncertainty of Omnimodal Large Language Models via External Omnimodal Embeddings** | Iacopo Ghinassi, Hy Nguyen Gia La et al. | Recent work has investigated Omni-modal Large Language Models (OLLMs)… | [📄 2610.16933](https://arxiv.org/abs/2610.16933) `cs.CL` |
| 2026-10-11 | **HMU-Bench: Hierarchical Music Understanding Benchmark for Omni Models** | Zheqi Dai, Boyang Wang et al. | Music-understanding benchmarks should identify both the evidence available to a model and the o… | [📄 2610.15773](https://arxiv.org/abs/2610.15773) `eess.AS` |
| 2026-10-08 | **EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams** | Heeseung Kim | Wearable augmented reality (AR) assistants are moving toward continuous real-world interaction… | [📄 2610.12248](https://arxiv.org/abs/2610.12248) `cs.CL` |
| 2026-10-08 | **When History Helps and Hurts: Selective History Use across Multimodal Turns** | Shuoyang Sun, Kerui Gu et al. | Reliable multimodal interaction depends on selective use of conversational history: an earlier… | [📄 2610.11948](https://arxiv.org/abs/2610.11948) `cs.CL` |
| 2026-10-08 | **MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement** | Xiaomi LLM-Core Team, : et al. | Reinforcement learning (RL) is the central training paradigm for advancing large foundation mod… | [📄 2610.11959](https://arxiv.org/abs/2610.11959) `cs.CL` |
| 2026-10-07 | **vLLM-Omni Technical Report: A Unified Serving Runtime for Omni-Modality Generation** | vLLM-Omni Team | Interaction with intelligent systems is expanding beyond text-centric chatbots and coding agent… | [📄 2610.09307](https://arxiv.org/abs/2610.09307) `cs.DC` |
| 2026-10-07 | **CrossEdit: Cross-Modal Training Enables Rich Audio-Visual Editing** | William Chen, Prem Seetharaman et al. | Multimedia editing requires generative models to interpret complex… | [📄 2610.10264](https://arxiv.org/abs/2610.10264) `cs.SD` |
| 2026-10-04 | **TS-SP: Learning Speaker-Preserving Representations in Audio Large Language Models** | Junjie Li, Zheng Liang et al. | Audio large language models (ALLMs) can understand speech content… | [📄 2610.04887](https://arxiv.org/abs/2610.04887) `cs.SD` |
| 2026-10-02 | **Text-Centric Post-Training for Omni-Modal Reasoning** | Ziyang Cheng, Yuhao Wang et al. | Improving joint audio-visual reasoning in Omni Large Language Models typically incurs substanti… | [📄 2610.02819](https://arxiv.org/abs/2610.02819) `cs.CL` |
| 2026-10-02 | **OmniConfess: Eliciting Token Confessions to Mitigate Omni-Modal Hallucination** | Huiqiang Rong, Haoran Luo et al. | Omni-modal large language models (OmniLLMs) unify text, images, audio, and video… | [📄 2610.02999](https://arxiv.org/abs/2610.02999) `cs.CL` |
| 2026-10-02 | **Batched Speech Decisions Without Decoding: Single-Token Supervision Lets a Frozen LLM Hear Beyond the Transcript** | Jie Jin, Ziyin Ma et al. | Full-duplex voice agents make many small, closed decisions… | [📄 2610.02638](https://arxiv.org/abs/2610.02638) `cs.AI` |
| 2026-10-01 | **Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation** | Mohammed Irfan Kurpath, Jaseel Muhammad Kaithakkodan et al. | Extending a text embedding model to new modalities typically degrades text retrieval quality… | [📄 2610.02148](https://arxiv.org/abs/2610.02148) `cs.CV` |
| 2026-09-30 | **LEAP: Learned Block-wise Evidence Retrieval for Long Audio-Video Perception** | Juyi Lin, Zhiqiang Lao et al. | Hour-scale audio-visual question answering is constrained by a context dilemma: dense whole-rec… | [📄 2609.39938](https://arxiv.org/abs/2609.39938) `cs.CL` |
| 2026-09-30 | **OmniReasoning: Pushing the Limits of Audio-Visual Joint Reasoning** | Junming Lin, Yuxuan Wang et al. | Recent advances have enabled unified omni-modal models in understanding audio, vision… | [📄 2609.39490](https://arxiv.org/abs/2609.39490) `cs.CV` |
| 2026-09-30 | **Learning to Reason with Compressed Context: Ground-Truth-Free Adaptation of OmniLLMs via Self-Distillation** | Jianghao Wang, Ke Meng et al. | Omni-modal large language models (OmniLLMs) enable unified audio-video understanding… | [📄 2609.39953](https://arxiv.org/abs/2609.39953) `cs.CV` |
| 2026-09-30 | **Index-Translate: A Multilingual Translation Model Family -- Text, Speech, Controlled Dubbing, and Long-Document Translation** | Tianjiao Li, Mengran Yu et al. | Index-Translate, a multilingual translation model family that combines a shared multilingual fo… | [📄 2609.40181](https://arxiv.org/abs/2609.40181) `cs.CL` |
| 2026-09-30 | **OP-CAD: On-Policy Clean-Audio Distillation for Robust Audio-Visual Reasoning** | Xingming Shui, Dapeng Chen et al. | Omni-modal large language models deployed in real-world environments encounter external noise t… | [📄 2609.39150](https://arxiv.org/abs/2609.39150) `cs.CV` |
| 2026-09-29 | **MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation** | Ke Wang, Houxing Ren et al. | End-to-end full-duplex speech models have brought open-source machine conversation closer to hu… | [📄 2609.36903](https://arxiv.org/abs/2609.36903) `cs.CL` |
| 2026-09-29 | **Seeing What Should Be Heard: Diagnosing and Repairing Cross-Modal Shortcuts in Omni-Modal LLMs** | Yueran Ma, Ronghao Lin | Omni-modal large language models (LLMs) are expected to answer a question using the modality it… | [📄 2609.36798](https://arxiv.org/abs/2609.36798) `cs.CV` |
| 2026-09-29 | **Calibrate the Decisions That Change the Future: On-Policy Post-Training Quantization for Multimodal Large Language Models** | Wenxiao Fan, Jingling Fu et al. | Post-training quantization (PTQ) lowers deployment cost for multimodal large language models… | [📄 2609.36828](https://arxiv.org/abs/2609.36828) `cs.AI` |
| 2026-09-28 | **HiThink Turn: An Intent-Aware Turn-Taking Control Module for Full-Duplex Dialogue** | Feiyang Chen, Wenhan Yang et al. | Full-duplex dialogue requires timely yet selective interruption handling… | [📄 2609.34096](https://arxiv.org/abs/2609.34096) `cs.HC` |
| 2026-09-28 | **SyncRA: Learning Temporal Correspondence in Omni-Modal Models** | Zelong Xu, Yan Li et al. | Recent omni-modal models demonstrate strong perception of audio and visual inputs… | [📄 2609.34363](https://arxiv.org/abs/2609.34363) `cs.CV` |
| 2026-09-28 | **Uncovering Ordinal-Matching Bias in Audio-Visual LLMs** | Jihoo Jung, Youngjoon Jang et al. | This work aims to improve how audio-visual large language models (AVLLMs) associate speech with… | [📄 2609.34223](https://arxiv.org/abs/2609.34223) `cs.CV` |
| 2026-09-28 | **OmniTide: Co-Designing Algorithms and Systems for Efficient On-Device Omni-LLM Streaming** | Zongshang Shen, Wangsong Yin et al. | On-device streaming omni-modal inference safeguards user privacy and eliminates prohibitive per… | [📄 2609.34653](https://arxiv.org/abs/2609.34653) `cs.AI` |
| 2026-09-28 | **DuplexCadence: Exact State and Execution from a Speech Model's Declared Timelines** | Haixiao Gao, Yimin Zheng et al. | Full-duplex speech models support streaming interaction that listens and speaks at the same tim… | [📄 2609.35115](https://arxiv.org/abs/2609.35115) `cs.AI` |
| 2026-09-27 | **When Does the Concept of "Dog" Emerge in an Audio LLM?** | Zhe Wang, Shiqi Liu et al. | Multimodal large language models answer audio questions… | [📄 2609.33458](https://arxiv.org/abs/2609.33458) `cs.AI` |
| 2026-09-27 | **Tokens Change, Structure Endures: Spectral Watermarking for Generated Speech** | Kanghwi Lee, Kyeongseok Jeong et al. | Watermarking is a promising tool for establishing the provenance of AI-generated speech… | [📄 2609.33774](https://arxiv.org/abs/2609.33774) `cs.SD` |
| 2026-09-25 | **Duplex-MPE: Benchmarking Multi-Party Interaction in Full-Duplex Dialogue** | Chengqian Ma, Wenhao Feng et al. | Real-time full-duplex speech models can listen while speaking… | [📄 2609.31948](https://arxiv.org/abs/2609.31948) `cs.SD` |
| 2026-09-24 | **AdaptDuplex: From Static to Adaptive Full-Duplex Spoken Dialogue** | Zhiyang Zhou, Yingxin Shang et al. | Full-duplex spoken dialogue requires simultaneous listening and speaking at sub-second latency… | [📄 2609.29217](https://arxiv.org/abs/2609.29217) `cs.SD` |
| 2026-09-24 | **Do Audio Language Models Hear and Read Distinctive Features Alike?** | Yuanhao Chen, Peter Chin | Audio language models pass speech and text through a single decoder… | [📄 2609.30167](https://arxiv.org/abs/2609.30167) `cs.CL` |
| 2026-09-23 | **A Harness for Synthesizing Diverse Naturalistic Full-Duplex Conversations** | Matthew Sun, Vinay Kothapally et al. | Full-duplex dialogue systems, which listen while speaking… | [📄 2609.28806](https://arxiv.org/abs/2609.28806) `eess.AS` |
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
