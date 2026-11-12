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
| [meta/astryx](https://github.com/meta/astryx) | An open source design system that's fully customizable and agent ready |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. |
| [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) |  |
| [shadcn/improve](https://github.com/shadcn/improve) | Use your most capable model to audit your codebase and write plans for cheaper models to execute. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Production-grade engineering skills for AI coding agents. |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Browser automation CLI for AI agents |
| [we-promise/sure](https://github.com/we-promise/sure) | The personal finance app for everyone (by everyone) |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants. |
| [openai/codex-security](https://github.com/openai/codex-security) | OpenAI's Codex Security CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities. npm:https://www.npmjs.com/package/@openai/codex-security |
| [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) | All Algorithms implemented in Java |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables deterministic query generation, better context retrieval, and more explainable AI for LLM and agent workflows. |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Computer use CLI for AI agents |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Open-source Grok Bot alternative with a virtual machine that bots can use |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Browser automation CLI for AI agents |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .agents directory. |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 🕷️ The BEST Web Scraping framework that handles everything from a single request to a full-scale crawl! Don't be shy, join here:https://discord.gg/EMgGbDceNQand follow here for daily tips and tricks:https://x.com/Scrapling_dev |
| [zed-industries/zed](https://github.com/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [morluto/rea](https://github.com/morluto/rea) | Reverse engineer anything with agents, from app behavior down to native binaries. |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Anti-AI-slop design skill for Claude Code, Cursor, and Codex. |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) |  |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Write HTML. Render video. Built for agents. |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships. |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | DeepTutor: Lifelong Personalized Tutoring.https://deeptutor.info/. |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages. |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
<!-- END OF MONTHLY_TOP10_REPOS -->
