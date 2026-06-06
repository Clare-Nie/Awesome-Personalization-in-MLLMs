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

| Date / Paper | Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2023.10 / [arXiv](https://arxiv.org/abs/2310.08560) | MemGPT: Towards LLMs as Operating Systems | arXiv | [letta-ai/letta](https://github.com/letta-ai/letta) / 23,168 stars |
| 2025.02 / [arXiv](https://arxiv.org/abs/2502.12110) | A-Mem: Agentic Memory for LLM Agents | arXiv | [agiresearch/A-mem](https://github.com/agiresearch/A-mem) / 1,036 stars |
| 2025.04 / [arXiv](https://arxiv.org/abs/2504.19413) | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | arXiv | [mem0ai/mem0](https://github.com/mem0ai/mem0) / 57,857 stars |
| 2025.05 | Memory OS of AI Agent | arXiv | - |
| 2025.10 | LightMem: Lightweight and Efficient Memory-Augmented Generation | ICLR 2026 | [zjunlp/LightMem](https://github.com/zjunlp/LightMem) / 907 stars |

### Personalized Memory Architectures

| Date / Paper | Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2025.07 | MIRIX: Multi-Agent Memory System for LLM-Based Agents | arXiv | [Mirix-AI/MIRIX](https://github.com/Mirix-AI/MIRIX) / stars pending |
| 2025.08 | M3-Agent: A Multimodal Agent with Long-Term Memory | arXiv | [ByteDance-Seed/m3-agent](https://github.com/ByteDance-Seed/m3-agent) / stars pending |
| 2025.12 | MemVerse: Multimodal Memory for Lifelong Learning Agents | arXiv | - |
| 2026.03 | PersonaVLM: Long-Term Personalized Multimodal LLMs | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) / stars pending |

### Latent Memory Mechanisms

| Date / Paper | Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2023.04 / [arXiv](https://arxiv.org/abs/2304.11062) | Scaling Transformer to 1M tokens and beyond with RMT | AAAI 2024 | - |
| 2024.06 / [arXiv](https://arxiv.org/abs/2406.18312) | AI-native Memory: A Pathway from LLMs Towards AGI | arXiv | - |
| 2025.02 / [arXiv](https://arxiv.org/abs/2502.00592) | M+: Extending MemoryLLM with Scalable Long-Term Memory | ICML 2025 | - |
| 2025.03 / [arXiv](https://arxiv.org/abs/2503.08102) | AI-native Memory 2.0: Second Me | arXiv | - |
| 2025.09 | MemGen: Weaving Generative Latent Memory for Self-Evolving Agents | ICLR 2026 | - |

## Personalized Alignment

| Date / Paper | Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2024.10 | Aligning LLMs with Individual Preferences via Interaction | arXiv | - |
| 2025.03 | ALIGNX: From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment | arXiv | - |
| 2025.05 | Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment | arXiv | - |
| 2025.08 | Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History | arXiv | - |
| 2025.09 | Personalized Reasoning / PrefDisco | ICLR 2026 | - |
| 2025.10 | Preference-Aware Memory Update for Long-Term LLM Agents | arXiv | - |
| 2026.03 | PersonaVLM: Long-Term Personalized Multimodal LLMs | CVPR 2026 | [MiG-NJU/PersonaVLM](https://github.com/MiG-NJU/PersonaVLM) / stars pending |

## Personalized Retrieval

| Date / Paper | Title | Publication | GitHub / Stars |
| :--- | :--- | :--- | :--- |
| 2023.10 / [arXiv](https://arxiv.org/abs/2310.08560) | MemGPT: Towards LLMs as Operating Systems | arXiv | [letta-ai/letta](https://github.com/letta-ai/letta) / 23,168 stars |
| 2025.04 / [arXiv](https://arxiv.org/abs/2504.19413) | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | arXiv | [mem0ai/mem0](https://github.com/mem0ai/mem0) / 57,857 stars |
| 2025.10 | LightMem: Lightweight and Efficient Memory-Augmented Generation | ICLR 2026 | [zjunlp/LightMem](https://github.com/zjunlp/LightMem) / 907 stars |
| 2026.05 | Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents | arXiv | - |

## Benchmarks and Evaluation

| Date / Paper | Title | Publication | GitHub / Stars |
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

GitHub star counts are checked manually when updating this repository. Some entries are marked as `stars pending` when GitHub API rate limits prevent real-time verification.

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Citation

If this list is useful, please consider citing or starring the repository after publication.

## License

This repository is released under the MIT License.
