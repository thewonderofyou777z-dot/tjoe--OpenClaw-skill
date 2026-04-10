---
name: memsearch
description: Semantic memory search — vector-powered search over your markdown memory files. Ask questions in natural language, find relevant memories by meaning, not just keywords.
---

# memsearch — Semantic Memory Search

给理查的记忆系统添加语义搜索能力。原理：将 markdown 文件分块、向量化存入 Milvus，用自然语言搜索。

## 核心能力

- **语义搜索**：问「上次讨论的 Polymarket 策略」，即使没有「策略」这个词也能找到
- **完全本地**：用 Ollama + `nomic-embed-text` 模型，不需要 OpenAI API key
- **增量索引**：SHA-256 内容哈希，已存在的文件不会重复 embedding
- **文件监听**：`memsearch watch` 自动监控文件变化，实时更新索引

## 安装

```bash
# memsearch（已在 ~/.venv/memsearch）
# Ollama（已安装，brew services start ollama）
# embedding 模型：nomic-embed-text（下载中）

# 配置（已配置好）
~/.venv/memsearch/bin/memsearch config set embedding.provider ollama
~/.venv/memsearch/bin/memsearch config set embedding.model nomic-embed-text
~/.venv/memsearch/bin/memsearch config set embedding.base_url http://localhost:11434
```

## 使用方式

```bash
# 索引记忆目录
~/.venv/memsearch/bin/memsearch index ~/.openclaw/workspace/memory/
~/.venv/memsearch/bin/memsearch index ~/.openclaw/workspace/MEMORY.md

# 自然语言搜索
~/.venv/memsearch/bin/memsearch search "上次讨论的Polymarket策略"

# 查看统计
~/.venv/memsearch/bin/memsearch stats

# 监听文件变化（自动重新索引）
~/.venv/memsearch/bin/memsearch watch ~/.openclaw/workspace/memory/
```

## 在理查对话中使用

当用户说「我记得上次...」或者问「我们之前讨论过什么关于X」的时候，主动使用 memsearch 搜索。

```bash
~/.venv/memsearch/bin/memsearch search "关键词"
```

## 注意

- Ollama 服务需要在运行：`brew services start ollama`
- 模型 nomic-embed-text 下载完成后才能使用
- Milvus 数据存在 `~/.memsearch/milvus.db`（完全本地）
