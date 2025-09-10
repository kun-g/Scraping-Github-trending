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
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | LLM agents built for control. Designed for real-world use. Deployed in minutes. |
| [Vector-Wangel/XLeRobot](https://github.com/Vector-Wangel/XLeRobot) | XLeRobot: Practical Dual-Arm Mobile Home Robot for $660 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | FULL v0, Cursor, Manus, Augment Code, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Xcode, Trae AI, Cluely & Orchids.app (And other Open Sourced) System Prompts, Tools & AI Models. |
| [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [vercel/examples](https://github.com/vercel/examples) | Enjoy our curated collection of examples and solutions. Use these patterns to build your own robust and scalable applications. |
| [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
| [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data. 🐳Docker-friendly.⚡Always in sync with Sharepoint, Google Drive, S3, Kafka, PostgreSQL, real-time data APIs, and more. |
| [hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | OCR software, free and offline. 开源、免费的离线OCR软件。支持截屏/批量导入图片，PDF文档识别，排除水印/页眉页脚，扫描/生成二维码。内置多国语言库。 |
| [11cafe/jaaz](https://github.com/11cafe/jaaz) | The world's first open-source multimodal creative assistant This is a substitute for Canva and Manus that prioritizes privacy and is usable locally. |
| [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [bytebot-ai/bytebot](https://github.com/bytebot-ai/bytebot) | Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment. |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [LukeGus/Termix](https://github.com/LukeGus/Termix) | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. |
| [pedroslopez/whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) | A WhatsApp client library for NodeJS that connects through the WhatsApp Web browser app |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | SoTA open-source TTS |
| [Eventual-Inc/Daft](https://github.com/Eventual-Inc/Daft) | Distributed query engine providing simple and reliable data processing for any modality and scale |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more |
| [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | Find, verify, and analyze leaked credentials |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | LLM agents built for control. Designed for real-world use. Deployed in minutes. |
| [google/mangle](https://github.com/google/mangle) |  |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [plait-board/drawnix](https://github.com/plait-board/drawnix) | 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等。All in one open-source whiteboard tool with mind, flowchart, freehand and etc. |
| [winapps-org/winapps](https://github.com/winapps-org/winapps) | Run Windows apps such as Microsoft Office/Adobe in Linux (Ubuntu/Fedora) and GNOME/KDE as if they were a part of the native OS, including Nautilus integration. Hard fork ofhttps://github.com/Fmstrat/winapps/ |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Open-source platform to build and deploy AI agent workflows. |
| [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud) | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, K8s, AI inference, and IAM services. |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [dtyq/magic](https://github.com/dtyq/magic) | Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system) |
<!-- END OF MONTHLY_TOP10_REPOS -->
