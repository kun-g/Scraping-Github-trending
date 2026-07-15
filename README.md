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
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 100+ AI Agent & RAG apps you can actually run — clone, customize, ship. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | The Destructive Command Guard (dcg) is for blocking dangerous git and shell commands from being executed by agents. |
| [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | The open-source CapCut alternative |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Anti-AI-slop design skill for Claude Code, Cursor, and Codex. |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | "Vibe-Trading: Your Personal Trading Agent" |
| [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | A simple, lightweight PowerShell script that allows you to remove pre-installed apps, disable telemetry, as well as perform various other changes to declutter and customize your Windows experience. Win11Debloat works for both Windows 10 and Windows 11. |
| [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | 1,324-exercise fitness dataset — animation GIFs, 180×180 thumbnails, muscle-group & equipment data, and step-by-step instructions in 6 languages. The exercise data layer behind the LogPress app. |
| [penpot/penpot](https://github.com/penpot/penpot) | Penpot: The open-source design platform for Product teams that need scalable collaboration. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. |
| [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities |
| [abseil/abseil-cpp](https://github.com/abseil/abseil-cpp) | Abseil Common Libraries (C++) |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | OfficeCLI is the first and best Office suite purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation required. |
| [stablyai/orca](https://github.com/stablyai/orca) | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile. |
| [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents. |
| [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | agent multiplexer that lives in your terminal. |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Never stop coding. Free AI gateway: one endpoint, 231+ providers (50+ free), connect Claude Code, Codex, Cursor, Cline & Copilot to FREE Claude/GPT/Gemini. RTK+Caveman stacked compression saves 15-95% tokens, smart auto-fallback, MCP/A2A, multimodal APIs, Desktop/PWA. |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | Use Codex from Claude Code to review code or delegate tasks. |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turn your AI coding assistant into a full video production studio. |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies. |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly. |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees. |
| [usestrix/strix](https://github.com/usestrix/strix) | Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. |
| [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | git push no-mistakes |
| [stablyai/orca](https://github.com/stablyai/orca) | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile. |
| [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | Google Cloud Knowledge Catalog Tools and Samples |
| [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | agent multiplexer that lives in your terminal. |
<!-- END OF MONTHLY_TOP10_REPOS -->
