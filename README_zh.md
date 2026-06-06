<p align="center">
  <img src="./assets/title.png" alt="Awesome Personalization in MLLMs" width="720">
</p>

# Awesome Personalization in MLLMs

> 面向个性化 LLM 和 MLLM 的系统性调研与前沿进展整理，覆盖 <span style="color:#0f9f8f"><b>个性化记忆</b></span>、<span style="color:#7a4ef3"><b>对齐</b></span>、<span style="color:#0b6b92"><b>检索</b></span>和<span style="color:#b45a00"><b>评估</b></span>。

[English README](./README.md) | [在线主页](https://clare-nie.github.io/Awesome-Personalization-in-MLLMs/)

## Overview

个性化 LLM / MLLM 的目标，不只是让模型对“平均用户”表现更好，而是让模型理解一个具体用户：长期目标、动态偏好、隐式 persona、多模态上下文，以及什么时候应该使用个性化信息、什么时候不应该使用。

本仓库主要整理四个方向的论文、系统、数据集和 benchmark：

| 方向 | 核心问题 |
| :--- | :--- |
| **个性化记忆** | agent 应该存什么、更新什么、检索什么、压缩什么、遗忘什么？ |
| **个性化对齐** | 模型如何适配个体偏好、人格和上下文？ |
| **个性化检索** | 系统如何选择正确的用户上下文、记忆和证据？ |
| **Benchmark 与评估** | 如何评测长期、动态、隐式、多模态的个性化能力？ |

## Table of Contents

- [Overview](#overview)
- [个性化记忆](#个性化记忆)
- [个性化对齐](#个性化对齐)
- [个性化检索](#个性化检索)
- [Benchmark 与评估](#benchmark-与评估)
- [贡献](#贡献)

## 个性化记忆

### 基于记忆架构

| 时间 / 论文 | Paper Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2023.10 / [arXiv](https://arxiv.org/abs/2310.08560) | MemGPT: Towards LLMs as Operating Systems | arXiv | [letta-ai/letta](https://github.com/letta-ai/letta) / 23,168 stars |
| 2025.02 / [arXiv](https://arxiv.org/abs/2502.12110) | A-Mem: Agentic Memory for LLM Agents | arXiv | [agiresearch/A-mem](https://github.com/agiresearch/A-mem) / 1,036 stars |
| 2025.04 / [arXiv](https://arxiv.org/abs/2504.19413) | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | arXiv | [mem0ai/mem0](https://github.com/mem0ai/mem0) / 57,857 stars |
| 2025.05 | Memory OS of AI Agent | arXiv | - |
| 2025.10 | LightMem: Lightweight and Efficient Memory-Augmented Generation | ICLR 2026 | [zjunlp/LightMem](https://github.com/zjunlp/LightMem) / 907 stars |

### 个性化记忆架构

| 时间 / 论文 | Paper Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2025.07 | MIRIX: Multi-Agent Memory System for LLM-Based Agents | arXiv | [Mirix-AI/MIRIX](https://github.com/Mirix-AI/MIRIX) / stars pending |
| 2025.08 | M3-Agent: A Multimodal Agent with Long-Term Memory | arXiv | [ByteDance-Seed/m3-agent](https://github.com/ByteDance-Seed/m3-agent) / stars pending |
| 2025.12 | MemVerse: Multimodal Memory for Lifelong Learning Agents | arXiv | - |
| 2026.03 | PersonaVLM: Long-Term Personalized Multimodal LLMs | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) / stars pending |

### Latent Memory 机制

| 时间 / 论文 | Paper Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2023.04 / [arXiv](https://arxiv.org/abs/2304.11062) | Scaling Transformer to 1M tokens and beyond with RMT | AAAI 2024 | - |
| 2024.06 / [arXiv](https://arxiv.org/abs/2406.18312) | AI-native Memory: A Pathway from LLMs Towards AGI | arXiv | - |
| 2025.02 / [arXiv](https://arxiv.org/abs/2502.00592) | M+: Extending MemoryLLM with Scalable Long-Term Memory | ICML 2025 | - |
| 2025.03 / [arXiv](https://arxiv.org/abs/2503.08102) | AI-native Memory 2.0: Second Me | arXiv | - |
| 2025.09 | MemGen: Weaving Generative Latent Memory for Self-Evolving Agents | ICLR 2026 | - |

## 个性化对齐

| 时间 / 论文 | Paper Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2024.10 | Aligning LLMs with Individual Preferences via Interaction | arXiv | - |
| 2025.03 | ALIGNX: From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment | arXiv | - |
| 2025.05 | Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment | arXiv | - |
| 2025.08 | Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History | arXiv | - |
| 2025.09 | Personalized Reasoning / PrefDisco | ICLR 2026 | - |
| 2025.10 | Preference-Aware Memory Update for Long-Term LLM Agents | arXiv | - |
| 2026.03 | PersonaVLM: Long-Term Personalized Multimodal LLMs | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) / stars pending |

## 个性化检索

| 时间 / 论文 | Paper Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2023.10 / [arXiv](https://arxiv.org/abs/2310.08560) | MemGPT: Towards LLMs as Operating Systems | arXiv | [letta-ai/letta](https://github.com/letta-ai/letta) / 23,168 stars |
| 2025.04 / [arXiv](https://arxiv.org/abs/2504.19413) | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | arXiv | [mem0ai/mem0](https://github.com/mem0ai/mem0) / 57,857 stars |
| 2025.10 | LightMem: Lightweight and Efficient Memory-Augmented Generation | ICLR 2026 | [zjunlp/LightMem](https://github.com/zjunlp/LightMem) / 907 stars |
| 2026.05 | Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents | arXiv | - |

## Benchmark 与评估

| 时间 / 论文 | Paper Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2023.04 | LaMP: When Large Language Models Meet Personalization | arXiv | - |
| 2024.02 | Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo) | arXiv | - |
| 2024.10 | LONGMEMEVAL: Benchmarking Chat Assistants on Long-Term Interactive Memory | ICLR 2025 | - |
| 2025.04 | Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale (PERSONAMEM) | COLM 2025 | - |
| 2025.06 | PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization | arXiv | - |
| 2025.12 | PERSONAMEM-V2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory | arXiv | - |
| 2026.03 | Persona-MME from PersonaVLM: Long-Term Personalized Multimodal LLMs | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) / stars pending |
| 2026.05 | Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents (PerMemBench) | arXiv | - |

## Notes

GitHub star 数量在更新仓库时手动确认。部分条目标记为 `stars pending`，表示当前 GitHub API rate limit 导致无法实时确认。

## 贡献

欢迎补充论文、代码、benchmark、数据集和简短说明。请参考 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 引用

如果这个列表对你有帮助，欢迎在仓库发布后 star 或引用。

## License

本仓库采用 MIT License。
