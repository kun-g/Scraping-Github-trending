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
| [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) |  Now we have become very big, Different from the original idea. Collect premium software in various categories. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [NVIDIA-NeMo/Gym](https://github.com/NVIDIA-NeMo/Gym) | Build RL environments for LLM training |
| [GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT) | A GPT-empowered penetration testing tool |
| [exo-explore/exo](https://github.com/exo-explore/exo) | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |
| [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | A list of useful payloads and bypass for Web Application Security and Pentest/CTF |
| [sgl-project/mini-sglang](https://github.com/sgl-project/mini-sglang) |  |
| [google/adk-js](https://github.com/google/adk-js) | An open-source, code-first Typescript toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [afshinea/stanford-cs-229-machine-learning](https://github.com/afshinea/stanford-cs-229-machine-learning) | VIP cheatsheets for Stanford's CS 229 Machine Learning |
| [metabase/metabase](https://github.com/metabase/metabase) | The easy-to-use open source Business Intelligence and Embedded Analytics tool that lets everyone work with data 📊 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Open-source platform to build and deploy AI agent workflows. |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization. |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | LLM-powered framework for deep document understanding, semantic retrieval, and context-aware answers using RAG paradigm. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [tursodatabase/turso](https://github.com/tursodatabase/turso) | Turso is an in-process SQL database, compatible with SQLite. |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | AGENTS.md — a simple, open format for guiding coding agents |
| [jellyfin/jellyfin-desktop](https://github.com/jellyfin/jellyfin-desktop) | Jellyfin Desktop Client |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for coding agents |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [facebookresearch/sam3](https://github.com/facebookresearch/sam3) | The repository provides code for running inference and finetuning with the Meta Segment Anything Model 3 (SAM 3), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. |
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 🎯 告别信息过载，AI 助你看懂新闻资讯热点，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等13种工具）。支持企业微信/个人微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 推送，1分钟手机通知，无需编程。支持Docker部署，支持数据远程云存储⭐ 让算法为你服务，用AI理解热点 |
| [kavishdevar/librepods](https://github.com/kavishdevar/librepods) | AirPods liberated from Apple's ecosystem. |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | A research prototype of a human-centered web agent |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [facebookresearch/sam-3d-body](https://github.com/facebookresearch/sam-3d-body) | The repository provides code for running inference with the SAM 3D Body Model (3DB), links for downloading the trained model checkpoints and datasets, and example notebooks that show how to use the model. |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | AGENTS.md — a simple, open format for guiding coding agents |
| [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit) | The ultimate training toolkit for finetuning diffusion models |
<!-- END OF MONTHLY_TOP10_REPOS -->
