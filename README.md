<p align="center">
  <a href="https://clare-nie.github.io/Awesome-Personalization-in-MLLMs/">
    <img src="./assets/logo.png" alt="Awesome Personalization in MLLMs" width="960">
  </a>
</p>


> The most comprehensive survey and frontier tracking repository for personalized LLMs and MLLMs, covering **personalized memory**, **alignment**, **retrieval**, and **evaluation**.

[Project Page](https://clare-nie.github.io/Awesome-Personalization-in-MLLMs/) | [中文 README](./README_zh.md)

## 📖 Overview

Personalized LLMs and MLLMs aim to move beyond one-size-fits-all assistants. Instead of only optimizing for average human preference, they need to model a specific user: long-term goals, evolving preferences, implicit personas, multimodal context, and when personalization should or should not be applied.

This repository tracks papers, benchmarks, datasets, and systems around four connected research directions:

| Direction | Core Question |
| :--- | :--- |
| **Personalized Memory** | What should an agent store, update, retrieve, compress, and forget? |
| **Personalized Alignment** | How can a model adapt to individual preferences, personalities, and contexts? |
| **Personalized Retrieval** | How should systems select the right user context, memory, and evidence? |
| **Personalized Evaluation** | How do we evaluate long-term, dynamic, implicit, and multimodal personalization? |

## 📑 Table of Contents

- [Surveys](#surveys)
- [Personalized Memory](#personalized-memory)
  - [Memory Architectures](#memory-architectures)
  - [Personalized Memory Architectures](#personalized-memory-architectures)
  - [Latent Memory Mechanisms](#latent-memory-mechanisms)
- [Personalized Alignment](#personalized-alignment)
- [Personalized Retrieval](#personalized-retrieval)
- [Personalized Evaluation](#personalized-evaluation)

<br>

## 📚 Surveys

| Date | Paper Title | Venue | Publication | Resources |
| :--- | :--- | :--- | :--- | :--- |
| 2026.03 | [Survey on AI Memory: Theories, Taxonomies, Evaluations, and Emerging Trends](https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf) | BaiJia AI / BUPT / Huawei | Preprint | [BAI-LAB/Survey-on-AI-Memory](https://github.com/BAI-LAB/Survey-on-AI-Memory) |
| 2026.02 | [Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations](https://arxiv.org/abs/2602.19320) | Agentic Memory Research Team | arXiv | [FredJiang0324/Anatomy-of-Agentic-Memory](https://github.com/FredJiang0324/Anatomy-of-Agentic-Memory) <br> ![Stars](https://img.shields.io/github/stars/FredJiang0324/Anatomy-of-Agentic-Memory?style=flat-square&logo=github) |
| 2025.12 | [Memory in the Age of AI Agents: A Survey](https://arxiv.org/abs/2512.13564) | NUS / Renmin University of China / Fudan University / Peking University / OPPO | arXiv | [Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) |
| 2025.04 | [A Survey of Personalization: From RAG to Agent](https://arxiv.org/abs/2504.10147) | Applied Machine Learning Lab | arXiv | [Applied-Machine-Learning-Lab/Awesome-Personalized-RAG-Agent](https://github.com/Applied-Machine-Learning-Lab/Awesome-Personalized-RAG-Agent) |
| 2024.12 | [Personalized Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2412.02142) | Adobe Research / UCSD / Salesforce / Amazon / University of Rochester | arXiv | - |
| 2024.10 | [Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027) | Adobe Research / UCSD / Salesforce / Amazon | arXiv | - |

<br>

## 🧠 Personalized Memory

> ![#0f9f8f](https://img.shields.io/badge/-_#0f9f8f-0f9f8f?style=flat-square) *What should an agent store, update, retrieve, compress, and forget?*

### Memory Architectures

| Date | Paper Title | Venue | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.05 | [Belief Memory: Agent Memory Under Partial Observability](https://arxiv.org/abs/2605.05583) | MBZUAI / RIKEN AIP / UT Austin / Wuhan University | arXiv | - |
| 2026.05 | [MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents](https://arxiv.org/abs/2605.03312) | New Jersey Institute of Technology | arXiv | - |
| 2026.04 | [Memory Intelligence Agent](https://arxiv.org/abs/2604.04503) | East China Normal University / Shanghai Innovation Institute / HIT / Xiamen University / Shanghai AI Laboratory | arXiv | [ECNU-SII/MIA](https://github.com/ECNU-SII/MIA) <br> ![Stars](https://img.shields.io/github/stars/ECNU-SII/MIA?style=flat-square&logo=github) |
| 2026.04 | [HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents](https://arxiv.org/abs/2604.16839) | HKUST | arXiv | [ReinerBRO/HeLa-Mem](https://github.com/ReinerBRO/HeLa-Mem) <br> ![Stars](https://img.shields.io/github/stars/ReinerBRO/HeLa-Mem?style=flat-square&logo=github) |
| 2026.03 | [AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution](https://arxiv.org/abs/2603.01145) | East China Normal University / Shanghai AI Laboratory | arXiv | [ECNU-ICALK/AutoSkill](https://github.com/ECNU-ICALK/AutoSkill) <br> ![Stars](https://img.shields.io/github/stars/ECNU-ICALK/AutoSkill?style=flat-square&logo=github) |
| 2026.02 | [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474) | Nanyang Technological University | arXiv | [ViktorAxelsen/MemSkill](https://github.com/ViktorAxelsen/MemSkill) <br> ![Stars](https://img.shields.io/github/stars/ViktorAxelsen/MemSkill?style=flat-square&logo=github) |
| 2026.01 | [EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://arxiv.org/abs/2601.02163) | EverMind AI | arXiv | [EverMind-AI/EverMemOS](https://github.com/EverMind-AI/EverMemOS) <br> ![Stars](https://img.shields.io/github/stars/EverMind-AI/EverMemOS?style=flat-square&logo=github) |
| 2026.01 | [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553) | AIMing Lab | arXiv | [aiming-lab/SimpleMem](https://github.com/aiming-lab/SimpleMem) <br> ![Stars](https://img.shields.io/github/stars/aiming-lab/SimpleMem?style=flat-square&logo=github) |
| 2025.10 | [LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866) | ZJUNLP | ICLR 2026 | [zjunlp/LightMem](https://github.com/zjunlp/LightMem) <br> ![Stars](https://img.shields.io/github/stars/zjunlp/LightMem?style=flat-square&logo=github) |
| 2025.06 | [Memory OS of AI Agent](https://arxiv.org/abs/2506.06326) | MemoryOS Team | EMNLP 2025 | - |
| 2025.04 | [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | Mem0 | arXiv | [mem0ai/mem0](https://github.com/mem0ai/mem0) <br> ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&logo=github) |
| 2025.02 | [A-Mem: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | Rutgers University | arXiv | [agiresearch/A-mem](https://github.com/agiresearch/A-mem) <br> ![Stars](https://img.shields.io/github/stars/agiresearch/A-mem?style=flat-square&logo=github) |
| 2023.11 | [Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory](https://arxiv.org/abs/2311.08719) | Alibaba Group | arXiv | - |
| 2023.10 | [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | UC Berkeley | arXiv | [letta-ai/letta](https://github.com/letta-ai/letta) <br> ![Stars](https://img.shields.io/github/stars/letta-ai/letta?style=flat-square&logo=github) |


### Personalized Memory Architectures

| Date | Paper Title | Venue | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.05 | [Personal Visual Memory from Explicit and Implicit Evidence](https://arxiv.org/abs/2605.28806) | Johns Hopkins University / University of Wisconsin-Madison / Adobe Research | arXiv | [viettmab/VisualMem](https://github.com/viettmab/VisualMem) <br> ![Stars](https://img.shields.io/github/stars/viettmab/VisualMem?style=flat-square&logo=github) |
| 2026.04 | [EgoSelf: From Memory to Personalized Egocentric Assistant](https://arxiv.org/abs/2604.19564) | Peking University / The Hong Kong Polytechnic University | arXiv | [Project Page](https://abie-e.github.io/egoself_project/) |
| 2026.04 | [Learning to Forget -- Hierarchical Episodic Memory for Lifelong Robot Deployment](https://arxiv.org/abs/2604.11306) | Karlsruhe Institute of Technology | arXiv | - |
| 2026.03 | [PersonaVLM: Long-Term Personalized Multimodal LLMs](https://github.com/MiG-NJU/PersonaVLM) | Nanjing University | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) <br> ![Stars](https://img.shields.io/github/stars/MiG-NJU/PersonaVLM?style=flat-square&logo=github) |
| 2026.01 | [Inside Out: Evolving User-Centric Core Memory Trees for Long-Term Personalized Dialogue Systems](https://arxiv.org/abs/2601.05171) | Renmin University of China / MemTensor / IAAR-Shanghai / Beihang University / Nankai University | arXiv | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) <br> ![Stars](https://img.shields.io/github/stars/MemTensor/MemOS?style=flat-square&logo=github) |
| 2025.12 | [MemVerse: Multimodal Memory for Lifelong Learning Agents](https://arxiv.org/abs/2512.03627) | Shanghai AI Laboratory | arXiv | [KnowledgeXLab/MemVerse](https://github.com/KnowledgeXLab/MemVerse) <br> ![Stars](https://img.shields.io/github/stars/KnowledgeXLab/MemVerse?style=flat-square&logo=github) |
| 2025.11 | [Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction](https://arxiv.org/abs/2511.13410) | Renmin University of China / Taobao & Tmall Group of Alibaba | AAAI 2026 | - |
| 2025.08 | [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) | ByteDance Seed | ICLR 2026 | [ByteDance-Seed/m3-agent](https://github.com/ByteDance-Seed/m3-agent) <br> ![Stars](https://img.shields.io/github/stars/ByteDance-Seed/m3-agent?style=flat-square&logo=github) |
| 2025.07 | [MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957) | MIRIX AI | arXiv | [Mirix-AI/MIRIX](https://github.com/Mirix-AI/MIRIX) <br> ![Stars](https://img.shields.io/github/stars/Mirix-AI/MIRIX?style=flat-square&logo=github) |
| 2025.02 | [USER-VLM 360: Personalized Vision Language Models with User-aware Tuning for Social Human-Robot Interactions](https://arxiv.org/abs/2502.10636) | Sorbonne University / International University of Rabat | ICMI 2025 | - |
| 2024.11 | [MC-LLaVA: Multi-Concept Personalized Vision-Language Model](https://arxiv.org/abs/2411.11706) | Shanghai AI Laboratory / CUHK / University of Sydney / Tsinghua University | arXiv | [arctanxarc/MC-LLaVA](https://github.com/arctanxarc/MC-LLaVA) <br> ![Stars](https://img.shields.io/github/stars/arctanxarc/MC-LLaVA?style=flat-square&logo=github) |
| 2024.06 | [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://arxiv.org/abs/2406.09400) | University of Wisconsin-Madison / UC Berkeley | NeurIPS 2024 | [WisconsinAIVision/YoLLaVA](https://github.com/WisconsinAIVision/YoLLaVA) <br> ![Stars](https://img.shields.io/github/stars/WisconsinAIVision/YoLLaVA?style=flat-square&logo=github) |
| 2024.03 | [MyVLM: Personalizing VLMs for User-Specific Queries](https://arxiv.org/abs/2403.14599) | Snap Research / Tel Aviv University | ECCV 2024 | [snap-research/MyVLM](https://github.com/snap-research/MyVLM) <br> ![Stars](https://img.shields.io/github/stars/snap-research/MyVLM?style=flat-square&logo=github) |


### Latent Memory Mechanisms

| Date | Paper Title | Venue | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.05 | [$\delta$-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/abs/2605.12357) | SUTD / DeCLaRe Lab | arXiv | [declare-lab/delta-Mem](https://github.com/declare-lab/delta-Mem) <br> ![Stars](https://img.shields.io/github/stars/declare-lab/delta-Mem?style=flat-square&logo=github) |
| 2026.02 | [Locas: Your Models are Principled Initializers of Locally-Supported Parametric Memories](https://arxiv.org/abs/2602.05085) | Tencent | arXiv | - |
| 2026.01 | [FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse](https://arxiv.org/abs/2601.05505) | Beihang University | arXiv | - |
| 2025.09 | [MemGen: Weaving Generative Latent Memory for Self-Evolving Agents](https://arxiv.org/abs/2509.24704) | National University of Singapore | ICLR 2026 | [KANABOON1/MemGen](https://github.com/KANABOON1/MemGen) <br> ![Stars](https://img.shields.io/github/stars/KANABOON1/MemGen?style=flat-square&logo=github) |
| 2025.03 | [AI-native Memory 2.0: Second Me](https://arxiv.org/abs/2503.08102) | Mindverse AI | arXiv | [Mindverse/Second-Me](https://github.com/Mindverse/Second-Me) <br> ![Stars](https://img.shields.io/github/stars/Mindverse/Second-Me?style=flat-square&logo=github) |
| 2025.02 | [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://arxiv.org/abs/2502.00592) | UC San Diego / MIT-IBM Watson AI Lab / IBM Research / Amazon | ICML 2025 | [wangyu-ustc/MemoryLLM](https://github.com/wangyu-ustc/MemoryLLM) <br> ![Stars](https://img.shields.io/github/stars/wangyu-ustc/MemoryLLM?style=flat-square&logo=github) |
| 2024.06 | [AI-native Memory: A Pathway from LLMs Towards AGI](https://arxiv.org/abs/2406.18312) | Mindverse AI | arXiv | - |
| 2024.02 | [MEMORYLLM: Towards Self-Updatable Large Language Models](https://arxiv.org/abs/2402.04624) | UC San Diego / Amazon / UCLA | ICML 2024 | [wangyu-ustc/MemoryLLM](https://github.com/wangyu-ustc/MemoryLLM) <br> ![Stars](https://img.shields.io/github/stars/wangyu-ustc/MemoryLLM?style=flat-square&logo=github) |
| 2023.04 | [Scaling Transformer to 1M tokens and beyond with RMT](https://arxiv.org/abs/2304.11062) | MIPT / AIRI / London Institute for Mathematical Sciences | AAAI 2024 | [booydar/recurrent-memory-transformer](https://github.com/booydar/recurrent-memory-transformer) <br> ![Stars](https://img.shields.io/github/stars/booydar/recurrent-memory-transformer?style=flat-square&logo=github) |

<br>

## 🎯 Personalized Alignment

> ![#7a4ef3](https://img.shields.io/badge/-_#7a4ef3-7a4ef3?style=flat-square) *How can a model adapt to individual preferences, personalities, and contexts?*

| Date | Paper Title | Venue | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.06 | [TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment](https://arxiv.org/abs/2606.01755) | Monash University | arXiv | - |
| 2026.06 | [Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization](https://arxiv.org/abs/2606.02300) | Fudan University / Shanghai Innovation Institute / OPPO | arXiv | - |
| 2026.05 | [MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models](https://arxiv.org/abs/2605.25342) | Monash University / Defence Science and Technology Group Australia | arXiv | - |
| 2026.04 | [Hierarchical Multi-Persona Induction from User Behavioral Logs: Learning Evidence-Grounded and Truthful Personas](https://arxiv.org/abs/2604.26120) | Emory University / Naver Corporation | arXiv | - |
| 2026.04 | [Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization](https://arxiv.org/abs/2604.22345) | McGill University / Mila / MBZUAI / Salesforce | arXiv | - |
| 2026.04 | [Beyond Static Personas: Situational Personality Steering for Large Language Models](https://arxiv.org/abs/2604.13846) | Singapore Management University | arXiv | - |
| 2026.03 | [PersonaVLM: Long-Term Personalized Multimodal LLMs](https://github.com/MiG-NJU/PersonaVLM) | Nanjing University | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) <br> ![Stars](https://img.shields.io/github/stars/MiG-NJU/PersonaVLM?style=flat-square&logo=github) |
| 2026.02 | [Learning Personalized Agents from Human Feedback](https://arxiv.org/abs/2602.16173) | Meta Superintelligence Labs / Princeton University / Duke University | arXiv | [facebookresearch/PAHF](https://github.com/facebookresearch/PAHF) <br> ![Stars](https://img.shields.io/github/stars/facebookresearch/PAHF?style=flat-square&logo=github) |
| 2025.10 | [CoPL: Collaborative Preference Learning for Personalizing LLMs](https://arxiv.org/abs/2510.09239) | Alibaba Group / Nanyang Technological University | AAAI 2026 | - |
| 2025.10 | [POPI: Personalizing LLMs via Optimized Natural Language Preference Inference](https://arxiv.org/abs/2510.17881) | UIUC / Amazon / University of Notre Dame | arXiv | - |
| 2025.10 | [Preference-Aware Memory Update for Long-Term LLM Agents](https://arxiv.org/abs/2510.09720) | Hong Kong Polytechnic University | arXiv | - |
| 2025.10 | [PrefDisco: Benchmarking Proactive Personalized Reasoning](https://arxiv.org/abs/2510.00177) | University of Washington / Allen Institute for AI | ICLR 2026 | [stellalisy/PrefDisco](https://github.com/stellalisy/PrefDisco) <br> ![Stars](https://img.shields.io/github/stars/stellalisy/PrefDisco?style=flat-square&logo=github) |
| 2025.08 | [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://arxiv.org/abs/2508.12521) | Salesforce AI Research / Cohere Labs / University of Maryland / CMU | arXiv | - |
| 2025.08 | [Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History](https://arxiv.org/abs/2508.04826) | Mila / Universite de Montreal / CHU Sainte-Justine / Tara Research | AAAI 2026 | [tosatot/PERSIST](https://github.com/tosatot/PERSIST) <br> ![Stars](https://img.shields.io/github/stars/tosatot/PERSIST?style=flat-square&logo=github) |
| 2025.05 | [Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment](https://arxiv.org/abs/2505.15456) | Harbin Institute of Technology / Du Xiaoman Financial | NeurIPS 2025 | [XingYuSSS/RLPA](https://github.com/XingYuSSS/RLPA) <br> ![Stars](https://img.shields.io/github/stars/XingYuSSS/RLPA?style=flat-square&logo=github) |
| 2025.03 | [ALIGNX: From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment](https://arxiv.org/abs/2503.15463) | Renmin University of China / Ant Group | ACL 2026 | [JinaLeejnl/AlignX](https://github.com/JinaLeejnl/AlignX) <br> ![Stars](https://img.shields.io/github/stars/JinaLeejnl/AlignX?style=flat-square&logo=github) |
| 2024.12 | [PersonalLLM: Tailoring LLMs to Individual Preferences](https://openreview.net/forum?id=65GT1a9fwF) | Singapore Management University / Amazon | ICLR 2025 | - |
| 2024.10 | [Aligning LLMs with Individual Preferences via Interaction](https://aclanthology.org/2025.coling-main.511/) | UIUC / USC | COLING 2025 | [ShujinWu-0814/ALOE](https://github.com/ShujinWu-0814/ALOE) <br> ![Stars](https://img.shields.io/github/stars/ShujinWu-0814/ALOE?style=flat-square&logo=github) |
| 2024.08 | [Personality Alignment of Large Language Models](https://arxiv.org/abs/2408.11779) | Zhejiang University / Westlake University / UCL / Huawei Noah's Ark Lab | ICLR 2025 | [zhu-minjun/PAlign](https://github.com/zhu-minjun/PAlign) <br> ![Stars](https://img.shields.io/github/stars/zhu-minjun/PAlign?style=flat-square&logo=github) |
| 2024.06 | [Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://arxiv.org/abs/2406.10471) | University of Notre Dame | EMNLP 2024 | [TamSiuhin/Per-Pcs](https://github.com/TamSiuhin/Per-Pcs) <br> ![Stars](https://img.shields.io/github/stars/TamSiuhin/Per-Pcs?style=flat-square&logo=github) |
| 2023.10 | [Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging](https://arxiv.org/abs/2310.11564) | University of Washington / Allen Institute for AI / KAIST AI / UC San Diego | arXiv | [joeljang/RLPHF](https://github.com/joeljang/RLPHF) <br> ![Stars](https://img.shields.io/github/stars/joeljang/RLPHF?style=flat-square&logo=github) |

<br>

## 🔍 Personalized Retrieval

> ![#0b6b92](https://img.shields.io/badge/-_#0b6b92-0b6b92?style=flat-square) *How should systems select the right user context, memory, and evidence?*

| Date | Paper Title | Venue | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.05 | [MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval](https://arxiv.org/abs/2605.06132) | MemTensor / China Telecom / Shanghai Jiao Tong University | arXiv | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) <br> ![Stars](https://img.shields.io/github/stars/MemTensor/MemOS?style=flat-square&logo=github) |
| 2026.05 | [An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration](https://arxiv.org/abs/2605.03989) | Macao Polytechnic University | arXiv | - |
| 2026.05 | [From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG](https://arxiv.org/abs/2605.18271) | UNIST | ICML 2026 | [UbiquitousAILab/EPIC](https://github.com/UbiquitousAILab/EPIC) <br> ![Stars](https://img.shields.io/github/stars/UbiquitousAILab/EPIC?style=flat-square&logo=github) |
| 2026.04 | [Response-Aware User Memory Selection for LLM Personalization](https://arxiv.org/abs/2604.14473) | University of Washington / Microsoft Research | arXiv | - |
| 2026.02 | [Mnemis: Dual-Route Retrieval on Hierarchical Graphs for Long-Term LLM Memory](https://arxiv.org/abs/2602.15313) | Microsoft | ACL 2026 | [microsoft/Mnemis](https://github.com/microsoft/Mnemis) <br> ![Stars](https://img.shields.io/github/stars/microsoft/Mnemis?style=flat-square&logo=github) |
| 2025.10 | [ClusterRAG: Cluster-Based Collaborative Filtering for Personalized Retrieval-Augmented Generation](https://arxiv.org/abs/2510.15666) | University of Science and Technology of China | arXiv | - |
| 2025.09 | [PrLM: Learning Explicit Reasoning for Personalized RAG via Contrastive Reward Optimization](https://arxiv.org/abs/2509.18056) | Renmin University of China / Ant Group | arXiv | - |
| 2025.03 | [In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://arxiv.org/abs/2503.08026) | Arizona State University / Google Cloud AI Research / UNC Chapel Hill | ACL 2025 | - |
| 2025.01 | [SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents](https://arxiv.org/abs/2501.05065) | University of Edinburgh / Huawei | ICLR 2025 | - |
| 2025.01 | [Personalized Graph-Based Retrieval for Large Language Models (PGraphRAG)](https://arxiv.org/abs/2501.02157) | UC Santa Cruz / Meta AI / Adobe Research / University of Oregon / USC / Cisco AI Research | arXiv | [PGraphRAG-benchmark/PGraphRAG](https://github.com/PGraphRAG-benchmark/PGraphRAG) <br> ![Stars](https://img.shields.io/github/stars/PGraphRAG-benchmark/PGraphRAG?style=flat-square&logo=github) |
| 2024.11 | [Pearl: Personalizing Large Language Model Writing Assistants with Generation-Calibrated Retrievers](https://aclanthology.org/2024.customnlp4u-1.16/) | Microsoft / Purdue | CustomNLP4U 2024 | - |
| 2024.10 | [RAP: Retrieval-Augmented Personalization for Multimodal Large Language Models](https://arxiv.org/abs/2410.13360) | Westlake University / Zhejiang University | CVPR 2025 | [Hoar012/RAP-MLLM](https://github.com/Hoar012/RAP-MLLM) <br> ![Stars](https://img.shields.io/github/stars/Hoar012/RAP-MLLM?style=flat-square&logo=github) |
| 2024.10 | [Retrieval Augmented Generation with Collaborative Filtering for Personalized Text Generation](https://arxiv.org/abs/2410.05185) | University of Waterloo | arXiv | - |
| 2024.09 | [Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs (EMG-RAG)](https://arxiv.org/abs/2409.19401) | Huawei | EMNLP 2024 | - |
| 2024.07 | [PersonaRAG: Enhancing Retrieval-Augmented Generation Systems with User-Centric Agents](https://arxiv.org/abs/2407.09394) | University of Passau | SIGIR-AP 2024 | [padas-lab-de/ir-rag-sigir24-persona-rag](https://github.com/padas-lab-de/ir-rag-sigir24-persona-rag) <br> ![Stars](https://img.shields.io/github/stars/padas-lab-de/ir-rag-sigir24-persona-rag?style=flat-square&logo=github) |
| 2024.07 | [MeMemo: On-device Retrieval Augmentation for Private and Personalized Text Generation](https://arxiv.org/abs/2407.01972) | Georgia Tech | SIGIR 2024 | [poloclub/mememo](https://github.com/poloclub/mememo) <br> ![Stars](https://img.shields.io/github/stars/poloclub/mememo?style=flat-square&logo=github) |
| 2024.01 | [UniMS-RAG: A Unified Multi-source Retrieval-Augmented Generation for Personalized Dialogue Systems](https://arxiv.org/abs/2401.13256) | CUHK / University of Edinburgh | arXiv | - |
| 2023.12 | [Learning Retrieval Augmentation for Personalized Dialogue Generation (LAPDOG)](https://arxiv.org/abs/2406.18847) | University of Surrey / SUSTech / ByteDance | EMNLP 2023 | [hqsiswiliam/LAPDOG](https://github.com/hqsiswiliam/LAPDOG) <br> ![Stars](https://img.shields.io/github/stars/hqsiswiliam/LAPDOG?style=flat-square&logo=github) |
| 2023.07 | [Personalized Retrieval over Millions of Items (XPERT)](https://www.microsoft.com/en-us/research/publication/personalized-retrieval-over-millions-of-items/) | Microsoft Research | SIGIR 2023 | [personalizedretrieval/xpert](https://github.com/personalizedretrieval/xpert) <br> ![Stars](https://img.shields.io/github/stars/personalizedretrieval/xpert?style=flat-square&logo=github) |
| 2023.07 | [PersonalTM: Transformer Memory for Personalized Retrieval](https://www.amazon.science/publications/personaltm-transformer-memory-for-personalized-retrieval) | Amazon | SIGIR 2023 | - |
| 2023.04 | [A Personalized Dense Retrieval Framework for Unified Information Access](https://arxiv.org/abs/2304.13654) | UMass Amherst / Lowe's | SIGIR 2023 | [HansiZeng/UIAA](https://github.com/HansiZeng/UIAA) <br> ![Stars](https://img.shields.io/github/stars/HansiZeng/UIAA?style=flat-square&logo=github) |

<br>

## 📊 Personalized Evaluation

> ![#b45a00](https://img.shields.io/badge/-_#b45a00-b45a00?style=flat-square) *How do we evaluate long-term, dynamic, implicit, and multimodal personalization?*

| Date | Paper Title | Venue | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.05 | [Preference-Aware Rubric Learning for Personalized Evaluation (PARL)](https://arxiv.org/abs/2605.31545) | National University of Singapore / Xiaohongshu / University of Tokyo | arXiv | [SnowCharmQ/PARL](https://github.com/SnowCharmQ/PARL) <br> ![Stars](https://img.shields.io/github/stars/SnowCharmQ/PARL?style=flat-square&logo=github) |
| 2026.05 | [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](https://arxiv.org/abs/2605.29341) | UC Santa Barbara / J.P. Morgan AI Research / ETH Zurich / Stanford University / Johns Hopkins University / CMU | arXiv | [Project Page](https://worldmemarena-mem.github.io/) |
| 2026.05 | [Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents (PerMemBench)](https://arxiv.org/abs/2605.25535) | KAIST | arXiv | [yeonjun-in/PerMemBench](https://github.com/yeonjun-in/PerMemBench) <br> ![Stars](https://img.shields.io/github/stars/yeonjun-in/PerMemBench?style=flat-square&logo=github) |
| 2026.05 | [MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](https://arxiv.org/abs/2605.25007) | Swinburne University of Technology / Southeast University / Tongji University | arXiv | - |
| 2026.05 | [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493) | UCLA NLP | arXiv | [Hugging Face Dataset](https://huggingface.co/datasets/xiaowu0162/longmemeval-v2) |
| 2026.05 | [Omni-Persona: Systematic Benchmarking and Improving Omnimodal Personalization](https://arxiv.org/abs/2605.09996) | Seoul National University | arXiv | - |
| 2026.05 | [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527) | Wuhan University / The Chinese University of Hong Kong / HKUST | arXiv | - |
| 2026.04 | [From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents](https://arxiv.org/abs/2604.20006) | Arizona State University | arXiv | - |
| 2026.04 | [Personalized Benchmarking: Evaluating LLMs by Individual Preferences](https://arxiv.org/abs/2604.18943) | University of Chicago | Findings of ACL 2026 | - |
| 2026.04 | [CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors](https://arxiv.org/abs/2604.14773) | East China Normal University | arXiv | [bjzgcai/CoPA](https://github.com/bjzgcai/CoPA) <br> ![Stars](https://img.shields.io/github/stars/bjzgcai/CoPA?style=flat-square&logo=github) |
| 2026.04 | [Trust Your Memory: Verifiable Control of Smart Homes through Reinforcement Learning with Multi-dimensional Rewards](https://arxiv.org/abs/2604.10110) | AI Research Center, Midea Group | arXiv | - |
| 2026.03 | [Persona-MME from PersonaVLM: Long-Term Personalized Multimodal LLMs](https://github.com/MiG-NJU/PersonaVLM) | Nanjing University | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) <br> ![Stars](https://img.shields.io/github/stars/MiG-NJU/PersonaVLM?style=flat-square&logo=github) |
| 2026.03 | [AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment](https://arxiv.org/abs/2603.26680) | University of Science and Technology of China | arXiv | [ThisIsCosine/AlpsBench](https://github.com/ThisIsCosine/AlpsBench) <br> ![Stars](https://img.shields.io/github/stars/ThisIsCosine/AlpsBench?style=flat-square&logo=github) |
| 2026.03 | [MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization](https://arxiv.org/abs/2603.25973) | University of Illinois Chicago | Lifelong Agent @ ICLR 2026 | [AgentMemoryWorld/MemoryCD](https://github.com/AgentMemoryWorld/MemoryCD) <br> ![Stars](https://img.shields.io/github/stars/AgentMemoryWorld/MemoryCD?style=flat-square&logo=github) |
| 2026.03 | [LMEB: Long-horizon Memory Embedding Benchmark](https://arxiv.org/abs/2603.12572) | Harbin Institute of Technology / KaLM-Embedding | arXiv | [KaLM-Embedding/LMEB](https://github.com/KaLM-Embedding/LMEB) <br> ![Stars](https://img.shields.io/github/stars/KaLM-Embedding/LMEB?style=flat-square&logo=github) |
| 2026.03 | [LifeBench: A Benchmark for Long-Horizon Multi-Source Memory](https://arxiv.org/abs/2603.03781) | Nanjing University / Huawei Technologies | arXiv | [1754955896/LifeBench](https://github.com/1754955896/LifeBench) <br> ![Stars](https://img.shields.io/github/stars/1754955896/LifeBench?style=flat-square&logo=github) |
| 2026.03 | [According to Me: Long-Term Personalized Referential Memory QA](https://arxiv.org/abs/2603.01990) | University of Cambridge / Independent Researcher | arXiv | [JingbiaoMei/ATM-Bench](https://github.com/JingbiaoMei/ATM-Bench) <br> ![Stars](https://img.shields.io/github/stars/JingbiaoMei/ATM-Bench?style=flat-square&logo=github) |
| 2026.02 | [ES-MemEval: Benchmarking Conversational Agents on Personalized Long-Term Emotional Support](https://arxiv.org/abs/2602.01885) | Tongji University | WWW 2026 | [slptongji/ES-MemEval](https://github.com/slptongji/ES-MemEval) <br> ![Stars](https://img.shields.io/github/stars/slptongji/ES-MemEval?style=flat-square&logo=github) |
| 2026.01 | [KnowMe-Bench: Benchmarking Person Understanding for Lifelong Digital Companions](https://arxiv.org/abs/2601.04745) | UCAS | arXiv | [QuantaAlpha/KnowMeBench](https://github.com/QuantaAlpha/KnowMeBench) <br> ![Stars](https://img.shields.io/github/stars/QuantaAlpha/KnowMeBench?style=flat-square&logo=github) |
| 2025.12 | [PERSONAMEM-V2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/abs/2512.06688) | University of Pennsylvania | arXiv | [bowen-upenn/PersonaMem-v2](https://github.com/bowen-upenn/PersonaMem-v2) <br> ![Stars](https://img.shields.io/github/stars/bowen-upenn/PersonaMem-v2?style=flat-square&logo=github) |
| 2025.06 | [PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization](https://arxiv.org/abs/2506.12915) | UESTC / OPPO | arXiv | - |
| 2025.06 | [LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://arxiv.org/abs/2506.00137) | UMass Amherst | EMNLP 2025 | [LaMP-Benchmark/LaMP-QA](https://github.com/LaMP-Benchmark/LaMP-QA) <br> ![Stars](https://img.shields.io/github/stars/LaMP-Benchmark/LaMP-QA?style=flat-square&logo=github) |
| 2025.04 | [Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale (PERSONAMEM)](https://arxiv.org/abs/2504.14225) | University of Pennsylvania | COLM 2025 | [bowen-upenn/PersonaMem](https://github.com/bowen-upenn/PersonaMem) <br> ![Stars](https://img.shields.io/github/stars/bowen-upenn/PersonaMem?style=flat-square&logo=github) |
| 2024.10 | [LONGMEMEVAL: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) | UCLA / Tencent AI Lab | ICLR 2025 | [xiaowu0162/LongMemEval](https://github.com/xiaowu0162/LongMemEval) <br> ![Stars](https://img.shields.io/github/stars/xiaowu0162/LongMemEval?style=flat-square&logo=github) |
| 2024.07 | [LongLaMP: A Benchmark for Personalized Long-form Text Generation](https://arxiv.org/abs/2407.11016) | Adobe Research / UMass Amherst / University of Oregon | arXiv | [Hugging Face Dataset](https://huggingface.co/datasets/LongLaMP/LongLaMP) |
| 2024.02 | [Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)](https://arxiv.org/abs/2402.17753) | UNC Chapel Hill / Snap Inc. | ACL 2024 | [snap-research/locomo](https://github.com/snap-research/locomo) <br> ![Stars](https://img.shields.io/github/stars/snap-research/locomo?style=flat-square&logo=github) |
| 2023.04 | [LaMP: When Large Language Models Meet Personalization](https://arxiv.org/abs/2304.11406) | UMass Amherst / Google Research | ACL 2024 | [LaMP-Benchmark/LaMP](https://github.com/LaMP-Benchmark/LaMP) <br> ![Stars](https://img.shields.io/github/stars/LaMP-Benchmark/LaMP?style=flat-square&logo=github) |

<br>

## 📝 Notes

If we missed any relevant work, please feel free to open an issue to contact us.

<br>

## ✒️ Citation

If this list is useful, please consider citing or starring the repository after publication.
