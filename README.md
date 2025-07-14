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
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [vercel/commerce](https://github.com/vercel/commerce) | Next.js Commerce |
| [block/goose](https://github.com/block/goose) | an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM |
| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more. |
| [NVIDIA/cutlass](https://github.com/NVIDIA/cutlass) | CUDA Templates for Linear Algebra Subroutines |
| [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| [gorhill/uBlock](https://github.com/gorhill/uBlock) | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. |
| [farhanashrafdev/90DaysOfCyberSecurity](https://github.com/farhanashrafdev/90DaysOfCyberSecurity) | This repository contains a 90-day cybersecurity study plan, along with resources and materials for learning various cybersecurity concepts and technologies. The plan is organized into daily tasks, covering topics such as Network+, Security+, Linux, Python, Traffic Analysis, Git, ELK, AWS, Azure, and Hacking. The repository also includes a `LEARN.md |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped withhttps://github.com/microsoft/RD-Agentto automate R&D process. |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | The AI Browser Automation Framework |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀 High-performance distributed object storage for MinIO alternative. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [snailyp/gemini-balance](https://github.com/snailyp/gemini-balance) | Gemini polling proxy service （gemini轮询代理服务） |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | Comfortably monitor your Internet traffic 🕵️‍♂️ |
| [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) | 📚 从零开始的大语言模型原理与实践教程 |
| [smallcloudai/refact](https://github.com/smallcloudai/refact) | AI Agent that handles engineering tasks end-to-end: integrates with developers’ tools, plans, executes, and iterates until it achieves a successful result. |
| [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) | Open Source realtime backend in 1 file |
| [gorhill/uBlock](https://github.com/gorhill/uBlock) | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) | An open source graphics editor for 2025: comprehensive 2D content creation tool suite for graphic design, digital art, and interactive real-time motion graphics — featuring node-based procedural editing |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [menloresearch/jan](https://github.com/menloresearch/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [embabel/embabel-agent](https://github.com/embabel/embabel-agent) | Agent framework for the JVM. Pronounced Em-BAY-bel /ɛmˈbeɪbəl/ |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) | 📚 从零开始的大语言模型原理与实践教程 |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
<!-- END OF MONTHLY_TOP10_REPOS -->
