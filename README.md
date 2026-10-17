# 定时抓取Github Trending里的数据

作为一个间歇性“松鼠症”患者，有时候会花几个小时逛Github Trending，生怕漏掉什么重要的东西，说到底是心理作用罢了。

而这个Github Trend爬虫，就是我给自己开的一味药，都收集起来，就不怕漏掉啥了（虽然这个逻辑经不起推敲，不过确实部署这个爬虫之后，我再也没有逛过Github Trend）

* 基于[Github Actions](https://docs.github.com/en/actions)的爬虫
* 使用[click](https://github.com/pallets/click)实现了命令行参数
* 使用[Crontab Guru](https://crontab.guru/)来设置定时参数

# Repos
## 今日TOP10 
<!-- START OF DAILY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 ready-to-use validated skills plus 100+ scientific databases covering biology, chemistry, medicine, and drug discovery. Compatible with Cursor, Claude Code, Codex, Pi, Antigravity, and the open Agent Skills standard. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub:https://clianything.cc/ |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks. |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated |
| [android/skills](https://github.com/android/skills) |  |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor plugin specification and official plugins |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [morluto/rea](https://github.com/morluto/rea) | Reverse engineer anything with agents, from app behavior down to native binaries. |
| [storytold/artcraft](https://github.com/storytold/artcraft) | ArtCraft is an intentional crafting engine for artists, designers, and filmmakers |
| [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | Tool for automatic PS5 executables porting to Linux and Windows |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, and Pi. 44 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop. |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Write HTML. Render video. Built for agents. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .agents directory. |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | Ghidra is a software reverse engineering (SRE) framework |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks. |
| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | A context-compression plugin for small context windows (a 100K context is enough), token savings (5x fewer tokens), and month-long single sessions (billions of tokens).上下文压缩插件，兼顾小窗口(100k上下文足矣)省token(省5倍token)和超长会话(数月级别几十亿token单会话)。billion-context is all you need |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | The open-source app everyone uses to manage agents at work |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) |  |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Write HTML. Render video. Built for agents. |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Hindsight: Agent Memory That Learns |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [agent-substrate/substrate](https://github.com/agent-substrate/substrate) | Agent Substrate: the core system |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks. |
<!-- END OF MONTHLY_TOP10_REPOS -->
