---
name: tech-news-digest
description: Multi-source tech news digest. RSS layer installed (46+ sources, no API key). Twitter/GitHub/Brave search optional.
---

# Tech News Digest（科技新闻摘要）

46+ RSS 源，完整覆盖 AI / Crypto / Tech，不需要任何 API key。

## 已安装模块

- ✅ `fetch-rss.py` — RSS 抓取（76 个源，360+ 篇文章/48小时）
- ✅ `sources.json` — 源配置（HackerNews / MIT / VentureBeat / CoinDesk / AI newsletters 等）
- ✅ `merge-sources.py` — 合并去重
- ⏳ Twitter/GitHub/Web — 需要额外 API key，按需开启

## 使用方式

```bash
# 抓取过去48小时 RSS 新闻
cd ~/.openclaw/workspace/skills/tech-news-digest/scripts
python3 fetch-rss.py \
  --defaults ../config/defaults \
  --hours 48 \
  --output /tmp/rss-digest.json \
  --verbose

# 合并 + 按 topic 分类
python3 merge-sources.py --rss /tmp/rss-digest.json --output /tmp/merged.json
```

## 主要 RSS 源（46个）

**AI / LLM**
- OpenAI Blog、Google AI Blog、Anthropic、DeepMind
- Hacker News、MIT Tech Review、VentureBeat
- Lil'Log (Lilian Weng)、Chip Huyen

**Crypto**
- CoinDesk、Cointelegraph、The Block

**Tech**
- TechCrunch、The Verge、Ars Technica
- GitHub Blog、Product Hunt

**中文**
- 少数派、极客公园

## 整合简报

抓取后，理查读取 `/tmp/merged.json`，按简报格式整理输出到对应板块。

## 可选 API key（按需配置）

- `X_BEARER_TOKEN` — Twitter KOL 监控
- `GITHUB_TOKEN` — GitHub releases（提高 rate limit）
- `BRAVE_API_KEY` — Web 搜索

RSS 层不需要任何 key，直接可用。
