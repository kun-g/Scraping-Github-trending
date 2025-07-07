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
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [dockur/macos](https://github.com/dockur/macos) | macOS inside a Docker container. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [vosen/ZLUDA](https://github.com/vosen/ZLUDA) | CUDA on non-NVIDIA GPUs |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | Comfortably monitor your Internet traffic 🕵️‍♂️ |
| [Alex313031/thorium](https://github.com/Alex313031/thorium) | Chromium fork named after radioactive element No. 90. Windows and MacOS/Raspi/Android/Special builds are in different repositories, links are towards the top of the README.md. |
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [iib0011/omni-tools](https://github.com/iib0011/omni-tools) | Self-hosted collection of powerful web-based tools for everyday tasks. No ads, no tracking, just fast, accessible utilities right from your browser! |
| [home-assistant/home-assistant.io](https://github.com/home-assistant/home-assistant.io) | 📘 Home Assistant User documentation |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) | An open source graphics editor for 2025: comprehensive 2D content creation tool suite for graphic design, digital art, and interactive real-time motion graphics — featuring node-based procedural editing |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 21 Lessons, Get Started Building with Generative AI 🔗https://microsoft.github.io/generative-ai-for-beginners/ |
| [zaidmukaddam/scira](https://github.com/zaidmukaddam/scira) | Scira (Formerly MiniPerplx) is a minimalistic AI-powered search engine that helps you find information on the internet and cites it too. Powered by Vercel AI SDK! Search with models like xAI's Grok 3. |
| [stanford-oval/storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |
| [midday-ai/midday](https://github.com/midday-ai/midday) | Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant made for Freelancers |
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
| [aldinokemal/go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice) | GOWA - WhatsApp REST API with support for UI, Webhooks, and MCP. Built in Golang for efficient memory use. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) | 📚 从零开始的大语言模型原理与实践教程 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
| [menloresearch/jan](https://github.com/menloresearch/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | TensorZero is an open-source stack for industrial-grade LLM applications. It unifies an LLM gateway, observability, optimization, evaluation, and experimentation. |
| [anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
<!-- END OF MONTHLY_TOP10_REPOS -->
