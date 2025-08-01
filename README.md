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
| [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) |  |
| [stenzek/duckstation](https://github.com/stenzek/duckstation) | Fast PlayStation 1 emulator for x86-64/AArch32/AArch64/RV64 |
| [SkyworkAI/SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2) | SkyReels-V2: Infinite-length Film Generative model |
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |
| [EmenstaNougat/ESP32-BlueJammer](https://github.com/EmenstaNougat/ESP32-BlueJammer) | The ESP32-BlueJammer (Bluetooth jammer, BLE jammer, WiFi jammer, RC jammer) disrupts 2.4GHz communications. Using an ESP32 and nRF24 modules, it generates noise and unnecessary packets, causing interference between the devices communicating, making them unable to work as intended. Ideal for controlled disruption and security testing. |
| [9001/copyparty](https://github.com/9001/copyparty) | Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps |
| [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | JavaScript API for Chrome and Firefox |
| [Canner/WrenAI](https://github.com/Canner/WrenAI) | ⚡️Wren AI is your GenBI Agent, that you can query any database with natural language, get accurate SQL(Text-to-SQL), charts(Text-to-Charts) & AI-generated insights in seconds. |
| [pointfreeco/swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) | A library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. |
| [fastrepl/hyprnote](https://github.com/fastrepl/hyprnote) | Local-first AI Notepad for Private Meetings |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud. |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
| [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | Improve your resumes with Resume Matcher. Get insights, keyword suggestions and tune your resumes to job descriptions. |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
| [cloudwego/eino](https://github.com/cloudwego/eino) | The ultimate LLM/AI application development framework in Golang. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated) | React Native's Animated library reimplemented |
| [Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | A generative world for general-purpose robotics & embodied AI learning. |
| [roboflow/supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
| [tldr-pages/tldr](https://github.com/tldr-pages/tldr) | 📚 Collaborative cheatsheets for console commands |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent) | 🌐 WebAgent for Information Seeking built by Tongyi Lab: WebWalker & WebDancer & WebSailor & WebShaperhttps://arxiv.org/abs/2507.15061https://arxiv.org/pdf/2507.02592 |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | A curated list of awesome commands, files, and workflows for Claude Code |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [sst/opencode](https://github.com/sst/opencode) | AI coding agent, built for the terminal. |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |  |
<!-- END OF MONTHLY_TOP10_REPOS -->
