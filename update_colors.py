import re

def optimize_readme(filepath, is_zh=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Overview Table with colored badges
    if is_zh:
        content = re.sub(r'\|\s*\*\*个性化记忆\*\*\s*\|', r'| ![Memory](https://img.shields.io/badge/🧠_个性化记忆-0f9f8f?style=flat-square) |', content)
        content = re.sub(r'\|\s*\*\*个性化对齐\*\*\s*\|', r'| ![Alignment](https://img.shields.io/badge/🎯_个性化对齐-7a4ef3?style=flat-square) |', content)
        content = re.sub(r'\|\s*\*\*个性化检索\*\*\s*\|', r'| ![Retrieval](https://img.shields.io/badge/🔍_个性化检索-0b6b92?style=flat-square) |', content)
        content = re.sub(r'\|\s*\*\*Benchmark 与评估\*\*\s*\|', r'| ![Evaluation](https://img.shields.io/badge/📊_Benchmark_与评估-b45a00?style=flat-square) |', content)
        
        # Add colored block below main section headers
        content = re.sub(r'## 🧠 个性化记忆\n', r'## 🧠 个性化记忆\n\n> ![#0f9f8f](https://img.shields.io/badge/-_#0f9f8f-0f9f8f?style=flat-square) *agent 应该存什么、更新什么、检索什么、压缩什么、遗忘什么？*\n', content)
        content = re.sub(r'## 🎯 个性化对齐\n', r'## 🎯 个性化对齐\n\n> ![#7a4ef3](https://img.shields.io/badge/-_#7a4ef3-7a4ef3?style=flat-square) *模型如何适配个体偏好、人格和上下文？*\n', content)
        content = re.sub(r'## 🔍 个性化检索\n', r'## 🔍 个性化检索\n\n> ![#0b6b92](https://img.shields.io/badge/-_#0b6b92-0b6b92?style=flat-square) *系统如何选择正确的用户上下文、记忆和证据？*\n', content)
        content = re.sub(r'## 📊 Benchmark 与评估\n', r'## 📊 Benchmark 与评估\n\n> ![#b45a00](https://img.shields.io/badge/-_#b45a00-b45a00?style=flat-square) *如何评测长期、动态、隐式、多模态的个性化能力？*\n', content)
        
    else:
        content = re.sub(r'\|\s*\*\*Personalized Memory\*\*\s*\|', r'| ![Memory](https://img.shields.io/badge/🧠_Personalized_Memory-0f9f8f?style=flat-square) |', content)
        content = re.sub(r'\|\s*\*\*Personalized Alignment\*\*\s*\|', r'| ![Alignment](https://img.shields.io/badge/🎯_Personalized_Alignment-7a4ef3?style=flat-square) |', content)
        content = re.sub(r'\|\s*\*\*Personalized Retrieval\*\*\s*\|', r'| ![Retrieval](https://img.shields.io/badge/🔍_Personalized_Retrieval-0b6b92?style=flat-square) |', content)
        content = re.sub(r'\|\s*\*\*Benchmarks and Evaluation\*\*\s*\|', r'| ![Evaluation](https://img.shields.io/badge/📊_Benchmarks_&_Evaluation-b45a00?style=flat-square) |', content)
        
        # Add colored block below main section headers
        content = re.sub(r'## 🧠 Personalized Memory\n', r'## 🧠 Personalized Memory\n\n> ![#0f9f8f](https://img.shields.io/badge/-_#0f9f8f-0f9f8f?style=flat-square) *What should an agent store, update, retrieve, compress, and forget?*\n', content)
        content = re.sub(r'## 🎯 Personalized Alignment\n', r'## 🎯 Personalized Alignment\n\n> ![#7a4ef3](https://img.shields.io/badge/-_#7a4ef3-7a4ef3?style=flat-square) *How can a model adapt to individual preferences, personalities, and contexts?*\n', content)
        content = re.sub(r'## 🔍 Personalized Retrieval\n', r'## 🔍 Personalized Retrieval\n\n> ![#0b6b92](https://img.shields.io/badge/-_#0b6b92-0b6b92?style=flat-square) *How should systems select the right user context, memory, and evidence?*\n', content)
        content = re.sub(r'## 📊 Benchmarks and Evaluation\n', r'## 📊 Benchmarks and Evaluation\n\n> ![#b45a00](https://img.shields.io/badge/-_#b45a00-b45a00?style=flat-square) *How do we evaluate long-term, dynamic, implicit, and multimodal personalization?*\n', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

optimize_readme('README.md', is_zh=False)
optimize_readme('README_zh.md', is_zh=True)
