<p align="center">
  <img src="./assets/title.png" alt="Awesome Personalization in MLLMs" width="720">
</p>

# Awesome Personalization in MLLMs

> The most comprehensive survey and frontier tracking repository for personalized LLMs and MLLMs, covering <span style="color:#0f9f8f"><b>personalized memory</b></span>, <span style="color:#7a4ef3"><b>alignment</b></span>, <span style="color:#0b6b92"><b>retrieval</b></span>, and <span style="color:#b45a00"><b>evaluation</b></span>.

[中文 README](./README_zh.md) | [Project Page](https://clare-nie.github.io/Awesome-Personalization-in-MLLMs/)

## Overview

Personalized LLMs and MLLMs aim to move beyond one-size-fits-all assistants. Instead of only optimizing for average human preference, they need to model a specific user: long-term goals, evolving preferences, implicit personas, multimodal context, and when personalization should or should not be applied.

This repository tracks papers, benchmarks, datasets, and systems around four connected research directions:

| Direction | Core Question |
| :--- | :--- |
| **Personalized Memory** | What should an agent store, update, retrieve, compress, and forget? |
| **Personalized Alignment** | How can a model adapt to individual preferences, personalities, and contexts? |
| **Personalized Retrieval** | How should systems select the right user context, memory, and evidence? |
| **Benchmarks and Evaluation** | How do we evaluate long-term, dynamic, implicit, and multimodal personalization? |

## Table of Contents

- [Overview](#overview)
- [Personalized Memory](#personalized-memory)
- [Personalized Alignment](#personalized-alignment)
- [Personalized Retrieval](#personalized-retrieval)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Contributing](#contributing)

## Personalized Memory

### Memory Architectures

| Date | Paper Title | Venue / Source | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2025.10 | [LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866) | ZJUNLP | ICLR 2026 | [zjunlp/LightMem](https://github.com/zjunlp/LightMem) <br> ![Stars](https://img.shields.io/github/stars/zjunlp/LightMem?style=flat-square&logo=github) |
| 2025.06 | [Memory OS of AI Agent](https://arxiv.org/abs/2506.06326) | MemoryOS Team | EMNLP 2025 | - |
| 2025.04 | [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | Mem0 | arXiv | [mem0ai/mem0](https://github.com/mem0ai/mem0) <br> ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&logo=github) |
| 2025.02 | [A-Mem: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | Rutgers University | arXiv | [agiresearch/A-mem](https://github.com/agiresearch/A-mem) <br> ![Stars](https://img.shields.io/github/stars/agiresearch/A-mem?style=flat-square&logo=github) |
| 2023.10 | [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | UC Berkeley | arXiv | [letta-ai/letta](https://github.com/letta-ai/letta) <br> ![Stars](https://img.shields.io/github/stars/letta-ai/letta?style=flat-square&logo=github) |


### Personalized Memory Architectures

| Date | Paper Title | Venue / Source | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.03 | [PersonaVLM: Long-Term Personalized Multimodal LLMs](https://github.com/MiG-NJU/PersonaVLM) | Nanjing University | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) <br> ![Stars](https://img.shields.io/github/stars/MiG-NJU/PersonaVLM?style=flat-square&logo=github) |
| 2025.12 | [MemVerse: Multimodal Memory for Lifelong Learning Agents](https://arxiv.org/abs/2512.03627) | - | arXiv | - |
| 2025.08 | [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) | ByteDance Seed | ICLR 2026 | [ByteDance-Seed/m3-agent](https://github.com/ByteDance-Seed/m3-agent) <br> ![Stars](https://img.shields.io/github/stars/ByteDance-Seed/m3-agent?style=flat-square&logo=github) |
| 2025.07 | [MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957) | MIRIX AI | arXiv | [Mirix-AI/MIRIX](https://github.com/Mirix-AI/MIRIX) <br> ![Stars](https://img.shields.io/github/stars/Mirix-AI/MIRIX?style=flat-square&logo=github) |


### Latent Memory Mechanisms

| Date | Paper Title | Venue / Source | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2025.09 | MemGen: Weaving Generative Latent Memory for Self-Evolving Agents | - | ICLR 2026 | - |
| 2025.03 | [AI-native Memory 2.0: Second Me](https://arxiv.org/abs/2503.08102) | Second Me Team | arXiv | - |
| 2025.02 | [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://arxiv.org/abs/2502.00592) | - | ICML 2025 | - |
| 2024.06 | [AI-native Memory: A Pathway from LLMs Towards AGI](https://arxiv.org/abs/2406.18312) | - | arXiv | - |
| 2023.04 | [Scaling Transformer to 1M tokens and beyond with RMT](https://arxiv.org/abs/2304.11062) | - | AAAI 2024 | - |


## Personalized Alignment

| Date | Paper Title | Venue / Source | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.03 | [PersonaVLM: Long-Term Personalized Multimodal LLMs](https://github.com/MiG-NJU/PersonaVLM) | Nanjing University | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) <br> ![Stars](https://img.shields.io/github/stars/MiG-NJU/PersonaVLM?style=flat-square&logo=github) |
| 2025.10 | Preference-Aware Memory Update for Long-Term LLM Agents | - | arXiv | - |
| 2025.09 | Personalized Reasoning / PrefDisco | - | ICLR 2026 | - |
| 2025.08 | Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History | - | arXiv | - |
| 2025.05 | Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment | - | arXiv | - |
| 2025.03 | ALIGNX: From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment | - | arXiv | - |
| 2024.10 | Aligning LLMs with Individual Preferences via Interaction | - | arXiv | - |


## Personalized Retrieval

| Date | Paper Title | Venue / Source | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.05 | Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents | - | arXiv | - |
| 2025.10 | [LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866) | ZJUNLP | ICLR 2026 | [zjunlp/LightMem](https://github.com/zjunlp/LightMem) <br> ![Stars](https://img.shields.io/github/stars/zjunlp/LightMem?style=flat-square&logo=github) |
| 2025.04 | [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | Mem0 | arXiv | [mem0ai/mem0](https://github.com/mem0ai/mem0) <br> ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&logo=github) |
| 2023.10 | [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | UC Berkeley | arXiv | [letta-ai/letta](https://github.com/letta-ai/letta) <br> ![Stars](https://img.shields.io/github/stars/letta-ai/letta?style=flat-square&logo=github) |


## Benchmarks and Evaluation

| Date | Paper Title | Venue / Source | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- | :--- |
| 2026.05 | Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents (PerMemBench) | - | arXiv | - |
| 2026.03 | [Persona-MME from PersonaVLM: Long-Term Personalized Multimodal LLMs](https://github.com/MiG-NJU/PersonaVLM) | Nanjing University | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) <br> ![Stars](https://img.shields.io/github/stars/MiG-NJU/PersonaVLM?style=flat-square&logo=github) |
| 2025.12 | PERSONAMEM-V2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory | - | arXiv | - |
| 2025.06 | PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization | - | arXiv | - |
| 2025.04 | Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale (PERSONAMEM) | - | COLM 2025 | - |
| 2024.10 | LONGMEMEVAL: Benchmarking Chat Assistants on Long-Term Interactive Memory | - | ICLR 2025 | - |
| 2024.02 | Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo) | - | arXiv | - |
| 2023.04 | LaMP: When Large Language Models Meet Personalization | - | arXiv | - |


## Notes

GitHub star counts are displayed with dynamic shields.io badges.

## Citation

If this list is useful, please consider citing or starring the repository after publication.

## License

This repository is released under the MIT License.
