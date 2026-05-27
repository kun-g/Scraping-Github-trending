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
| [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Learn it. Build it. Ship it for others. |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 754 structured cybersecurity skills for AI agents · Mapped to 5 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND & NIST AI RMF · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 26 security domains · Apache 2.0 |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | A skill file for removing AI tells from prose |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop |
| [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | DigitalPlat FreeDomain: Free Domain For Everyone |
| [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | The Free Software Media System - Server Backend & API |
| [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | Curated list of the best free apps for PC and mobile |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Pre-indexed code knowledge graph for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, and Hermes Agent — fewer tokens, fewer tool calls, 100% local |
| [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Learn it. Build it. Ship it for others. |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Your Personal AI super intelligence. Private, Simple and extremely powerful. |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video. |
| [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | "ViMax: Agentic Video Generation (Director, Screenwriter, Producer, and Video Generator All-in-One)" |
| [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | #1 Persistent memory for AI coding agents based on real-world benchmarks |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more |
| [NVlabs/Sana](https://github.com/NVlabs/Sana) | SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Pre-indexed code knowledge graph for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, and Hermes Agent — fewer tokens, fewer tool calls, 100% local |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) |  |
| [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. |
| [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | #1 Persistent memory for AI coding agents based on real-world benchmarks |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Academic Research Skills for Claude Code: research → write → review → revise → finalize |
| [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more. |
| [soxoj/maigret](https://github.com/soxoj/maigret) | 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
<!-- END OF MONTHLY_TOP10_REPOS -->
