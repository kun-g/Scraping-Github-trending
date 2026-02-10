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
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | Fully autonomous AI hacker to find actual exploits in your web apps. Shannon has achieved a 96.15% success rate on the hint-free, source-aware XBOW Benchmark. |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research |
| [pydantic/monty](https://github.com/pydantic/monty) | A minimal, secure Python interpreter written in Rust for use by AI |
| [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | 基于多智能体LLM的中文金融交易框架 - TradingAgents中文增强版 |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Free, local, open-source 24/7 Cowork and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [github/gh-aw](https://github.com/github/gh-aw) | GitHub Agentic Workflows |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [gitbutlerapp/gitbutler](https://github.com/gitbutlerapp/gitbutler) | The GitButler version control client, backed by Git, powered by Tauri/Rust/Svelte |
| [microsoft/litebox](https://github.com/microsoft/litebox) | A security-focused library OS supporting kernel- and user-mode execution |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | Fully autonomous AI hacker to find actual exploits in your web apps. Shannon has achieved a 96.15% success rate on the hint-free, source-aware XBOW Benchmark. |
| [openai/skills](https://github.com/openai/skills) | Skills Catalog for Codex |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | Master Claude Code Hooks |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research |
| [tobi/qmd](https://github.com/tobi/qmd) | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
| [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | The best ChatGPT that $100 can buy. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | The open source coding agent. |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Free, local, open-source 24/7 Cowork and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 🎥 Make videos programmatically with React |
| [openai/skills](https://github.com/openai/skills) | Skills Catalog for Codex |
| [tobi/qmd](https://github.com/tobi/qmd) | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
<!-- END OF MONTHLY_TOP10_REPOS -->
