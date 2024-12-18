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
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [htmx](https://github.com/bigskysoftware/htmx) | </> htmx - high power tools for HTML |
| [openpilot](https://github.com/commaai/openpilot) | openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 275+ supported cars. |
| [cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [stripe-ios](https://github.com/stripe/stripe-ios) | Stripe iOS SDK |
| [RIOT](https://github.com/RIOT-OS/RIOT) | RIOT - The friendly OS for IoT |
| [EasyVolcap](https://github.com/zju3dv/EasyVolcap) | [SIGGRAPH Asia 2023 (Technical Communications)] EasyVolcap: Accelerating Neural Volumetric Video Research |
| [TEN-Agent](https://github.com/TEN-framework/TEN-Agent) | TEN Agent is a conversational AI powered by TEN, integrating Gemini 2.0 Multimodal Live API, OpenAI Realtime API, RTC, and more. It offers real-time capabilities to see, hear, and speak, along with advanced tools like weather checks, web search, and RAG. |
| [docling](https://github.com/DS4SD/docling) | Get your documents ready for gen AI |
| [iptv-api](https://github.com/Guovin/iptv-api) | 📺IPTV电视直播源更新工具🚀：✨央视、📡卫视、☘️广东及各省份地方台、🌊港·澳·台、🎬电影、🎥咪咕、🏀体育、🪁动画、🎮游戏、🎵音乐、🏛经典剧场；支持IPv4/IPv6；支持自定义增加频道；支持组播源、酒店源、订阅源、关键字搜索；每天自动更新两次，结果可用于TVBox等播放软件；支持工作流、Docker(amd64/arm64/arm v7)、命令行、GUI运行方式 | IPTV live TV source update tool |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [next-saas-starter](https://github.com/leerob/next-saas-starter) | Get started quickly with Next.js, Postgres, Stripe, and shadcn/ui. |
| [fish-speech](https://github.com/fishaudio/fish-speech) | SOTA Open Source TTS |
| [graphcast](https://github.com/google-deepmind/graphcast) |  |
| [dioxus](https://github.com/DioxusLabs/dioxus) | Fullstack app framework for web, desktop, mobile, and more. |
| [eliza](https://github.com/ai16z/eliza) | Autonomous agents for everyone |
| [Telegram](https://github.com/DrKLO/Telegram) | Telegram for Android source |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent Framework / shim to use Pydantic with LLMs |
| [uv](https://github.com/astral-sh/uv) | An extremely fast Python package and project manager, written in Rust. |
| [MegaParse](https://github.com/QuivrHQ/MegaParse) | File Parser optimised for LLM Ingestion with no loss 🧠 Parse PDFs, Docx, PPTx in a format that is ideal for LLMs. |
| [llamacoder](https://github.com/Nutlope/llamacoder) | Open source Claude Artifacts – built with Llama 3.1 405B |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [eliza](https://github.com/ai16z/eliza) | Autonomous agents for everyone |
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [freqtrade](https://github.com/freqtrade/freqtrade) | Free, open source crypto trading bot |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [TinyTroupe](https://github.com/microsoft/TinyTroupe) | LLM-powered multiagent persona simulation for imagination enhancement and business insights. |
| [atproto](https://github.com/bluesky-social/atproto) | Social networking technology created by Bluesky |
| [payload](https://github.com/payloadcms/payload) | Payload is the open-source, fullstack Next.js framework, giving you instant backend superpowers. Get a full TypeScript backend and admin panel instantly. Use Payload as a headless CMS or for building powerful applications. |
| [MinerU](https://github.com/opendatalab/MinerU) | A high-quality tool for convert PDF to Markdown and JSON.一站式开源高质量数据提取工具，将PDF转换成Markdown和JSON格式。 |
<!-- END OF MONTHLY_TOP10_REPOS -->
