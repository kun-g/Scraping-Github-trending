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
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | PowerShell for every system! |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus Agent Tools, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [SoftFever/OrcaSlicer](https://github.com/SoftFever/OrcaSlicer) | G-code generator for 3D printers (Bambu, Prusa, Voron, VzBot, RatRig, Creality, etc.) |
| [simdjson/simdjson](https://github.com/simdjson/simdjson) | Parsing gigabytes of JSON per second : used by Facebook/Meta Velox, the Node.js runtime, ClickHouse, WatermelonDB, Apache Doris, Milvus, StarRocks |
| [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | Perplexica is an AI-powered search engine. It is an Open source alternative to Perplexity AI |
| [sst/opencode](https://github.com/sst/opencode) | AI coding agent, built for the terminal. |
| [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | all of the workflows of n8n i could find (also from the site itself) |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | PowerShell for every system! |
| [vercel/examples](https://github.com/vercel/examples) | Enjoy our curated collection of examples and solutions. Use these patterns to build your own robust and scalable applications. |
| [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | all of the workflows of n8n i could find (also from the site itself) |
| [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 12 Lessons to Get Started Building AI Agents |
| [grpc/grpc-go](https://github.com/grpc/grpc-go) | The Go language implementation of gRPC. HTTP/2 based RPC |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | LLM agents built for control. Designed for real-world use. Deployed in minutes. |
| [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
| [winapps-org/winapps](https://github.com/winapps-org/winapps) | Run Windows apps such as Microsoft Office/Adobe in Linux (Ubuntu/Fedora) and GNOME/KDE as if they were a part of the native OS, including Nautilus integration. Hard fork ofhttps://github.com/Fmstrat/winapps/ |
| [plait-board/drawnix](https://github.com/plait-board/drawnix) | 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等。All in one open-source whiteboard tool with mind, flowchart, freehand and etc. |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Open-source platform to build and deploy AI agent workflows. |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
<!-- END OF MONTHLY_TOP10_REPOS -->
