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
| [microsoft/edit](https://github.com/microsoft/edit) | We all edit. |
| [mui/base-ui](https://github.com/mui/base-ui) | Unstyled UI components for building accessible web apps and design systems. From the creators of Radix, Floating UI, and Material UI. |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | Find secrets with Gitleaks 🔑 |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | A collection of MCP servers. |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Collection of leaked system prompts |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [nexus-xyz/nexus-cli](https://github.com/nexus-xyz/nexus-cli) | Command line interface for supplying proofs to the Nexus network. |
| [AykutSarac/jsoncrack.com](https://github.com/AykutSarac/jsoncrack.com) | ✨ Innovative and open-source visualization application that transforms various data formats, such as JSON, YAML, XML, CSV and more, into interactive graphs. |
| [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | Fullstack app framework for web, desktop, and mobile. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | Telegram for Android source |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |
| [automatisch/automatisch](https://github.com/automatisch/automatisch) | The open source Zapier alternative. Build workflow automation without spending time and money. |
| [microsoft/edit](https://github.com/microsoft/edit) | We all edit. |
| [Mail-0/Zero](https://github.com/Mail-0/Zero) | Experience email the way you want with Mail0 – the first open source email app that puts your privacy and safety first. Join the discord:https://discord.gg/mail0 |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
| [mui/base-ui](https://github.com/mui/base-ui) | Unstyled UI components for building accessible web apps and design systems. From the creators of Radix, Floating UI, and Material UI. |
| [menloresearch/jan](https://github.com/menloresearch/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | TensorZero is an open-source stack for industrial-grade LLM applications. It unifies an LLM gateway, observability, optimization, evaluation, and experimentation. |
| [menloresearch/jan](https://github.com/menloresearch/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
| [anthropics/courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
<!-- END OF MONTHLY_TOP10_REPOS -->
