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
| [block/buzz](https://github.com/block/buzz) | A hive mind communication platform |
| [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets |
| [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin) | Empowering everyone to host fast and efficient Minecraft servers. |
| [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | The best browser for both you and your AI agents work in parallel. |
| [chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11) | Original Apollo 11 Guidance Computer (AGC) source code for the command and lunar modules. |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | A collection of agent skills for CAD, robotics and hardware design |
| [agegr/pi-web](https://github.com/agegr/pi-web) | Web UI for the pi coding agent |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo workflows. |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Anti-AI-slop design skill for Claude Code, Cursor, and Codex. |
| [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | Kimi Code CLI — The Starting Point for Next-Gen Agents |
| [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | The most intelligent agent harness for code |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | DeepTutor: Lifelong Personalized Tutoring.https://deeptutor.info/. |
| [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | Bonsai Demo |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | Skills for Design Engineers |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors |
| [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | Kimi Code CLI is your next CLI agent. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. |
| [usestrix/strix](https://github.com/usestrix/strix) | Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors |
| [catchorg/Catch2](https://github.com/catchorg/Catch2) | A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x branch) |
| [stablyai/orca](https://github.com/stablyai/orca) | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS. |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai -https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes |
| [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | agent multiplexer that lives in your terminal. |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies. |
| [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | git push no-mistakes |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly. |
<!-- END OF MONTHLY_TOP10_REPOS -->
