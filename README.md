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
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Fully automatic censorship removal for language models |
| [seerr-team/seerr](https://github.com/seerr-team/seerr) | Open-source media request and discovery manager for Jellyfin, Plex, and Emby. |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [steipete/gogcli](https://github.com/steipete/gogcli) | Google Suite CLI: Gmail, GCal, GDrive, GContacts. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | A lightweight, lightning-fast, in-process vector database |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0 |
| [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | Learn System Design concepts and prepare for interviews using free resources. |
| [steipete/summarize](https://github.com/steipete/summarize) | Point at any URL/YouTube/Podcast or file. Get the gist. CLI and Chrome Extension. |
| [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | Open source software that helps you create and deploy high-frequency crypto trading bots |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [github/gh-aw](https://github.com/github/gh-aw) | GitHub Agentic Workflows |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 66 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer. |
| [google/langextract](https://github.com/google/langextract) | A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Fully automatic censorship removal for language models |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for coding agents |
| [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | Agentic AI Infrastructure for magnifying HUMAN capabilities. |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [steipete/summarize](https://github.com/steipete/summarize) | Point at any URL/YouTube/Podcast or file. Get the gist. CLI and Chrome Extension. |
| [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | Generative UI SDK for React |
| [steipete/gogcli](https://github.com/steipete/gogcli) | Google Suite CLI: Gmail, GCal, GDrive, GContacts. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | Fully autonomous AI hacker to find actual exploits in your web apps. Shannon has achieved a 96.15% success rate on the hint-free, source-aware XBOW Benchmark. |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 🎥 Make videos programmatically with React |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [openai/skills](https://github.com/openai/skills) | Skills Catalog for Codex |
| [tobi/qmd](https://github.com/tobi/qmd) | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [steipete/gogcli](https://github.com/steipete/gogcli) | Google Suite CLI: Gmail, GCal, GDrive, GContacts. |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
<!-- END OF MONTHLY_TOP10_REPOS -->
