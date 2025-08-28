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
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [plait-board/drawnix](https://github.com/plait-board/drawnix) | 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等。All in one open-source whiteboard tool with mind, flowchart, freehand and etc. |
| [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) | Python package for Real-time, Local Speech-to-Text and Speaker Diarization. FastAPI Server & Web Interface |
| [microsoft/terminal](https://github.com/microsoft/terminal) | The new Windows Terminal and the original Windows console host, all in the same place! |
| [firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker) | Secure and fast microVMs for serverless computing. |
| [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | Neural Networks: Zero to Hero |
| [santinic/audiblez](https://github.com/santinic/audiblez) | Generate audiobooks from e-books |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, and more! |
| [eythaann/Seelen-UI](https://github.com/eythaann/Seelen-UI) | The Fully Customizable Desktop Environment for Windows 10/11. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [plait-board/drawnix](https://github.com/plait-board/drawnix) | 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等。All in one open-source whiteboard tool with mind, flowchart, freehand and etc. |
| [winapps-org/winapps](https://github.com/winapps-org/winapps) | Run Windows apps such as Microsoft Office/Adobe in Linux (Ubuntu/Fedora) and GNOME/KDE as if they were a part of the native OS, including Nautilus integration. Hard fork ofhttps://github.com/Fmstrat/winapps/ |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Sim is an open-source AI agent workflow builder. Sim's interface is a lightweight, intuitive way to rapidly build and deploy LLMs that connect with your favorite tools. |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [google/googletest](https://github.com/google/googletest) | GoogleTest - Google Testing and Mocking Framework |
| [Leantime/leantime](https://github.com/Leantime/leantime) | Leantime is a goals focused project management system for non-project managers. Building with ADHD, Autism, and dyslexia in mind. |
| [Budibase/budibase](https://github.com/Budibase/budibase) | Create business apps and automate workflows in minutes. Supports PostgreSQL, MySQL, MariaDB, MSSQL, MongoDB, Rest API, Docker, K8s, and more 🚀 No code / Low code platform.. |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data 🔥 |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [9001/copyparty](https://github.com/9001/copyparty) | Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps |
| [plait-board/drawnix](https://github.com/plait-board/drawnix) | 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等。All in one open-source whiteboard tool with mind, flowchart, freehand and etc. |
| [winapps-org/winapps](https://github.com/winapps-org/winapps) | Run Windows apps such as Microsoft Office/Adobe in Linux (Ubuntu/Fedora) and GNOME/KDE as if they were a part of the native OS, including Nautilus integration. Hard fork ofhttps://github.com/Fmstrat/winapps/ |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Sim is an open-source AI agent workflow builder. Sim's interface is a lightweight, intuitive way to rapidly build and deploy LLMs that connect with your favorite tools. |
| [dtyq/magic](https://github.com/dtyq/magic) | Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system) |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [oraios/serena](https://github.com/oraios/serena) | A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & Agno integration) |
<!-- END OF MONTHLY_TOP10_REPOS -->
