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
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! |
| [trailofbits/buttercup](https://github.com/trailofbits/buttercup) |  |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [menloresearch/jan](https://github.com/menloresearch/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 21 Lessons, Get Started Building with Generative AI 🔗https://microsoft.github.io/generative-ai-for-beginners/ |
| [midday-ai/midday](https://github.com/midday-ai/midday) | Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant made for Freelancers |
| [xiaoyaocz/dart_simple_live](https://github.com/xiaoyaocz/dart_simple_live) | 简简单单的看直播 |
| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration. |
| [ollama/ollama](https://github.com/ollama/ollama) | Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Examples and guides for using the OpenAI API |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | LLM inference in C/C++ |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | The AI Browser Automation Framework |
| [actualbudget/actual](https://github.com/actualbudget/actual) | A local-first personal finance app |
| [lvgl/lvgl](https://github.com/lvgl/lvgl) | Embedded graphics library to create beautiful UIs for any MCU, MPU and display type. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Financial data aggregator for humans and AI agents. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |  |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | A curated list of awesome commands, files, and workflows for Claude Code |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
| [sst/opencode](https://github.com/sst/opencode) | AI coding agent, built for the terminal. |
<!-- END OF MONTHLY_TOP10_REPOS -->
