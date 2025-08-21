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
| [simstudioai/sim](https://github.com/simstudioai/sim) | Sim is an open-source AI agent workflow builder. Sim Studio's interface is a lightweight, intuitive way to quickly build and deploy LLMs that connect with your favorite tools. |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | JavaScript API for Chrome and Firefox |
| [bitwarden/clients](https://github.com/bitwarden/clients) | Bitwarden client apps (web, browser extension, desktop, and cli). |
| [Leantime/leantime](https://github.com/Leantime/leantime) | Leantime is a goals focused project management system for non-project managers. Building with ADHD, Autism, and dyslexia in mind. |
| [n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) | The Self-hosted AI Starter Kit is an open-source template that quickly sets up a local AI environment. Curated by n8n, it provides essential tools for creating secure, self-hosted AI workflows. |
| [MotiaDev/motia](https://github.com/MotiaDev/motia) | Modern Backend Framework that unifies APIs, background jobs, workflows, and AI Agents into a single core primitive with built-in observability and state management. |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |
| [laude-institute/terminal-bench](https://github.com/laude-institute/terminal-bench) | A benchmark for LLMs on complicated tasks in the terminal |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud) | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, K8s, AI inference, and IAM services. |
| [microsoft/poml](https://github.com/microsoft/poml) | Prompt Orchestration Markup Language |
| [dtyq/magic](https://github.com/dtyq/magic) | Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system) |
| [external-secrets/external-secrets](https://github.com/external-secrets/external-secrets) | External Secrets Operator reads information from a third-party service like AWS Secrets Manager and automatically injects the values as Kubernetes Secrets. |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-sourced Multimodal AI Agent Stack connecting Cutting-edge AI Models and Agent Infra. |
| [PixiEditor/PixiEditor](https://github.com/PixiEditor/PixiEditor) | PixiEditor is a Universal Editor for all your 2D needs |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [syncthing/syncthing](https://github.com/syncthing/syncthing) | Open Source Continuous File Synchronization |
| [apple/embedding-atlas](https://github.com/apple/embedding-atlas) | Embedding Atlas is a tool that provides interactive visualizations for large embeddings. It allows you to visualize, cross-filter, and search embeddings and metadata. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Financial data platform for analysts, quants and AI agents. |
| [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | Improve your resumes with Resume Matcher. Get insights, keyword suggestions and tune your resumes to job descriptions. |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [dtyq/magic](https://github.com/dtyq/magic) | Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system) |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [roboflow/supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
<!-- END OF MONTHLY_TOP10_REPOS -->
