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
| [GoodbyeDPI](https://github.com/ValdikSS/GoodbyeDPI) | GoodbyeDPI — Deep Packet Inspection circumvention utility (for Windows) |
| [zapret](https://github.com/bol-van/zapret) | DPI bypass multi platform |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. |
| [byedpi](https://github.com/hufrea/byedpi) | Bypass DPI |
| [Magisk](https://github.com/topjohnwu/Magisk) | The Magic Mask for Android |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader |
| [LibreChat](https://github.com/danny-avila/LibreChat) | Enhanced ChatGPT Clone: Features OpenAI, Assistants API, Azure, Groq, GPT-4 Vision, Mistral, Bing, Anthropic, OpenRouter, Vertex AI, Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development |
| [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [Sunshine](https://github.com/LizardByte/Sunshine) | Self-hosted game stream host for Moonlight. |
| [sqlite-vec](https://github.com/asg017/sqlite-vec) | A vector search SQLite extension that runs anywhere! |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [MinerU](https://github.com/opendatalab/MinerU) | A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。 |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [dice](https://github.com/DiceDB/dice) | A drop-in replacement of Redis with SQL-based realtime reactivity. |
| [metahuman-stream](https://github.com/lipku/metahuman-stream) | Real time interactive streaming digital human |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [googletest](https://github.com/google/googletest) | GoogleTest - Google Testing and Mocking Framework |
| [java-design-patterns](https://github.com/iluwatar/java-design-patterns) | Design patterns implemented in Java |
| [trufflehog](https://github.com/trufflesecurity/trufflehog) | Find and verify secrets |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [graphrag](https://github.com/microsoft/graphrag) | A modular graph-based Retrieval-Augmented Generation (RAG) system |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [books](https://github.com/free-educa/books) | o armazém de livros |
| [tiptap](https://github.com/ueberdosis/tiptap) | The headless rich text editor framework for web artisans. |
| [graphrag-accelerator](https://github.com/Azure-Samples/graphrag-accelerator) | One-click deploy of a Knowledge Graph powered RAG (GraphRAG) in Azure |
| [everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | 人人都能用英语 |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
<!-- END OF MONTHLY_TOP10_REPOS -->
