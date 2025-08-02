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
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |
| [TandoorRecipes/recipes](https://github.com/TandoorRecipes/recipes) | Application for managing recipes, planning meals, building shopping lists and much much more! |
| [devlikeapro/waha](https://github.com/devlikeapro/waha) | WAHA - WhatsApp HTTP API (REST API) that you can configure in a click! 3 engines: WEBJS (browser based), NOWEB (websocket nodejs), GOWS (websocket go) |
| [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | JavaScript API for Chrome and Firefox |
| [kubesphere/kubesphere](https://github.com/kubesphere/kubesphere) | The container platform tailored for Kubernetes multi-cloud, datacenter, and edge management ⎈ 🖥 ☁️ |
| [eclipse-sumo/sumo](https://github.com/eclipse-sumo/sumo) | Eclipse SUMO is an open source, highly portable, microscopic and continuous traffic simulation package designed to handle large networks. It allows for intermodal simulation including pedestrians and comes with a large set of tools for scenario creation. |
| [9001/copyparty](https://github.com/9001/copyparty) | Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder | v0 / lovable / Bolt alternative | 🌟 Star if you like it! |
| [stenzek/duckstation](https://github.com/stenzek/duckstation) | Fast PlayStation 1 emulator for x86-64/AArch32/AArch64/RV64 |
| [playcanvas/editor](https://github.com/playcanvas/editor) | Powerful visual editor environment for building WebGL, WebGPU, WebXR apps |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud. |
| [cloudwego/eino](https://github.com/cloudwego/eino) | The ultimate LLM/AI application development framework in Golang. |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [outline/outline](https://github.com/outline/outline) | The fastest knowledge base for growing teams. Beautiful, realtime collaborative, feature packed, and markdown compatible. |
| [tldr-pages/tldr](https://github.com/tldr-pages/tldr) | 📚 Collaborative cheatsheets for console commands |
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 一款提示词优化器，助力于编写高质量的提示词 |
| [Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | A generative world for general-purpose robotics & embodied AI learning. |
| [mattermost-community/focalboard](https://github.com/mattermost-community/focalboard) | Focalboard is an open source, self-hosted alternative to Trello, Notion, and Asana. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent) | 🌐 WebAgent for Information Seeking built by Tongyi Lab: WebWalker & WebDancer & WebSailor & WebShaperhttps://arxiv.org/abs/2507.15061https://arxiv.org/pdf/2507.02592 |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | A curated list of awesome commands, files, and workflows for Claude Code |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [sst/opencode](https://github.com/sst/opencode) | AI coding agent, built for the terminal. |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |  |
<!-- END OF MONTHLY_TOP10_REPOS -->
