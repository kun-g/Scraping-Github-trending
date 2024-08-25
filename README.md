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
| [zed](https://github.com/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. |
| [quivr](https://github.com/QuivrHQ/quivr) | Open-source RAG Framework for building GenAI Second Brains 🧠 Build productivity assistant (RAG) ⚡️🤖 Chat with your docs (PDF, CSV, ...) & apps using Langchain, GPT 3.5 / 4 turbo, Private, Anthropic, VertexAI, Ollama, LLMs, Groq that you can share with users ! Efficient retrieval augmented generation framework |
| [es-toolkit](https://github.com/toss/es-toolkit) | A modern JavaScript utility library that's 2-3 times faster and up to 97% smaller—a major upgrade to lodash. |
| [mimalloc](https://github.com/microsoft/mimalloc) | mimalloc is a compact general purpose allocator with excellent performance. |
| [opencti](https://github.com/OpenCTI-Platform/opencti) | Open Cyber Threat Intelligence Platform |
| [uv](https://github.com/astral-sh/uv) | An extremely fast Python package and project manager, written in Rust. |
| [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook) | This is a Phi-3 book for getting started with Phi-3. Phi-3, a family of open AI models developed by Microsoft. Phi-3 models are the most capable and cost-effective small language models (SLMs) available, outperforming models of the same size and next size up across a variety of language, reasoning, coding, and math benchmarks. |
| [roop](https://github.com/s0md3v/roop) | one-click face swap |
| [aws-cli](https://github.com/aws/aws-cli) | Universal Command Line Interface for Amazon Web Services |
| [fmt](https://github.com/fmtlib/fmt) | A modern formatting library |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [authentik](https://github.com/goauthentik/authentik) | The authentication glue you need. |
| [es-toolkit](https://github.com/toss/es-toolkit) | A modern JavaScript utility library that's 2-3 times faster and up to 97% smaller—a major upgrade to lodash. |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
| [ai-toolkit](https://github.com/ostris/ai-toolkit) | Various AI scripts. Mostly Stable Diffusion stuff. |
| [aria2](https://github.com/aria2/aria2) | aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. It supports HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink. |
| [uv](https://github.com/astral-sh/uv) | An extremely fast Python package and project manager, written in Rust. |
| [parler-tts](https://github.com/huggingface/parler-tts) | Inference and training library for high-quality TTS models. |
| [AeroSpace](https://github.com/nikitabobko/AeroSpace) | AeroSpace is an i3-like tiling window manager for macOS |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mem0](https://github.com/mem0ai/mem0) | The memory layer for Personalized AI |
| [MinerU](https://github.com/opendatalab/MinerU) | A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。 |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [FlClash](https://github.com/chen08209/FlClash) | A multi-platform proxy client based on ClashMeta,simple and easy to use, open-source and ad-free. |
| [metahuman-stream](https://github.com/lipku/metahuman-stream) | Real time interactive streaming digital human |
| [teable](https://github.com/teableio/teable) | ✨ The Next Gen Airtable Alternative: No-Code Postgres |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. |
| [composio](https://github.com/ComposioHQ/composio) | Composio equips agents with well-crafted tools empowering them to tackle complex tasks |
<!-- END OF MONTHLY_TOP10_REPOS -->
