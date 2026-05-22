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
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode — fewer tokens, fewer tool calls, 100% local |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [dotnet/skills](https://github.com/dotnet/skills) | Repository for skills to assist AI coding agents with .NET and C# |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub:https://clianything.cc/ |
| [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | Free, Open Source, Self-Hosted WhatsApp API Gateway |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for coding agents |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Learn it. Build it. Ship it for others. |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Your Personal AI super intelligence. Private, Simple and extremely powerful. |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode — fewer tokens, fewer tool calls, 100% local |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX. |
| [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | #1 Persistent memory for AI coding agents based on real-world benchmarks |
| [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video. |
| [oven-sh/bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | 💻 vibe coding 2026 | Your first modern Coding course for beginners to master step by step. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported) |
| [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. |
| [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | #1 Persistent memory for AI coding agents based on real-world benchmarks |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) |  |
| [huggingface/ml-intern](https://github.com/huggingface/ml-intern) | 🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode — fewer tokens, fewer tool calls, 100% local |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | 🚀 AI 全自动短视频引擎 | AI Fully Automated Short Video Engine |
| [soxoj/maigret](https://github.com/soxoj/maigret) | 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites |
<!-- END OF MONTHLY_TOP10_REPOS -->
