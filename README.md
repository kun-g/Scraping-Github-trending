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
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Sim is an open-source AI agent workflow builder. Sim Studio's interface is a lightweight, intuitive way to quickly build and deploy LLMs that connect with your favorite tools. |
| [google/googletest](https://github.com/google/googletest) | GoogleTest - Google Testing and Mocking Framework |
| [bitwarden/clients](https://github.com/bitwarden/clients) | Bitwarden client apps (web, browser extension, desktop, and cli). |
| [Budibase/budibase](https://github.com/Budibase/budibase) | Create business apps and automate workflows in minutes. Supports PostgreSQL, MySQL, MariaDB, MSSQL, MongoDB, Rest API, Docker, K8s, and more 🚀 No code / Low code platform.. |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data 🔥 |
| [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack) | Useful tool to track location or mobile number |
| [nextjs/saas-starter](https://github.com/nextjs/saas-starter) | Get started quickly with Next.js, Postgres, Stripe, and shadcn/ui. |
| [plait-board/drawnix](https://github.com/plait-board/drawnix) | 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等。All in one open-source whiteboard tool with mind, flowchart, freehand and etc. |
| [HeyPuter/puter](https://github.com/HeyPuter/puter) | 🌐 The Internet OS! Free, Open-Source, and Self-Hostable. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [microsoft/poml](https://github.com/microsoft/poml) | Prompt Orchestration Markup Language |
| [dtyq/magic](https://github.com/dtyq/magic) | Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system) |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [external-secrets/external-secrets](https://github.com/external-secrets/external-secrets) | External Secrets Operator reads information from a third-party service like AWS Secrets Manager and automatically injects the values as Kubernetes Secrets. |
| [PixiEditor/PixiEditor](https://github.com/PixiEditor/PixiEditor) | PixiEditor is a Universal Editor for all your 2D needs |
| [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud) | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, K8s, AI inference, and IAM services. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! |
| [syncthing/syncthing](https://github.com/syncthing/syncthing) | Open Source Continuous File Synchronization |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-sourced Multimodal AI Agent Stack connecting Cutting-edge AI Models and Agent Infra. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud. |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Financial data platform for analysts, quants and AI agents. |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
| [dtyq/magic](https://github.com/dtyq/magic) | Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system) |
| [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | Improve your resumes with Resume Matcher. Get insights, keyword suggestions and tune your resumes to job descriptions. |
<!-- END OF MONTHLY_TOP10_REPOS -->
