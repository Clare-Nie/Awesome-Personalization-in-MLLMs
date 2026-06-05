<p align="center">
  <img src="./assets/title.png" alt="Awesome Personalization in MLLMs" width="720">
</p>

# Awesome Personalization in MLLMs

> 关于 LLM 和 MLLM 个性化的论文总结，覆盖 **个性化记忆、对齐、Benchmark 和检索**。

[English README](./README.md) | [在线主页](https://clare-nie.github.io/Awesome-Personalization-in-MLLMs/)

个性化 LLM / MLLM 的目标，不只是让模型对“平均用户”表现更好，而是让模型理解一个具体用户：长期目标、动态偏好、隐式 persona、多模态上下文，以及什么时候应该使用个性化信息、什么时候不应该使用。

这个仓库主要整理四个问题：

- **记忆：** agent 应该记住什么、更新什么、检索什么、遗忘什么？
- **对齐：** 模型如何适配不同用户的偏好、人格和场景？
- **Benchmark：** 如何评测长期、动态、隐式、多模态的个性化能力？
- **检索：** 个性化系统如何检索正确的用户上下文、记忆和证据？

## 目录

- [个性化记忆](#个性化记忆)
- [个性化对齐](#个性化对齐)
- [Benchmark 与评估](#benchmark-与评估)
- [个性化检索](#个性化检索)

## 研究脉络

| 方向 | 核心问题 | 代表工作 |
| :--- | :--- | :--- |
| 个性化记忆 | 什么该存、什么该更新、什么该检索、什么该遗忘？ | MemGPT, A-Mem, Mem0, MemoryOS, LightMem, MIRIX, M3-Agent, MemVerse |
| 个性化对齐 | 模型如何适配个体偏好、人格和上下文？ | Personality Alignment, Interaction Alignment, ALIGNX, RLPA / Dynamic Profile, PrefDisco, PAMU |
| Benchmark | 如何评测长期用户建模，而不是只做通用 QA？ | LaMP, LoCoMo, LongMemEval, PERSONAMEM, Persona-MME, PersonaFeedback, PerMemBench |
| 个性化检索 | 如何选择正确的用户上下文和证据？ | RAG-style memory retrieval, graph memory, preference-aware retrieval, storage gating |
| 多模态个性化 | 图像、个人概念、视觉记忆如何支持个性化 MLLM？ | MC-LLaVA, Yo'LLaVA, MyVLM, PersonaVLM |

## 个性化记忆

### 基础记忆系统

- **MemGPT: Towards LLMs as Operating Systems**（2023.10）  
  用操作系统的视角设计 LLM 记忆管理，让模型通过工具式操作管理短期和长期记忆。  
  链接：[arXiv](https://arxiv.org/abs/2310.08560)

- **A-Mem: Agentic Memory for LLM Agents**（2025.02）  
  借鉴卡片盒笔记法组织 agentic memory，关注长线对话、多跳推理和时间推理。  
  链接：[arXiv](https://arxiv.org/abs/2502.12110)

- **Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory**（2025.04）  
  面向生产环境的长期记忆系统，结合可扩展记忆抽取、检索和图记忆。  
  链接：[arXiv](https://arxiv.org/abs/2504.19413)

- **Memory OS of AI Agent**（2025.05）  
  提出短期、中期、长期的分层记忆架构，面向个性化对话和 persona 追踪。

- **LightMem: Lightweight and Efficient Memory-Augmented Generation**（ICLR 2026 / 2025.10）  
  采用轻量压缩和主题级记忆更新，减少逐轮写入成本，常在 LongMemEval 和 LoCoMo 上评测。

### 多模态 / 个性化记忆系统

- **MIRIX: Multi-Agent Memory System for LLM-Based Agents**（2025.07）  
  面向 LLM agent 的多智能体记忆系统，用于组织和使用长期记忆。

- **M3-Agent: A Multimodal Agent with Long-Term Memory**（2025.08）  
  研究具备长期记忆的多模态 agent，把视觉上下文、交互历史和用户中心记忆结合起来。

- **MemVerse: Multimodal Memory for Lifelong Learning Agents**（2025.12）  
  关注 lifelong agent 的多模态记忆，让系统持续积累并复用用户相关经验。

## 个性化对齐

- **Personality Alignment of Large Language Models**（ICLR 2025）  
  利用人格数据和 activation-level intervention，让模型输出更符合个体人格特质。

- **Aligning LLMs with Individual Preferences via Interaction**（2024.10）  
  通过多轮交互学习用户偏好，而不是只依赖静态 profile。

- **ALIGNX: From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment**（2025.03）  
  从大规模用户行为中构造 user-level preference 数据和偏好空间。

- **Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment**（2025.05）  
  动态建模用户 profile，使模型能随长期交互持续演化。

- **Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History**（2025.08）  
  指出 LLM 人格测量存在不稳定性，为人格个性化和评估提出警示。

- **Personalized Reasoning / PrefDisco**（ICLR 2026 / 2025.09）  
  研究在缺少用户历史时，模型如何主动发现偏好并进行个性化推理。

- **Preference-Aware Memory Update for Long-Term LLM Agents**（2025.10）  
  关注用户偏好变化下的记忆更新，融合短期波动与长期趋势。

## Benchmark 与评估

- **LaMP: When Large Language Models Meet Personalization**（2023.04）  
  早期个性化 NLP benchmark，包含 7 个任务，测试用户 profile 是否能提升分类和生成。

- **Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)**（2024.02）  
  长期多会话对话记忆 benchmark。很多工作常用 LoCoMo-10，并聚焦人物相关记忆问题。

- **LONGMEMEVAL: Benchmarking Chat Assistants on Long-Term Interactive Memory**（ICLR 2025 / 2024.10）  
  测试长期助手记忆，包括信息抽取、跨会话推理、知识更新、时间推理和拒答。

- **Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale (PERSONAMEM)**（COLM 2025 / 2025.04）  
  评估动态用户画像和个性化回答选择，重点关注偏好变化与新场景泛化。

- **PERSONAMEM-V2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory**（2025.12）  
  从工具型、多会话、多模态、多语言交互中评估隐式 persona 学习。

- **Persona-MME from PersonaVLM: Long-Term Personalized Multimodal LLMs**（CVPR 2026 / 2026.03）  
  多模态长期个性化 benchmark，包含 2034 个 in-situ test cases 和 14 个细粒度任务。

- **PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization**（2025.06）  
  人工标注的个性化偏好比较 benchmark，判断哪个回答更符合给定 persona。

- **Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents (PerMemBench)**（2026.05）  
  评估 session-level storage gating，即某段交互是否值得为特定用户写入长期记忆。

## 个性化检索

个性化检索连接记忆和生成：系统需要判断当前请求应该检索哪些用户历史、偏好、profile、图像或过去事件。

- **Memory-augmented retrieval for agents**  
  从长期记忆库中检索用户记忆，常结合 embedding search、图记忆、recency、importance 或 hybrid ranking。

- **Preference-aware retrieval**  
  不只看语义相似度，还要看检索结果是否符合用户当前偏好状态。

- **Context-aware retrieval**  
  在注入用户信息前，先判断当前任务是否适合个性化。

- **Storage-aware retrieval**  
  和记忆写入策略配合：如果重要信息一开始没有被存储，后续检索再强也无法恢复。

这一部分仍在扩展，欢迎补充 personalized RAG、user-aware retrieval、memory retrieval 和 multimodal retrieval 相关工作。

## 个性化多模态模型

- **MC-LLaVA: Multi-Concept Personalized Vision-Language Model**  
  研究视觉语言模型中的多概念个性化，关注用户特定或概念特定的视觉表示。

- **Yo'LLaVA: Your Personalized Language and Vision Assistant**（2024.03）  
  探索个性化视觉语言助手，强调用户专属视觉概念和个人上下文。

- **MyVLM: Personalizing VLMs for User-Specific Queries**（2024.06）  
  研究面向用户特定查询的 VLM 个性化理解与回答。

- **PersonaVLM: Long-Term Personalized Multimodal LLMs**（CVPR 2026 / 2026.03）  
  长期个性化多模态 agent 框架，结合用户偏好记忆、视觉概念、长期记忆和动态人格对齐，并提出 Persona-MME benchmark。

## 数据集与任务

| Benchmark | 主要关注 | 评估方式 |
| :--- | :--- | :--- |
| LaMP | 个性化 NLP 分类与生成 | Accuracy, F1, MAE, RMSE, ROUGE |
| LoCoMo | 长期对话记忆 | QA 正确性 |
| LongMemEval | 长期助手记忆 | QA, LLM judge, abstention |
| PERSONAMEM | 动态 persona 与个性化回答 | 多选题 |
| PersonaMem-v2 | 隐式 persona 与 agentic memory | MCQ + open-ended |
| Persona-MME | 多模态长期个性化 | Accuracy |
| PersonaFeedback | 显式 persona 下的回答偏好 | 人类多数投票 accuracy |
| PerMemBench | 个性化记忆写入 | Gating F1, FNR, FPR |

## 贡献

欢迎补充论文、代码、benchmark、数据集和简短说明。请参考 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 引用

如果这个列表对你有帮助，欢迎在仓库发布后 star 或引用。

## License

本仓库采用 MIT License。
