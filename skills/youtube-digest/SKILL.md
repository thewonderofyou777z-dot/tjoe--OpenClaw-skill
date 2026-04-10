---
name: youtube-digest
description: Get daily summaries of new videos from your favorite YouTube channels. Uses youtube-transcript-api (free, no API key needed).
---

# YouTube Digest（每日 YouTube 视频摘要）

抓取指定频道的最新视频，提取字幕，生成摘要。

## 安装依赖

```bash
pip install youtube-transcript-api
```

## 使用方式

### 1. 获取频道最新视频

```bash
node {baseDir}/scripts/youtube-digest.mjs latest <channel_url_or_handle> [--limit 3]
```

支持的频道格式：
- `@handle`（如 `@TED`）
- 频道 URL（如 `https://www.youtube.com/@TED`）
- 频道 ID（如 `UCsUQM0W5JXv5xJn0hH8CmRg`）

### 2. 获取视频字幕

```bash
node {baseDir}/scripts/youtube-digest.mjs transcript <video_url_or_id>
```

### 3. 生成每日摘要

需要先配置关注的频道列表（在 SKILL.md 同目录创建 `channels.txt`，每行一个频道）。

```bash
node {baseDir}/scripts/youtube-digest.mjs digest --channels /path/to/channels.txt
```

## channels.txt 格式

```
@3Blue1Brown
@Veritasium
@LexFridman
@KBDragon
```

## 依赖

- `python3 -m youtube_transcript_api`（直接调用 Python）
- 无需 API key
- 需要网络连接

## 限制

- 部分视频没有字幕（自动跳过）
- 部分频道禁止自动抓取（跳过并警告）
- YouTube 可能会限流（加了延迟保护）
