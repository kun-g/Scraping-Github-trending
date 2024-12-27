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
| [shortest](https://github.com/anti-work/shortest) | QA via natural language AI tests |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Qwen / DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS/Plugins/Artifacts). One-click FREE deployment of your private ChatGPT/ Claude application. |
| [cobalt](https://github.com/imputnet/cobalt) | best way to save what you love |
| [openai-openapi](https://github.com/openai/openai-openapi) | OpenAPI specification for the OpenAI API |
| [echarts](https://github.com/apache/echarts) | Apache ECharts is a powerful, interactive charting and data visualization library for browser |
| [postiz-app](https://github.com/gitroomhq/postiz-app) | 📨 The ultimate social media scheduling tool, with a bunch of AI 🤖 |
| [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. |
| [zig](https://github.com/ziglang/zig) | General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [limbo](https://github.com/tursodatabase/limbo) | Limbo is a work-in-progress, in-process OLTP database management system, compatible with SQLite. |
| [waveterm](https://github.com/wavetermdev/waveterm) | An open-source, cross-platform terminal for seamless workflows |
| [PowerToys](https://github.com/microsoft/PowerToys) | Windows system utilities to maximize productivity |
| [blink.cmp](https://github.com/Saghen/blink.cmp) | Performant, batteries-included completion plugin for Neovim |
| [htmx](https://github.com/bigskysoftware/htmx) | </> htmx - high power tools for HTML |
| [TEN-Agent](https://github.com/TEN-framework/TEN-Agent) | TEN Agent is a conversational AI powered by the TEN, integrating Gemini 2.0 Live, OpenAI Realtime, RTC, and more. It delivers real-time capabilities to see, hear, and speak, while being fully compatible with popular workflow platforms like Dify and Coze. |
| [openpilot](https://github.com/commaai/openpilot) | openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 275+ supported cars. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [eliza](https://github.com/ai16z/eliza) | Autonomous agents for everyone |
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [fish-speech](https://github.com/fishaudio/fish-speech) | SOTA Open Source TTS |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [TEN-Agent](https://github.com/TEN-framework/TEN-Agent) | TEN Agent is a conversational AI powered by the TEN, integrating Gemini 2.0 Live, OpenAI Realtime, RTC, and more. It delivers real-time capabilities to see, hear, and speak, while being fully compatible with popular workflow platforms like Dify and Coze. |
| [multi-agent-orchestrator](https://github.com/awslabs/multi-agent-orchestrator) | Flexible and powerful framework for managing multiple AI agents and handling complex conversations |
| [langflow](https://github.com/langflow-ai/langflow) | Langflow is a low-code app builder for RAG and multi-agent AI applications. It’s Python-based and agnostic to any model, API, or database. |
<!-- END OF MONTHLY_TOP10_REPOS -->
