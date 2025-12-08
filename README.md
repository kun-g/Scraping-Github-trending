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
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Open-Source Frontier Voice AI |
| [NVIDIA/cutile-python](https://github.com/NVIDIA/cutile-python) | cuTile is a programming model for writing parallel kernels for NVIDIA GPUs |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |
| [TelegramMessenger/Telegram-iOS](https://github.com/TelegramMessenger/Telegram-iOS) | Telegram-iOS |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
| [sst/opencode](https://github.com/sst/opencode) | The open source coding agent. |
| [BeehiveInnovations/pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server) | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one. |
| [microsoft/Foundry-Local](https://github.com/microsoft/Foundry-Local) |  |
| [sinelaw/fresh](https://github.com/sinelaw/fresh) | Text editor for your terminal: easy, powerful and fast |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | A research prototype of a human-centered web agent |
| [oven-sh/bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |
| [vercel/next.js](https://github.com/vercel/next.js) | The React Framework |
| [microsoft/typescript-go](https://github.com/microsoft/typescript-go) | Staging repo for development of native port of TypeScript |
| [lynx-family/lynx](https://github.com/lynx-family/lynx) | Empower the Web community and invite more to build across platforms. |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more |
| [FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome) | The iconic SVG, font, and CSS toolkit |
| [gunnarmorling/1brc](https://github.com/gunnarmorling/1brc) | 1️⃣🐝🏎️ The One Billion Row Challenge -- A fun exploration of how quickly 1B rows from a text file can be aggregated with Java |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 🎯 告别信息过载，AI 助你看懂新闻资讯热点，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等13种工具）。支持企业微信/个人微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 推送，1分钟手机通知，无需编程。支持Docker部署⭐ 让算法为你服务，用AI理解热点【 当前仅推荐Docker部署，Fork/Actions方式暂停（正在与GitHub官方沟通中）】 |
| [kavishdevar/librepods](https://github.com/kavishdevar/librepods) | AirPods liberated from Apple's ecosystem. |
| [google/adk-go](https://github.com/google/adk-go) | An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | Open-Source Memory Engine for LLMs, AI Agents & Multi-Agent Systems |
| [usestrix/strix](https://github.com/usestrix/strix) | Open-source AI agents for penetration testing |
| [lzhoang2801/OpCore-Simplify](https://github.com/lzhoang2801/OpCore-Simplify) | A tool designed to simplify the creation of OpenCore EFI |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | A research prototype of a human-centered web agent |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 所有小初高、大学PDF教材。 |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
<!-- END OF MONTHLY_TOP10_REPOS -->
