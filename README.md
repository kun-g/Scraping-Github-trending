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
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | ✨ Fully autonomous AI Agents system capable of performing complex penetration testing tasks |
| [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | Build ultra fast, tiny, and cross-platform desktop apps with Typescript. |
| [HailToDodongo/pyrite64](https://github.com/HailToDodongo/pyrite64) | N64 Game-Engine and Editor using libdragon & tiny3d |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more |
| [PostHog/posthog](https://github.com/PostHog/posthog) | 🦔 PostHog is an all-in-one developer platform for building successful products. We offer product analytics, web analytics, session replay, error tracking, feature flags, experimentation, surveys, data warehouse, a CDP, and an AI product assistant to help debug your code, ship features faster, and keep all your usage and customer data in one stack. |
| [eslint/eslint](https://github.com/eslint/eslint) | Find and fix problems in your JavaScript code. |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
| [Effect-TS/effect-smol](https://github.com/Effect-TS/effect-smol) | Core libraries and experimental work for Effect v4 |
| [google-research/timesfm](https://github.com/google-research/timesfm) | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [alibaba/zvec](https://github.com/alibaba/zvec) | A lightweight, lightning-fast, in-process vector database |
| [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | Open-source AI coworker, with memory |
| [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0 |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Fully automatic censorship removal for language models |
| [steipete/summarize](https://github.com/steipete/summarize) | Point at any URL/YouTube/Podcast or file. Get the gist. CLI and Chrome Extension. |
| [github/gh-aw](https://github.com/github/gh-aw) | GitHub Agentic Workflows |
| [steipete/gogcli](https://github.com/steipete/gogcli) | Google Suite CLI: Gmail, GCal, GDrive, GContacts. |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 66 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer. |
| [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | Production-ready implementation of InvisPose - a revolutionary WiFi-based dense human pose estimation system that enables real-time full-body tracking through walls using commodity mesh routers |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for coding agents |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | Fully autonomous AI hacker to find actual exploits in your web apps. Shannon has achieved a 96.15% success rate on the hint-free, source-aware XBOW Benchmark. |
| [tobi/qmd](https://github.com/tobi/qmd) | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [openai/skills](https://github.com/openai/skills) | Skills Catalog for Codex |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [steipete/gogcli](https://github.com/steipete/gogcli) | Google Suite CLI: Gmail, GCal, GDrive, GContacts. |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 🎥 Make videos programmatically with React |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
<!-- END OF MONTHLY_TOP10_REPOS -->
