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
| [dioxus](https://github.com/DioxusLabs/dioxus) | Fullstack app framework for web, desktop, mobile, and more. |
| [helium](https://github.com/mherrmann/helium) | Lighter web automation with Python |
| [docling](https://github.com/DS4SD/docling) | Get your documents ready for gen AI |
| [esp32-weather-epd](https://github.com/lmarzen/esp32-weather-epd) | A low-power E-Paper weather display powered by an ESP32 microcontroller. Utilizes the OpenWeatherMap API. |
| [cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [checkmate](https://github.com/bluewave-labs/checkmate) | Checkmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents in real-time with beautiful visualizations. |
| [limbo](https://github.com/tursodatabase/limbo) | Limbo is a work-in-progress, in-process OLTP database management system, compatible with SQLite. |
| [typeorm](https://github.com/typeorm/typeorm) | ORM for TypeScript and JavaScript. Supports MySQL, PostgreSQL, MariaDB, SQLite, MS SQL Server, Oracle, SAP Hana, WebSQL databases. Works in NodeJS, Browser, Ionic, Cordova and Electron platforms. |
| [terragrunt](https://github.com/gruntwork-io/terragrunt) | Terragrunt is a flexible orchestration tool that allows Infrastructure as Code written in OpenTofu/Terraform to scale. |
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
| [windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [eliza](https://github.com/ai16z/eliza) | Autonomous agents for everyone |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [MinerU](https://github.com/opendatalab/MinerU) | A high-quality tool for convert PDF to Markdown and JSON.一站式开源高质量数据提取工具，将PDF转换成Markdown和JSON格式。 |
| [freqtrade](https://github.com/freqtrade/freqtrade) | Free, open source crypto trading bot |
| [ai-chatbot](https://github.com/vercel/ai-chatbot) | A full-featured, hackable Next.js AI chatbot built by Vercel |
| [next-forge](https://github.com/haydenbleasel/next-forge) | Production-grade Turborepo template for Next.js apps. |
| [khoj](https://github.com/khoj-ai/khoj) | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (e.g gpt, claude, gemini, llama, qwen, mistral). |
| [exo](https://github.com/exo-explore/exo) | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |
| [autogen](https://github.com/microsoft/autogen) | A programming framework for agentic AI 🤖 (PyPi: autogen-agentchat) |
<!-- END OF MONTHLY_TOP10_REPOS -->
