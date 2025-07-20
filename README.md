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
| [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | Hyprland is an independent, highly customizable, dynamic tiling Wayland compositor that doesn't sacrifice on its looks. |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |  |
| [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | Ready-to-use SRT / WebRTC / RTSP / RTMP / LL-HLS media server and media proxy that allows to read, publish, proxy, record and playback video and audio streams. |
| [shadps4-emu/shadPS4](https://github.com/shadps4-emu/shadPS4) | PlayStation 4 emulator for Windows, Linux and macOS written in C++ |
| [soxoj/maigret](https://github.com/soxoj/maigret) | 🕵️‍♂️ Collect a dossier on a person by username from thousands of sites |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | GitHub's official MCP Server |
| [remoteintech/remote-jobs](https://github.com/remoteintech/remote-jobs) | A list of semi to fully remote-friendly companies (jobs) in tech. |
| [bknd-io/bknd](https://github.com/bknd-io/bknd) | Lightweight Firebase/Supabase alternative built to run anywhere — incl. Next.js, Remix, Astro, Cloudflare, Bun, Node, AWS Lambda & more. |
| [mrdbourke/pytorch-deep-learning](https://github.com/mrdbourke/pytorch-deep-learning) | Materials for the Learn PyTorch for Deep Learning: Zero to Mastery course. |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [gorhill/uBlock](https://github.com/gorhill/uBlock) | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Build Real-Time Knowledge Graphs for AI Agents |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |  |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | Find secrets with Gitleaks 🔑 |
| [strapi/strapi](https://github.com/strapi/strapi) | 🚀 Strapi is the leading open-source headless CMS. It’s 100% JavaScript/TypeScript, fully customizable, and developer-first. |
| [RSSNext/Folo](https://github.com/RSSNext/Folo) | 🧡 Follow everything in one place |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent) | 🌐 WebAgent for Information Seeking built by Tongyi Lab: WebWalker & WebDancer & WebSailor & WebShaperhttps://arxiv.org/pdf/2507.02592 |
| [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) | An open source graphics editor for 2025: comprehensive 2D content creation tool suite for graphic design, digital art, and interactive real-time motion graphics — featuring node-based procedural editing |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | Comfortably monitor your Internet traffic 🕵️‍♂️ |
| [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) | 📚 从零开始的大语言模型原理与实践教程 |
| [embabel/embabel-agent](https://github.com/embabel/embabel-agent) | Agent framework for the JVM. Pronounced Em-BAY-bel /ɛmˈbeɪbəl/ |
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
<!-- END OF MONTHLY_TOP10_REPOS -->
