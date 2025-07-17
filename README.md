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
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [PromtEngineer/localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [maotoumao/MusicFree](https://github.com/maotoumao/MusicFree) | 插件化、定制化、无广告的免费音乐播放器 |
| [frappe/erpnext](https://github.com/frappe/erpnext) | Free and Open Source Enterprise Resource Planning (ERP) |
| [arc53/DocsGPT](https://github.com/arc53/DocsGPT) | DocsGPT is an open-source genAI tool that helps users get reliable answers from knowledge source, while avoiding hallucinations. It enables private and reliable information retrieval, with tooling and agentic system capability built in. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |
| [aws/amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli) | ✨ Agentic chat experience in your terminal. Build applications using natural language. |
| [vpnhood/VpnHood](https://github.com/vpnhood/VpnHood) | Undetectable Fast Portable VPN |
| [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | Build effective agents using Model Context Protocol and simple workflow patterns |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent) | 🌐 WebAgent for Information Seeking built by Tongyi Lab: WebWalker & WebDancer & WebSailorhttps://arxiv.org/pdf/2507.02592 |
| [gorhill/uBlock](https://github.com/gorhill/uBlock) | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Build Real-Time Knowledge Graphs for AI Agents |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀 High-performance distributed object storage for MinIO alternative. |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) | An open source graphics editor for 2025: comprehensive 2D content creation tool suite for graphic design, digital art, and interactive real-time motion graphics — featuring node-based procedural editing |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [embabel/embabel-agent](https://github.com/embabel/embabel-agent) | Agent framework for the JVM. Pronounced Em-BAY-bel /ɛmˈbeɪbəl/ |
| [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) | 📚 从零开始的大语言模型原理与实践教程 |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | Comfortably monitor your Internet traffic 🕵️‍♂️ |
<!-- END OF MONTHLY_TOP10_REPOS -->
