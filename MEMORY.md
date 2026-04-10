# MEMORY.md - Long-Term Memory

_Last updated: 2026-04-09_

## 关于用户

### 小Joe
- 名字：小Joe
- 时区：Asia/Shanghai
- 平台：Mac Mini (Darwin)，OpenClaw 本地部署
- 聊天渠道：Telegram + webchat
- 兴趣：Polymarket、自我提升、健身

### 理查（我的名字）
- 2026-04-09 由小Joe命名
- 风格：务实、直接、有点个性
- Emoji：🤖

### Top Skills 推荐（2026年3月视频数据）
1. **Capability Evolver** — AI 自我进化引擎，35K+ 下载
2. **GOG** — Google Workspace 全家桶，14K+ 下载
3. **Agent Browser** — 浏览器自动化，11K+ 下载
4. **Summarize** — 智能文本摘要，10K+ 下载
5. **Mission Control** — 高级工作流控制中心，8K+ 下载

### 核心概念
- OpenClaw 是本地运行的 AI 助手
- Skills 扩展能力，ClawHub 有 13,700+ Skills
- Memory 系统跨会话记忆
- Discord 可作为聊天平台接入

### 实用 Prompt 模式
- 每日定时简报
- 工作流发现
- 跨平台编排

### 🛠️ Mac 本地工具（已安装）
- **pandoc 3.7.0.1** — Markdown ↔ PDF/Word/HTML/EPUB 格式转换（brew 安装）
- **Python 3.9** — 内置，数据处理、CSV/JSON/numbers XML
- **AppleScript/osascript** — 日历、Pages 等 Mac app 控制
- **Chrome headless** — HTML → PDF 转换
- **Homebrew** — 包管理器

### 📄 重要文件路径
- 学习反思与Polymarket认知：~/.openclaw/workspace/学习反思与Polymarket认知_2026-04-09.md
- PDF版本：~/Downloads/学习反思与Polymarket认知_2026-04-09.pdf

### ⚠️ 待处理
- Mac Calendar AppleScript 权限问题（事件读不到，可能 iCloud 日历）
- GUI 自动化需要安装 cliclick（brew install cliclick）

### 📋 每日简报格式（小Joe确认版，2026-04-08）

**【国际政治】**
- 详细、附来源媒体
- 核心事件 + 关键细节（不止标题，要有事态进展和博弈细节）
- 中美关系单独列板块

**【AI领域】**
- 详细、附来源媒体
- 按公司分类（OpenAI/Anthropic/Google/微软/其他）
- 模型发布、算力合作、监管动态都要
- 新模型单独列表格对比

**【Polymarket预测市场】（优化版，2026-04-08确认）**
- 数据来源：Gamma API `gamma-api.polymarket.com`（官方无需认证，curl直接抓）
- 每个热门市场展示：
  - 当前YES价格（概率%）+ 成交量 + 流动性（liquidity）
  - 订单簿spread（bid/ask价差，越小说明市场越健康）
  - 我的分析判断（信号/机会/风险）
- 单独列出「我的判断」板块：短期机会 / 中期机会 / 风险提示
- 注明：数据均为实时API抓取，非第三方估算
- ⚠️ 免责声明

**【NBA / F1 / 游戏】（简略版）
- 每条附一句核心

**格式要求**：
- 政治和AI要详细全面，不只是标题
- Polymarket要有深度分析和预测，不是只列数据
- 注明媒体来源
- 分析部分要体现独立思考，不是泛泛而谈

### 信息来源
- YouTube 文档：`~/.openclaw/workspace/youtube-docs/`

---

## Polymarket 预测市场知识（深度）

### 平台概述
- 基于加密货币（USDC on Polygon）的预测市场
- 交易 YES/NO 股票，价格代表事件概率
- 主要竞争对手：Kalshi

