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
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [microsoft/poml](https://github.com/microsoft/poml) | Prompt Orchestration Markup Language |
| [LMCache/LMCache](https://github.com/LMCache/LMCache) | Supercharge Your LLM with the Fastest KV Cache Layer |
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [farhanashrafdev/90DaysOfCyberSecurity](https://github.com/farhanashrafdev/90DaysOfCyberSecurity) | This repository contains a 90-day cybersecurity study plan, along with resources and materials for learning various cybersecurity concepts and technologies. The plan is organized into daily tasks, covering topics such as Network+, Security+, Linux, Python, Traffic Analysis, Git, ELK, AWS, Azure, and Hacking. The repository also includes a `LEARN.md |
| [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) |  Now we have become very big, Different from the original idea. Collect premium software in various categories. |
| [tsoding/nob.h](https://github.com/tsoding/nob.h) | Header only library for writing build recipes in C. |
| [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) | A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP). |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | LLM agents built for control. Designed for real-world use. Deployed in minutes. |
| [PixiEditor/PixiEditor](https://github.com/PixiEditor/PixiEditor) | PixiEditor is a Universal Editor for all your 2D needs |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
| [menloresearch/jan](https://github.com/menloresearch/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [xiaoyaocz/dart_simple_live](https://github.com/xiaoyaocz/dart_simple_live) | 简简单单的看直播 |
| [external-secrets/external-secrets](https://github.com/external-secrets/external-secrets) | External Secrets Operator reads information from a third-party service like AWS Secrets Manager and automatically injects the values as Kubernetes Secrets. |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! |
| [umami-software/umami](https://github.com/umami-software/umami) | Umami is a modern, privacy-focused alternative to Google Analytics. |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-sourced Multimodal AI Agent Stack connecting Cutting-edge AI Models and Agent Infra. |
| [idosal/git-mcp](https://github.com/idosal/git-mcp) | Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project |
| [polarsource/polar](https://github.com/polarsource/polar) | An open source engine for your digital products. Sell SaaS and digital products in minutes. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | Improve your resumes with Resume Matcher. Get insights, keyword suggestions and tune your resumes to job descriptions. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Financial data aggregator for humans and AI agents. |
| [roboflow/supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |  |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | A curated list of awesome commands, files, and workflows for Claude Code |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |
<!-- END OF MONTHLY_TOP10_REPOS -->
