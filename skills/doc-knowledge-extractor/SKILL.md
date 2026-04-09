---
name: doc-knowledge-extractor
description: >
  Extract structured knowledge from documents (PDF, DOCX, TXT, MD, HTML) and store in OpenClaw memory.
  Trigger when: user shares a document and wants to understand/remember it; user says read/summarize and save key points;
  user asks to analyze document or build knowledge base from files.
  Does NOT trigger for simple one-off summarization without memory storage.
---

# Doc Knowledge Extractor

Extract structured knowledge from documents and store in OpenClaw memory.

## Workflow

### Step 1: Extract Text

使用 `scripts/extract_text.py` 提取文档内容：

```bash
python3 ~/.openclaw/workspace/skills/doc-knowledge-extractor/scripts/extract_text.py "/path/to/file.pdf" --max-chars 50000
```

支持格式：PDF, DOCX, TXT, MD, HTML, RTF

### Step 2: Understand & Extract Knowledge

参考 `references/extraction-template.md` 进行结构化知识提取：

1. 识别核心实体（人物/概念/事件/产品）
2. 提取关键信息和结论
3. 标注信息来源
4. 评估重要程度

### Step 3: Save to Memory

根据知识类型存入对应位置：

- **用户相关** → `MEMORY.md` 或 `USER.md`
- **项目相关** → `projects/[项目名]/KNOWLEDGE.md`
- **人物/组织** → `ontology/persons.md` 或 `ontology/organizations.md`
- **每日事件** → `memory/YYYY-MM-DD.md`
- **通用知识** → `memory/knowledge-base/`

### Step 4: 生成摘要报告

向用户返回结构化摘要，包含：
- 文档概要
- 核心知识点（3-5条）
- 知识存储位置
- 与现有知识的关系

## 工具

`scripts/extract_text.py` — macOS textutil 封装，支持 PDF/DOCX/TXT/MD/HTML

```bash
# 基本用法
python3 scripts/extract_text.py input.pdf

# 输出到文件
python3 scripts/extract_text.py input.pdf -o output.txt

# 限制长度（用于超大文档）
python3 scripts/extract_text.py large.pdf --max-chars 30000
```

## 注意事项

- 先运行 extract_text.py 获取原始文本，再进行知识提取
- 存储时追加到现有文件，不要覆盖
- 与现有知识冲突时，标注"更新：[新信息]，待确认：[原信息]"
- 超大文档（>50000字符）先截断处理，分批提取
- 如果文档是 URL，先用 web_fetch 抓取内容再提取
