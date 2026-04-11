# MEMORY.md — 活跃长期记忆

> 📌 **上次更新：** 2026-04-11 | **下次整理：** 每次 session 结尾自动触发

---

## 🟡 最近讨论摘要（每次 session 必读）

> 以下是今天（2026-04-11）的讨论要点。新的 session 开始前请先读这些。

### 2026-04-11 今天的关键决定

| 话题 | 结论 | 标签 |
|------|------|------|
| **PPT Generator v2** | 升级完成，路径：`~/.openclaw/skills/ppt-generator/scripts/ppt_generator_v2.py` | `#PPT` `#v2` |
| **简报格式锁定** | 双语版（中文 + English括号），已写入 MEMORY.md | `#简报` `#双语` |
| **Feishu App权限问题** | App ID: `cli_a93d5c431cf99cb6`，需要用户开通 `docx:document:write` 权限 | `#飞书` |
| **Cron简报任务** | Step1（9:00生成→Downloads） + Step2（9:10发飞书，已配置） | `#cron` |
| **Google Search API** | `AIzaSyBmH5IyLT0AkfNZNeuLq0Gb-uN_tVLZUK0` 开通了Custom Search API（个人版飞书Bot限制多） | `#工具` |
| **无毛猫中耳炎** | 病灶深处，VBO手术是正确方案，TECA（封闭耳道）是过度治疗 | `#无毛猫` `#VBO` |
| **用户无毛猫情况** | 黑色脓+耳垢，盐城兽医建议TECA（不合理），建议转诊 | `#无毛猫` |
| **PPT v2问题** | v1有send_to_back XML兼容问题，已修复v2；Mac Mini用Keynote打开PPTX | `#PPT` |
| **MEMORY系统重构** | 正在做：Zettelkasten式总结 + 晨间锚点 + 标签系统 | `#记忆` |

### 长期记住的悬而未决
- 飞书Bot没有对小Joe的DM权限（个人版限制）
- Google Search API key需要新项目独立开通
- Mem0记忆系统未接入

---

## 关于用户

### 小Joe
- 身高：174cm（2026-04-10更正）
- 体重：~70kg
- 时区：Asia/Shanghai（GMT+8）
- 平台：Mac Mini (Darwin)，OpenClaw 本地部署
- 聊天渠道：**Telegram** + **webchat** + **飞书**（Bot已配对）
- 兴趣：Polymarket、自我提升、**健身**、**无毛猫（斯芬克斯）**

### 理查
- 2026-04-09 由小Joe命名
- 风格：务实、直接、有点个性
- Emoji：🤖

---

## 活跃工具与技能

### 🛠️ Mac 本地工具（已安装）
| 工具 | 版本 | 用途 |
|------|------|------|
| pandoc | 3.7.0.1 | Markdown ↔ PDF/Word/HTML |
| Python | 3.11 | 数据处理 |
| AppleScript | 内置 | 日历、Pages等Mac app控制 |
| Chrome headless | — | HTML → PDF |
| cliclick | 5.1 | GUI自动化（需辅助功能权限）|
| Homebrew | — | 包管理器 |
| youtube-transcript-api | — | YouTube字幕抓取 |
| python-pptx | — | PPT生成 |
| Pillow | — | 图片处理 |
| matplotlib | — | 图表生成 |