### 基础知识（必读）
1. **开户**：连接钱包（MetaMask/Phantom等）
2. **充值**：需要 USDC on Polygon 网络
3. **交易**：选市场 → 买 YES 或 NO → 等待结算
4. **卖出**：结果出来前随时可以卖出
5. **结算**：市场按规则判定结果

### 重要平台概念
- **订单簿**：显示买卖盘口
- **流动性**：市场深度影响价差
- **限价单**：设置目标价格
- **Market Maker 奖励**：为市场提供流动性可获奖励

### Top 5 热门市场（2026年3月）
| 市场 | 交易量 | 领先预测 |
|------|--------|----------|
| 2028 民主党候选人 | $785M | Gavin Newsom 25.2% |
| 2026 NBA 冠军 | $378M | OKC Thunder 35.5% |
| 2028 美国总统 | $376M | JD Vance 21% |
| 2028 GOP 候选人 | $366M | RFK Jr 49% |
| EPL 2025-26 冠军 | $326M | Arsenal 80.5% |

### 盈利策略

#### 1. 赢家三要素（基础）
- 原创研究（不是凭感觉）
- 仓位计算（控制风险）
- 市场选择（选对市场比方向更重要）
- **收益**：200-400% 年化

#### 2. 套利策略（进阶）
- Polymarket-Kalshi 之间的价格差异
- Opinion、Probable Markets 等新平台
- AlertPilot 工具（alertpilot.io）- 找套利机会
- ArbBets - 另一个 arb finder
- **注意**：2026 年 Polymarket 更新了规则，传统套利利润下降

#### 3. Delta-Neutral Strategy（专业）
- 同时在 Polymarket 和 Kalshi 对冲
- 产生交易量同时保持资本安全
- 目标：$10k+ 交易量

#### 4. Copy Trading
- 复制顶级交易员策略
- Polycule Bot (polycule.trade)
- TradeFox

### Airdrop 机会（重大！）

#### Polymarket 空投
- **已确认**：CMO 官方确认
- **估值**：$90 亿
- **可能是 DeFi 史上最大分配**
- **策略**：
  - 产生交易量
  - Market Maker 奖励
  - 避免 Sybil（一个钱包做多笔小额交易会被禁）

#### 其他预测市场空投
1. **Kalshi** - Stake Trade 空投
2. **Probable Markets** - YZI Labs 支持
3. **Opinion Trade** - 新平台
4. **Limitless** - 另一个预测市场
5. **Hyperliquid Season 3** - 有关联但不是直接的 Polymarket

#### Airdrop 挖矿工具
- AlertPilot（套利工具）
- AirdropSea（200+ 空投目录）
- OddsHuntr（统计机会发现）
- Waypoint Tools（市场分析）

### 高级功能
- **API 交易**：Python/TypeScript/Rust 写 bot
- **自动化**：PolyBot TBot v4.1
- **GitHub 开源 Bot**：BenjaminCup Bot Suite
- **风险**：开源 Bot 可能盗私钥，只用可信来源

### 争议与风险

#### 假新闻问题
- 预测市场被批评驱动假新闻
- 用户群体有偏差（年轻男性为主）
- Better Markets："没有内幕信息，用户并不比其他人更可能知道结果"

#### 道德争议
- 2026年4月：Polymarket 开设美国飞行员救援投注（被撤下）
- 批评：不应该对真实悲剧下注

### 新手常见错误（必看！）
1. ❌ 不读规则（#1 错误）
2. ❌ 把预测市场当赌博
3. ❌ 不使用工具
4. ❌ 用 VPN 违反规则
5. ❌ 下载未知来源的 Bot
6. ❌ copy trading 作为主要策略（延迟问题）

### 安全提示
- 使用官方 Polymarket API
- 只用可信 Bot（Crubble AI、BenjaminCup 等验证过的）
- 不要用"保证盈利"的 Bot
- 钱包安全：硬件钱包优于热钱包

