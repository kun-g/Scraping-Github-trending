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
| [morluto/rea](https://github.com/morluto/rea) | Reverse engineer anything with agents, from app behavior down to native binaries. |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks. |
| [storytold/artcraft](https://github.com/storytold/artcraft) | ArtCraft is an intentional crafting engine for artists, designers, and filmmakers |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, and Pi. 44 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop. |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | AirLLM 2.8T LLM inference with single 4GB GPU |
| [microsoft/BitNet](https://github.com/microsoft/BitNet) | Official inference framework for 1-bit LLMs |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly) |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | Tool for automatic PS5 executables porting to Linux and Windows |
| [tester-army/e2e](https://github.com/tester-army/e2e) | Next generation e2e testing framework for web and mobile apps. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .agents directory. |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Write HTML. Render video. Built for agents. |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More |
| [flutter/flutter](https://github.com/flutter/flutter) | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor plugin specification and official plugins |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Give your agent CAD superpowers. |
| [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | Build your own network of agents from Claude Code, Codex and Pi: persistent teams with roles, shared context and owned work. |
| [morluto/rea](https://github.com/morluto/rea) | Reverse engineer anything with agents, from app behavior down to native binaries. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages. |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | The open-source app everyone uses to manage agents at work |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) |  |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Hindsight: Agent Memory That Learns |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki. |
| [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | A smarter, self-hosted AI assistant — multi-user, multi-agent. |
<!-- END OF MONTHLY_TOP10_REPOS -->
