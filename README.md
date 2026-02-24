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
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models |
| [huggingface/skills](https://github.com/huggingface/skills) |  |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Financial data platform for analysts, quants and AI agents. |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, or debugging agent systems that require effective context management. |
| [f/prompts.chat](https://github.com/f/prompts.chat) | a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy. |
| [CompVis/stable-diffusion](https://github.com/CompVis/stable-diffusion) | A latent text-to-image diffusion model |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration |
| [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | Stremio - Freedom to Stream |
| [stan-smith/FossFLOW](https://github.com/stan-smith/FossFLOW) | Make beautiful isometric infrastructure diagrams |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Fully automatic censorship removal for language models |
| [alibaba/zvec](https://github.com/alibaba/zvec) | A lightweight, lightning-fast, in-process vector database |
| [huggingface/skills](https://github.com/huggingface/skills) |  |
| [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0 |
| [google-research/timesfm](https://github.com/google-research/timesfm) | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models |
| [seerr-team/seerr](https://github.com/seerr-team/seerr) | Open-source media request and discovery manager for Jellyfin, Plex, and Emby. |
| [cloudflare/agents](https://github.com/cloudflare/agents) | Build and deploy AI Agents on Cloudflare |
| [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | Open-source AI coworker, with memory |
| [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | Stremio - Freedom to Stream |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | Fully autonomous AI hacker to find actual exploits in your web apps. Shannon has achieved a 96.15% success rate on the hint-free, source-aware XBOW Benchmark. |
| [tobi/qmd](https://github.com/tobi/qmd) | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
| [openai/skills](https://github.com/openai/skills) | Skills Catalog for Codex |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [steipete/gogcli](https://github.com/steipete/gogcli) | Google Suite CLI: Gmail, GCal, GDrive, GContacts. |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Fully automatic censorship removal for language models |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
<!-- END OF MONTHLY_TOP10_REPOS -->
