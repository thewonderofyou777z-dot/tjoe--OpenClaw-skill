# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod

### Mac 日历

- 日历名称：「日历」（中文系统）
- AppleScript 可正常读取（2026-04-10 验证）
- 权限已授权

### memsearch（语义记忆搜索）

- 路径：`~/.venv/memsearch/bin/memsearch`
- embedding：Ollama + `nomic-embed-text`（本地）
- 向量数据库：Milvus（`~/.memsearch/milvus.db`）
- 索引目录：`~/.openclaw/workspace/memory/` + `MEMORY.md`
- Ollama 服务：`brew services start ollama`
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
