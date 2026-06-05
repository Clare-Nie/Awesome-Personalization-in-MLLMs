<p align="center">
  <img src="./assets/logo.png" alt="Awesome Personalization in MLLMs Logo" width="180">
</p>

# Awesome Personalization in MLLMs

> A curated list of papers, benchmarks, datasets, and systems on personalization in LLMs and MLLMs, with a focus on **memory, alignment, and evaluation**.

[中文 README](./README_zh.md)

Personalized LLMs and MLLMs aim to move beyond one-size-fits-all assistants. Instead of only optimizing for average human preference, they need to understand a specific user: long-term goals, evolving preferences, implicit personas, multimodal context, and when personalization should or should not be applied.

This repository tracks work around three connected questions:

- **Memory:** what should an agent remember, update, retrieve, and forget?
- **Alignment:** how should a model adapt to individual preferences, personalities, and contexts?
- **Evaluation:** how do we benchmark long-term, dynamic, implicit, and multimodal personalization?

## Contents

- [Survey Map](#survey-map)
- [Long-Term Memory for Agents](#long-term-memory-for-agents)
- [Personalized Multimodal Models](#personalized-multimodal-models)
- [Personalized Alignment](#personalized-alignment)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Datasets and Tasks](#datasets-and-tasks)
- [Contributing](#contributing)

## Survey Map

| Direction | Core Question | Representative Work |
| :--- | :--- | :--- |
| Long-term memory | What should be stored, updated, retrieved, and forgotten? | MemGPT, A-Mem, Mem0, MemoryOS, LightMem, MIRIX, M3-Agent, MemVerse |
| Personalized alignment | How can a model adapt to individual preferences and personalities? | Personality Alignment, Interaction Alignment, ALIGNX, RLPA / Dynamic Profile, PrefDisco, PAMU |
| Multimodal personalization | How can visual context, personal concepts, and user-specific memories support MLLMs? | MC-LLaVA, Yo'LLaVA, MyVLM, PersonaVLM |
| Evaluation | How do we test long-term user modeling beyond generic QA? | LaMP, LoCoMo, LongMemEval, PERSONAMEM, Persona-MME, PersonaFeedback, PerMemBench |

## Long-Term Memory for Agents

### Foundational Memory Systems

- **MemGPT: Towards LLMs as Operating Systems** (2023.10)  
  Introduces an OS-inspired memory management framework where LLM agents manage short-term and long-term memory through tool-like operations.  
  Links: [arXiv](https://arxiv.org/abs/2310.08560)

- **A-Mem: Agentic Memory for LLM Agents** (2025.02)  
  Builds agentic memory with a note-taking / Zettelkasten-style organization, focusing on long-horizon dialogue, multi-hop reasoning, and temporal reasoning.  
  Links: [arXiv](https://arxiv.org/abs/2502.12110)

- **Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory** (2025.04)  
  A production-oriented memory system that combines scalable memory extraction, retrieval, and graph-based memory for agent applications.  
  Links: [arXiv](https://arxiv.org/abs/2504.19413)

- **Memory OS of AI Agent** (2025.05)  
  Proposes a hierarchical memory architecture with short-term, mid-term, and long-term memory, targeting personalized dialogue and persona tracking.  

- **LightMem: Lightweight and Efficient Memory-Augmented Generation** (ICLR 2026 / 2025.10)  
  Uses lightweight compression and topic-level memory updates instead of heavy turn-level memory operations, evaluated on long-context memory benchmarks such as LongMemEval and LoCoMo.

### Multimodal / Personalized Memory Systems

- **MIRIX: Multi-Agent Memory System for LLM-Based Agents** (2025.07)  
  A multi-agent memory system for organizing and using long-term memories in LLM agents.

- **M3-Agent: A Multimodal Agent with Long-Term Memory** (2025.08)  
  Studies multimodal agents with long-term memory, connecting visual context, interaction history, and user-centered memory.

- **MemVerse: Multimodal Memory for Lifelong Learning Agents** (2025.12)  
  Focuses on multimodal memory for lifelong agents that continuously accumulate and reuse user-specific experience.

## Personalized Multimodal Models

- **MC-LLaVA: Multi-Concept Personalized Vision-Language Model**  
  Studies personalization in vision-language models through user-specific or concept-specific visual representations.

- **Yo'LLaVA: Your Personalized Language and Vision Assistant** (2024.03)  
  Explores personalized vision-language assistance, emphasizing user-specific visual concepts and personal context.

- **MyVLM: Personalizing VLMs for User-Specific Queries** (2024.06)  
  Investigates user-specific visual-language understanding and personalized responses for VLMs.

- **PersonaVLM: Long-Term Personalized Multimodal LLMs** (CVPR 2026 / 2026.03)  
  A unified framework for long-term personalized multimodal agents, combining user preference memory, visual concepts, long-term memory, and dynamic persona alignment. It also introduces Persona-MME for evaluation.

## Personalized Alignment

- **Personality Alignment of Large Language Models** (ICLR 2025)  
  Aligns model behavior with individual personality traits using personality data and activation-level interventions.

- **Aligning LLMs with Individual Preferences via Interaction** (2024.10)  
  Learns user preferences through multi-turn interaction rather than relying only on static profiles.

- **ALIGNX: From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment** (2025.03)  
  Builds scalable user-level preference data and preference spaces from large-scale user behavior.

- **Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment** (2025.05)  
  Models user profiles dynamically so that personalization can evolve with long-term interactions.

- **Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History** (2025.08)  
  Shows that personality measurement in LLMs can be unstable, raising concerns for personality-based personalization and evaluation.

- **Personalized Reasoning / PrefDisco** (ICLR 2026 / 2025.09)  
  Studies active discovery of user preferences for personalized reasoning when the model lacks enough user history.

- **Preference-Aware Memory Update for Long-Term LLM Agents** (2025.10)  
  Focuses on updating preference memories under short-term fluctuations and long-term trends.

## Benchmarks and Evaluation

- **LaMP: When Large Language Models Meet Personalization** (2023.04)  
  A foundational personalized NLP benchmark with seven tasks, testing whether user profiles improve classification and generation.

- **Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)** (2024.02)  
  Evaluates long-term conversational memory over long multi-session dialogues. Common usage often focuses on LoCoMo-10 and person-related memory questions.

- **LONGMEMEVAL: Benchmarking Chat Assistants on Long-Term Interactive Memory** (ICLR 2025 / 2024.10)  
  Tests long-term assistant memory across information extraction, multi-session reasoning, knowledge updates, temporal reasoning, and abstention.

- **Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale (PERSONAMEM)** (COLM 2025 / 2025.04)  
  Evaluates dynamic user profiling and personalized response selection under evolving preferences.

- **PERSONAMEM-V2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory** (2025.12)  
  Evaluates implicit persona learning from tool-like, multi-session, multimodal, and multilingual interactions.

- **Persona-MME from PersonaVLM: Long-Term Personalized Multimodal LLMs** (CVPR 2026 / 2026.03)  
  A multimodal personalization benchmark with 2034 in-situ test cases and 14 fine-grained tasks across memory, intent, behavior, growth, preference, relationship, and alignment.

- **PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization** (2025.06)  
  A human-annotated preference comparison benchmark for judging which response better fits a given persona.

- **Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents (PerMemBench)** (2026.05)  
  Evaluates session-level storage gating: whether a session should be stored as long-term memory for a specific user.

## Datasets and Tasks

| Benchmark | Main Focus | Evaluation Style |
| :--- | :--- | :--- |
| LaMP | Personalized NLP classification and generation | Accuracy, F1, MAE, RMSE, ROUGE |
| LoCoMo | Long-term conversational memory | QA correctness |
| LongMemEval | Long-term assistant memory | QA, LLM judge, abstention |
| PERSONAMEM | Dynamic persona and personalized response | Multiple choice |
| PersonaMem-v2 | Implicit persona and agentic memory | MCQ + open-ended |
| Persona-MME | Long-term multimodal personalization | Accuracy |
| PersonaFeedback | Persona-conditioned response preference | Human majority accuracy |
| PerMemBench | Personalized memory storage | Gating F1, FNR, FPR |

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Citation

If this list is useful, please consider citing or starring the repository after publication.

## License

This repository is released under the MIT License.
