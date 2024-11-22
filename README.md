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
| [twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [webvm](https://github.com/leaningtech/webvm) | Virtual Machine for the Web |
| [multi-agent-orchestrator](https://github.com/awslabs/multi-agent-orchestrator) | Flexible and powerful framework for managing multiple AI agents and handling complex conversations |
| [go-blueprint](https://github.com/Melkeydev/go-blueprint) | Go-blueprint allows users to spin up a quick Go project using a popular framework |
| [maxun](https://github.com/getmaxun/maxun) | 🔥 Open-source no-code web data extraction platform. Turn websites to APIs and spreadsheets with no-code robots in minutes! [In Beta] |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [screenpipe](https://github.com/mediar-ai/screenpipe) | rewind.ai x cursor.com = your AI assistant that has all the context. 24/7 screen & voice recording for the age of super intelligence. get your data ready or be left behind |
| [data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [FreeCAD](https://github.com/FreeCAD/FreeCAD) | This is the official source code of FreeCAD, a free and opensource multiplatform 3D parametric modeler. |
| [InfoSec-Black-Friday](https://github.com/0x90n/InfoSec-Black-Friday) | All the deals for InfoSec related software/tools this Black Friday |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [exo](https://github.com/exo-explore/exo) | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |
| [ai-chatbot](https://github.com/vercel/ai-chatbot) | A full-featured, hackable Next.js AI chatbot built by Vercel |
| [GetQzonehistory](https://github.com/LibraHp/GetQzonehistory) | 获取QQ空间发布的历史说说 |
| [next-forge](https://github.com/haydenbleasel/next-forge) | Production-grade Turborepo template for Next.js apps. |
| [autogen](https://github.com/microsoft/autogen) | A programming framework for agentic AI 🤖 |
| [eliza](https://github.com/ai16z/eliza) | Conversational Agent for Twitter and Discord |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🙌 OpenHands: Code Less, Make More |
| [LocalAI](https://github.com/mudler/LocalAI) | 🤖 The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI, running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed, P2P inference |
| [bbot](https://github.com/blacklanternsecurity/bbot) | A recursive internet scanner for hackers. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [BitNet](https://github.com/microsoft/BitNet) | Official inference framework for 1-bit LLMs |
| [docling](https://github.com/DS4SD/docling) | Get your documents ready for gen AI |
| [windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Agents with memory, knowledge, tools and reasoning. Chat with them using a beautiful Agent UI. |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [social-app](https://github.com/bluesky-social/social-app) | The Bluesky Social application for Web, iOS, and Android |
| [ai-chatbot](https://github.com/vercel/ai-chatbot) | A full-featured, hackable Next.js AI chatbot built by Vercel |
| [apihub](https://github.com/hiteshchoudhary/apihub) | Your own API Hub to learn and master API interaction. Ideal for frontend, mobile dev and backend developers. |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database diagram editor and SQL generator. |
<!-- END OF MONTHLY_TOP10_REPOS -->
