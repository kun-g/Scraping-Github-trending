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
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder | v0 / lovable / Bolt alternative | 🌟 Star if you like it! |
| [pointfreeco/swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) | A library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. |
| [MotiaDev/motia](https://github.com/MotiaDev/motia) | Unified Backend Framework for APIs, Events, and AI Agents |
| [OpenBAS-Platform/openbas](https://github.com/OpenBAS-Platform/openbas) | Open Adversary Exposure Validation Platform |
| [tonsky/FiraCode](https://github.com/tonsky/FiraCode) | Free monospaced font with programming ligatures |
| [kubesphere/kubesphere](https://github.com/kubesphere/kubesphere) | The container platform tailored for Kubernetes multi-cloud, datacenter, and edge management ⎈ 🖥 ☁️ |
| [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings |
| [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | Master the command line, in one page |
| [lydiahallie/javascript-questions](https://github.com/lydiahallie/javascript-questions) | A long list of (advanced) JavaScript questions, and their explanations ✨ |
| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [cloudwego/eino](https://github.com/cloudwego/eino) | The ultimate LLM/AI application development framework in Golang. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud. |
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 一款提示词优化器，助力于编写高质量的提示词 |
| [outline/outline](https://github.com/outline/outline) | The fastest knowledge base for growing teams. Beautiful, realtime collaborative, feature packed, and markdown compatible. |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
| [pointfreeco/swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) | A library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. |
| [daveebbelaar/ai-cookbook](https://github.com/daveebbelaar/ai-cookbook) | Examples and tutorials to help developers build AI systems |
| [Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | A generative world for general-purpose robotics & embodied AI learning. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent) | 🌐 WebAgent for Information Seeking built by Tongyi Lab: WebWalker & WebDancer & WebSailor & WebShaperhttps://arxiv.org/abs/2507.15061https://arxiv.org/pdf/2507.02592 |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀 High-performance distributed object storage for MinIO alternative. |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | A curated list of awesome commands, files, and workflows for Claude Code |
<!-- END OF MONTHLY_TOP10_REPOS -->