### 视频来源（33个已学习）
- Crypto Gorilla - Polymarket 专业教程
- PredictLab - 策略和社区
- Hustle - 空投策略专家
- evg capital - 套利教程
- BenjaminCup - 开源 Bot
- Bitcoin.com - 加密新闻
- Daily DeFranco - 新闻评论
- 大量空投/套利教程（多语言）

### 文档已保存
`~/.openclaw/workspace/youtube-docs/polymarket/` - 33个文档

---

## MiniMax 平台知识（2026-04-08 学习）

### 接入方式
MiniMax 通过 Anthropic SDK 接入，base URL: `https://api.minimaxi.com/anthropic`

### 文本模型（与OpenClaw相关）

| 模型 | 上下文 | 速度 | 介绍 |
|------|--------|------|------|
| **MiniMax-M2.7** | 204,800 tokens | ~60 TPS | 旗舰，自我迭代 |
| **MiniMax-M2.7-highspeed** | 204,800 tokens | ~100 TPS | 极速版，效果不变 |
| **MiniMax-M2.5** | 204,800 tokens | ~60 TPS | 高性价比 |
| **MiniMax-M2.5-highspeed** | 204,800 tokens | ~100 TPS | 极速版 |
| **MiniMax-M2-her** | — | — | 角色扮演/多轮对话专用 |
| **MiniMax-M2** | — | — | 编码/Agent工作流 |

### 高频速版本说明
- highspeed 版本效果与原版完全一致，只是速度更快（60→100 TPS）
- 但有套餐限制：普通套餐不支持 highspeed（报错 2061）
- 小Joe的套餐可能不支持M2.7-highspeed

### 多模态能力
- **语音合成**：Speech-2.8-HD/Turbo，Speech-2.6-HD/Turbo
- **语音克隆**：Voice Cloning API，支持音色快速复刻
- **图片生成**：image-01，image-01-live（手绘/卡通增强）
- **视频生成**：MiniMax Hailuo 2.3/02，文生视频/图生视频/首尾帧
- **音乐生成**：music-2.5+（纯音乐）

### Prompt缓存（重要）
- 支持 Anthropic 格式的 `cache_control` 断点
- 缓存生命周期：5分钟，每次访问自动刷新
- 缓存读取价格：基础输入的 0.1倍
- 对长时间多轮对话/重复任务非常有用

### OpenClaw配置
当前使用 `minimax/MiniMax-M2.7` 模型（通过Anthropic兼容接口）
- OpenClaw 的 `image_generate` 工具配置的是 MiniMax 图片生成（image-01）


---

## Polymarket API 深度知识（2026-04-08 学习）

### 官方文档
docs.polymarket.com（国内访问受限，需梯子）
官方Agent Skills: github.com/Polymarket/agent-skills

### API架构

**四个API服务：**
| API | Base URL | 认证 | 用途 |
|-----|----------|------|------|
| CLOB | https://clob.polymarket.com | 交易端需L2 | 订单簿、价格、订单管理 |
| Gamma | https://gamma-api.polymarket.com | 无 | 市场发现、元数据、事件 |
| Data | https://data-api.polymarket.com | 无 | 用户持仓、交易历史 |
| Bridge | https://bridge.polymarket.com | 有 | 跨链充值提现 |

**WebSocket实时通道：**
| 通道 | URL | 认证 | 用途 |
|------|-----|------|------|
| Market WS | wss://ws-subscriptions-clob.polymarket.com/ws/market | 无 | 订单簿更新、价格变化 |
| User WS | wss://ws-subscriptions-clob.polymarket.com/ws/user | API creds | 订单成交、取消 |
| Sports WS | wss://sports-api.polymarket.com/ws | 无 | 实时比赛比分 |
| RTD | wss://ws-live-data.polymarket.com | 可选 | 加密价格 |

### 核心概念

**数据层级：** Series → Event → Market → Outcomes(YES/NO)
**Condition ID**：市场标识 | **Token ID**：结果代币标识
**价格**：0.00～1.00（概率）| YES+NO≈$1.00（偏差=套利机会）

