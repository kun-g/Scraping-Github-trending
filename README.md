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
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [KaijuEngine/kaiju](https://github.com/KaijuEngine/kaiju) | General purpose 3D and 2D game engine using Go (golang) and Vulkan with built in editor |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | AGENTS.md — a simple, open format for guiding coding agents |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Open-Source Frontier Voice AI |
| [block/goose](https://github.com/block/goose) | an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM |
| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
| [cloudflare/vibesdk](https://github.com/cloudflare/vibesdk) | An open-source vibe coding platform that helps you build your own vibe-coding platform, built entirely on Cloudflare stack |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [basecamp/fizzy](https://github.com/basecamp/fizzy) | Kanban as it should be. Not as it has been. |
| [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization. |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [oven-sh/bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [microsoft/typescript-go](https://github.com/microsoft/typescript-go) | Staging repo for development of native port of TypeScript |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [vercel/next.js](https://github.com/vercel/next.js) | The React Framework |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [lynx-family/lynx](https://github.com/lynx-family/lynx) | Empower the Web community and invite more to build across platforms. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 🎯 告别信息过载，AI 助你看懂新闻资讯热点，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等13种工具）。支持企业微信/个人微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 推送，1分钟手机通知，无需编程。支持Docker部署⭐ 让算法为你服务，用AI理解热点 |
| [kavishdevar/librepods](https://github.com/kavishdevar/librepods) | AirPods liberated from Apple's ecosystem. |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Open-Source Frontier Voice AI |
| [google/adk-go](https://github.com/google/adk-go) | An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [usestrix/strix](https://github.com/usestrix/strix) | Open-source AI agents for penetration testing |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | A research prototype of a human-centered web agent |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit) | The ultimate training toolkit for finetuning diffusion models |
<!-- END OF MONTHLY_TOP10_REPOS -->
