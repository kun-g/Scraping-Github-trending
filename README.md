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
| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | Biomni: a general-purpose biomedical AI agent |
| [open-telemetry/opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go) | OpenTelemetry Go API and SDK |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf) | Protocol Buffers - Google's data interchange format |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Build Real-Time Knowledge Graphs for AI Agents |
| [pybind/pybind11](https://github.com/pybind/pybind11) | Seamless operability between C++11 and Python |
| [WordPress/wordpress-develop](https://github.com/WordPress/wordpress-develop) | WordPress Develop, Git-ified. Synced from git://develop.git.wordpress.org/, including branches and tags! This repository is just a mirror of the WordPress subversion repository. Please include a link to a pre-existing ticket onhttps://core.trac.wordpress.org/with every pull request. |
| [gorhill/uBlock](https://github.com/gorhill/uBlock) | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. |
| [landing-ai/agentic-doc](https://github.com/landing-ai/agentic-doc) | Python library for Agentic Document Extraction from LandingAI |
| [zijie0/HumanSystemOptimization](https://github.com/zijie0/HumanSystemOptimization) | 健康学习到150岁 - 人体系统调优不完全指南 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀 High-performance distributed object storage for MinIO alternative. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | Comfortably monitor your Internet traffic 🕵️‍♂️ |
| [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) | Open Source realtime backend in 1 file |
| [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) | 📚 从零开始的大语言模型原理与实践教程 |
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
| [langchain-ai/agents-from-scratch](https://github.com/langchain-ai/agents-from-scratch) | Build an email assistant with human-in-the-loop and memory |
| [aldinokemal/go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice) | GOWA - WhatsApp REST API with support for UI, Webhooks, and MCP. Built with Golang for efficient memory use. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) | An open source graphics editor for 2025: comprehensive 2D content creation tool suite for graphic design, digital art, and interactive real-time motion graphics — featuring node-based procedural editing |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [menloresearch/jan](https://github.com/menloresearch/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | MCP Toolbox for Databases is an open source MCP server for databases. |
| [embabel/embabel-agent](https://github.com/embabel/embabel-agent) | Agent framework for the JVM. Pronounced Em-BAY-bel /ɛmˈbeɪbəl/ |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | Telegram for Android source |
<!-- END OF MONTHLY_TOP10_REPOS -->
