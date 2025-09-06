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
| [bytebot-ai/bytebot](https://github.com/bytebot-ai/bytebot) | Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment. |
| [microsoft/BitNet](https://github.com/microsoft/BitNet) | Official inference framework for 1-bit LLMs |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | Find, verify, and analyze leaked credentials |
| [mack-a/v2ray-agent](https://github.com/mack-a/v2ray-agent) | Xray、Tuic、hysteria2、sing-box 八合一一键脚本 |
| [nukeop/nuclear](https://github.com/nukeop/nuclear) | Streaming music player that finds free music for you |
| [EvolutionAPI/evolution-api](https://github.com/EvolutionAPI/evolution-api) | Evolution API is an open-source WhatsApp integration API |
| [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | Awesome MCP Servers - A curated list of Model Context Protocol servers |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | LLM agents built for control. Designed for real-world use. Deployed in minutes. |
| [coleam00/ottomator-agents](https://github.com/coleam00/ottomator-agents) | All the open source AI Agents hosted on the oTTomator Live Agent Studio platform! |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) | Real-time & local speech-to-text, translation, and speaker diarization. With server & web UI. |
| [bytebot-ai/bytebot](https://github.com/bytebot-ai/bytebot) | Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment. |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | HumanLayer enables AI agents to communicate with humans in tool-based and async workflows. Guarantee human oversight of high-stakes function calls with approval workflows across slack, email and more. Bring your LLM and Framework of choice and start giving your AI agents safe access to the world. Agentic Workflows, human in the loop, tool calling |
| [laramies/theHarvester](https://github.com/laramies/theHarvester) | E-mails, subdomains and names Harvester - OSINT |
| [pedroslopez/whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) | A WhatsApp client library for NodeJS that connects through the WhatsApp Web browser app |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
| [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-V 4.5: A GPT-4o Level MLLM for Single Image, Multi Image and High-FPS Video Understanding on Your Phone |
| [JetBrains/koog](https://github.com/JetBrains/koog) | Koog is the official Kotlin framework for building and running robust, scalable and production-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems |
| [gristlabs/grist-core](https://github.com/gristlabs/grist-core) | Grist is the evolution of spreadsheets. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | An Open-Source Asynchronous Coding Agent |
| [winapps-org/winapps](https://github.com/winapps-org/winapps) | Run Windows apps such as Microsoft Office/Adobe in Linux (Ubuntu/Fedora) and GNOME/KDE as if they were a part of the native OS, including Nautilus integration. Hard fork ofhttps://github.com/Fmstrat/winapps/ |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Open-source platform to build and deploy AI agent workflows. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [basecamp/omarchy](https://github.com/basecamp/omarchy) | Opinionated Arch/Hyprland Setup |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [dtyq/magic](https://github.com/dtyq/magic) | Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system) |
<!-- END OF MONTHLY_TOP10_REPOS -->