### 🧠 记忆相关
- **memsearch**：Ollama + nomic-embed-text，本地向量搜索
- **Milvus**：向量数据库 `~/.memsearch/milvus.db`
- **.learnings/**：错误和纠正记录
- **session-wrap-up**：自动commit脚本（简化版自写）

### 📡 API Keys
| 服务 | Key | 备注 |
|------|-----|------|
| YouTube Data API v3 | `AIzaSyDSkXW-rUSaYCIMiR3VMLwmUktAw0SB8Xw` | 正常工作 |
| Feishu Bot | App ID: `cli_a93d5c431cf99cb6` | Bot已配对 |

---

## 📋 每日简报格式（最终确认版 2026-04-11）

> ⚠️ **所有内容必须中英双语**：格式为「中文 (English)」，英文放括号里
> 示例：美伊历史性谈判开启 (US-Iran talks begin in Oman as first formal bilateral dialogue in years)

### 天气
- 城市：江苏盐城（wttr.in 实时）
- 内容：天气图标 + 温度 + 体感 + 风速 + 湿度 + 降雨 + 紫外线

### 国际政治
- 详细、附来源媒体（BBC World / Reuters / Al Jazeera）
- 核心事件 + 关键细节（事态进展和博弈细节，不只是标题）
- **4-6条**

### AI领域
- 按公司分类（OpenAI / Anthropic / Google / 开源社区）
- 中文：36氪 + 机器之心
- **中英双语**

### 大模型API价格对比
- 各平台官方定价（OpenAI / Groq / Grok / Gemini / Claude）
- 每个平台：模型名 + 输入价格 + 输出价格 + 备注
- 独立分析：近期降价/活动
- 底部：价格总结与建议

### YouTube值得关注的更新
- 频道名 + 最新视频标题 + 发布时间
- 理查推荐最值得看的1-2条

### Polymarket预测市场
- 数据来源：Gamma API（curl直接抓）
- 每个热门市场：YES价格 + 成交量 + 流动性
- **我的判断**：短期机会 / 中期机会 / 风险提示
- ⚠️ 免责声明

### NBA / F1（简略版）
- NBA：ESPN 西部前5（胜率/胜差/近况）
- F1：ESPN 前5（重大变化标注）

### 发送方式
- 每天 9:00 自动生成 → `~/Downloads/简报_YYYY-MM-DD.md`
- Step2（9:10）→ 飞书（目前发飞书有问题，pending解决）

---

## 🔧 Cron 定时任务

| 任务 | 时间 | 状态 | 备注 |
|------|------|------|------|
| 小Joe每日简报-生成 | 9:00 | ⚠️ 超时 | Step1生成文件 |
| 小Joe每日简报-发飞书 | 9:10 | ⚠️ 待测 | Step2发飞书 |
| 简报文件午夜清理 | 0:00 | ✅ | `rm ~/Downloads/简报_*.md` |
| Polymarket警报检查 | 自定义 | ✅ | timeout 300s |

---

## 🧠 Polymarket 知识（长期）

### 核心概念
- 基于 USDC on Polygon 的预测市场
- Gamma API（无需认证）：`https://gamma-api.polymarket.com`
- 关键参数：`volume`（成交量）、`liquidity`（流动性）
- 体育类市场成交量往往最大

### 盈利策略
- 赢家三要素：原创研究 + 仓位计算 + 市场选择
- Delta-neutral：Polymarket + Kalshi 对冲
- 套利机会注意2026年规则更新后利润下降

### 近期热门市场（2026-04-11实时）
| 市场 | YES价格 | 成交量 |
|------|---------|--------|
| 马刺NBA冠军 | 16.0% | $14.67M |
| 雪崩NHL冠军 | 19.7% | $13.42M |
| GTA VI发布 | 1.6% | $13.33M |
| 耶稣回归 | 48.5% | $10.95M |
| 雷霆NBA冠军 | 40.5% | $6.31M |

---

## 🔑 重要文件路径

| 文件 | 说明 |
|------|------|
| `~/.openclaw/workspace/学习反思与Polymarket认知_2026-04-09.md` | Polymarket深度学习文档 |
| `~/.openclaw/workspace/skills/ppt-generator/` | PPT生成器v1+v2 |
| `~/.openclaw/skills/tech-news-digest/` | RSS新闻聚合 |
| `~/Downloads/简报_*.md` | 每日简报（午夜自动清理） |
| `~/Downloads/每日简报_*_v2.pptx` | PPT v2测试文件 |

---

## 📌 待处理（Active）

- [ ] **飞书发送**：Bot对小Joe的DM权限问题（个人版限制，需用户授权）
- [ ] **Google Search API**：需要新Google Cloud项目独立开通Custom Search API
- [ ] **Mem0接入**：记忆持久化层
- [ ] **简报cron超时**：Step1任务超时（300s→已改5min，仍需监控）
- [ ] **无毛猫VBO手术**：建议转诊到有CT的专科医院

---

## 📚 长期知识（稳定不变的内容）

### MiniMax 平台
- 模型：`minimax/MiniMax-M2.7`（当前使用）
- highspeed版需套餐支持
- image-01：图片生成

### 工具配置
- **飞书**：App ID `cli_a93d5c431cf99cb6`，pairing已通过
- **Mac日历**：中文系统日历名「日历」

### GitHub
- 仓库：`thewonderofyou777z-dot/tjoe--OpenClaw-skill`
- Token存钥匙串，HTTPS认证

---

## 📅 每日日志归档（按日期）

- `memory/2026-04-11.md` — 今天（待写入知识点提取）
- `memory/2026-04-10.md` — 昨日
- `memory/2026-04-09.md` — 前日
- `memory/2026-04-08.md` — Polymarket模拟仓记录

---

## 🏷️ 标签索引（快速检索）

| 标签 | 关联内容 |
|------|---------|
| `#polymarket` | Gamma API、盈利策略、空投机会 |
| `#飞书` | App权限、Bot DM问题、文档创建 |
| `#PPT` | v1/v2生成器、模板风格、图表类型 |
| `#简报` | 每日简报格式、双语要求、cron任务 |
| `#记忆` | MEMORY.md结构、Zettelkasten、晨间锚点 |
| `#无毛猫` | 中耳炎、VBO手术、盐城医院 |
| `#工具` | API Keys、Mac工具、Python库 |
| `#健身` | PPL方案、蛋白质目标、PR记录 |
