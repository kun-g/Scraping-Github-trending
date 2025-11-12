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
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 🎯 告别信息过载，AI 助你看懂新闻资讯热点，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等13种工具）。支持企业微信/飞书/钉钉/Telegram/邮件/ntfy推送，30秒网页部署，1分钟手机通知，无需编程。支持Docker部署⭐ 让算法为你服务，用AI理解热点 |
| [google/adk-go](https://github.com/google/adk-go) | An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [usestrix/strix](https://github.com/usestrix/strix) | ✨ Open-source AI hackers for your apps 👨🏻‍💻 |
| [bobeff/open-source-games](https://github.com/bobeff/open-source-games) | A list of open source games. |
| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 所有小初高、大学PDF教材。 |
| [serverless-dns/serverless-dns](https://github.com/serverless-dns/serverless-dns) | The RethinkDNS resolver that deploys to Cloudflare Workers, Deno Deploy, Fastly, and Fly.io |
| [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application on your personal device. |
| [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 12 Lessons to Get Started Building AI Agents |
| [LizardByte/Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host for Moonlight. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
| [usestrix/strix](https://github.com/usestrix/strix) | ✨ Open-source AI hackers for your apps 👨🏻‍💻 |
| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | Automate browser based workflows with AI |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🤖 The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI, running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference |
| [nocobase/nocobase](https://github.com/nocobase/nocobase) | NocoBase is the most extensible AI-powered no-code/low-code platform for building business applications and enterprise solutions. |
| [lima-vm/lima](https://github.com/lima-vm/lima) | Linux virtual machines, with a focus on running containers |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [sst/opentui](https://github.com/sst/opentui) | OpenTUI is a library for building terminal user interfaces (TUIs) |
| [opencloud-eu/opencloud](https://github.com/opencloud-eu/opencloud) | 🌤️This is the main repository of the OpenCloud server. It contains the golang codebase for the backend services. |
| [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | Free universal database tool and SQL client |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [usestrix/strix](https://github.com/usestrix/strix) | ✨ Open-source AI hackers for your apps 👨🏻‍💻 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Generate audiobooks from e-books, voice cloning & 1107+ languages! |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [minio/minio](https://github.com/minio/minio) | MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. |
| [servo/servo](https://github.com/servo/servo) | Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications. |
<!-- END OF MONTHLY_TOP10_REPOS -->