**链上**：Polygon + CTF(ERC-1155) + USDC.e抵押
**CLOB**：混合去中心化（链下撮合+链上结算），订单签名用EIP-712

### 认证：L1(钱包EIP-712签名) → L2(HMAC-SHA256)
钱包类型：EOA(0)、POLY_PROXY(1)、GNOSIS_SAFE(2-最常见)

### SDK：py-clob-client(Python)、@polymarket/clob-client(TypeScript)

### 智能合约
USDC.e: 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174
CTF: 0x4D97DCd97eC945f40cF65F87097ACe5EA0476045

### 订单类型
GTC(挂单)、FOK(立即全成)、FAK(立即成交剩余撤)、Post-only(maker)
Rate limit: ~10 req/s下单

### OpenClaw集成价值
- 抓取实时价格/订单簿（无需认证）
- 自动抓取热门市场数据
- 交易信号监控


## 今日新增（2026-04-09）

### 飞书接入完成
- App ID: cli_a93d5c431cf99cb6
- 理查现在可通过飞书直接对话
- pairing 已通过飞书账号 ou_73c905616ebd957129e49829c3abc23f

### Mac 工具更新
- **cliclick 5.1** — GUI 自动化（需辅助功能权限）
- **Python 3.11** — 解决 SSL 兼容问题
- **Mem0 1.0.11** — AI 记忆持久化层（pip）
- **youtube-transcript-api** — YouTube 字幕抓取
- **Chrome headless** — HTML → PDF 转换

### 健身 PR（2026-04-09）
- 卧推：100kg / 深蹲：110kg / 硬拉：140kg

### AI Agents 课程路径（Microsoft）
路径：~/Downloads/ai-agents-for-beginners/
推荐：13(Agent Memory) → 04(Tool Use) → 05(Agentic RAG) → 08(Multi-Agent)

### GitHub Trending Top5（2026-04-09）
1. AutoGPT 183K — 自主代理框架
2. Langflow 146K — 可视化拖拽构建器
3. Dify 136K — 生产级代理工作流
4. LangChain 132K — 基础代理工程平台
5. Gemini CLI 100K — Google 终端代理
（OpenClaw 已超越 React，250K+ stars）

## 今日完成（2026-04-09）
- 飞书接入完成（pairing 已通过）
- pandoc 3.7.0.1 安装（PDF 转换能力）
- cliclick 5.1 安装（GUI 自动化）
- ClawHub Skills 安装：polymarket-api、polymarket-trade、morning-daily-briefing、ai-daily-briefing、macos-calendar、ranked-gym
- Polymarket API 知识深化
- PPL 训练方案（170cm/70kg/PR基准）
- 每日简报格式最终确认
- 理查正式命名

## 今日教训
- Python 3.13 SSL 兼容性问题（用 3.11 解决）
- YouTube API IP 封锁（无解，需手动）
- ClawHub 可疑 Skill 不轻易装（VirusTotal 标记）
- 钥匙串密码绝对不能给

## 2026-04-10 新增

### session-wrap-up skill 完成
- 自己写了个简化版：`~/.openclaw/skills/session-wrap-up/`
- Phase 1（Git）用 shell 脚本自动化
- Phase 2-4 由理查直接做
- 今天是第一次正式跑，21 个文件 commit

### 飞书+webchat 会话不共享 context
- 跨 channel 的会话 history 需要单独读文件
- 首次会话应主动检查其他 channel 的重要内容

### 日历名称问题（已解决）
- 中文 macOS 日历名称是「日历」
- skill 默认填的 "Calendar" 不匹配

## 待处理
- [ ] 辅助功能权限（Terminal → 系统设置 → 辅助功能）
- [ ] Mem0 接入记忆系统
- [ ] Polymarket Agentic RAG
- [ ] 简报多代理架构
