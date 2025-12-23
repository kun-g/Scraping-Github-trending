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
| [exo-explore/exo](https://github.com/exo-explore/exo) | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | Collection of publicly available IPTV channels from all over the world |
| [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | A list of useful payloads and bypass for Web Application Security and Pentest/CTF |
| [GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT) | A GPT-empowered penetration testing tool |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | Data transformation framework for AI. Ultra performant, with incremental processing. 🌟 Star if you like it! |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | Fabric is an open-source framework for augmenting humans using AI. It provides a modular system for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | An Open Source Machine Learning Framework for Everyone |
| [rendercv/rendercv](https://github.com/rendercv/rendercv) | Typst-based CV/resume generator for academics and engineers |
| [home-assistant/core](https://github.com/home-assistant/core) | 🏡 Open source home automation that puts local control and privacy first. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [exo-explore/exo](https://github.com/exo-explore/exo) | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Open-source platform to build and deploy AI agent workflows. |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [Morganamilo/paru](https://github.com/Morganamilo/paru) | Feature packed AUR helper |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | SoTA open-source TTS |
| [ZJU-LLMs/Foundations-of-LLMs](https://github.com/ZJU-LLMs/Foundations-of-LLMs) | A book for Learning the Foundations of LLMs |
| [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | Personal AI Infrastructure for upgrading humans. |
| [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | A research prototype of a human-centered web agent |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 🎯 告别信息过载，AI 助你看懂新闻资讯热点，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等13种工具）。支持企业微信/个人微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 推送，1分钟手机通知，无需编程。支持Docker部署，支持数据远程云存储⭐ 让算法为你服务，用AI理解热点 |
| [trustedsec/social-engineer-toolkit](https://github.com/trustedsec/social-engineer-toolkit) | The Social-Engineer Toolkit (SET) repository from TrustedSec - All new versions of SET will be deployed here. |
| [facebookresearch/sam3](https://github.com/facebookresearch/sam3) | The repository provides code for running inference and finetuning with the Meta Segment Anything Model 3 (SAM 3), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | AGENTS.md — a simple, open format for guiding coding agents |
| [sst/opencode](https://github.com/sst/opencode) | The open source coding agent. |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | LLM-powered framework for deep document understanding, semantic retrieval, and context-aware answers using RAG paradigm. |
<!-- END OF MONTHLY_TOP10_REPOS -->
