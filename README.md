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
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database diagram editor and SQL generator. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [apihub](https://github.com/hiteshchoudhary/apihub) | Your own API Hub to learn and master API interaction. Ideal for frontend, mobile dev and backend developers. |
| [TV](https://github.com/Guovin/TV) | 📺IPTV电视直播源更新工具🚀：包含💰央视(付费)、📡卫视、🏠广东、🌊港·澳·台、🎬电影、🎥咪咕、🏀体育、🪁动画、🎮游戏、🎵音乐、🏛经典剧场；支持自定义增加频道（含图标）；支持组播源、酒店源、订阅源、线上检索；每天自动更新两次，结果可用于TVBox等播放软件；支持工作流、Docker(amd64/arm64)、命令行、软件界面多种部署/运行方式 | IPTV live TV source update tool |
| [PlayIntegrityFix](https://github.com/chiteroman/PlayIntegrityFix) | Fix Play Integrity (and SafetyNet) verdicts. |
| [PowerShell](https://github.com/PowerShell/PowerShell) | PowerShell for every system! |
| [svelte](https://github.com/sveltejs/svelte) | web development for the rest of us |
| [swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) | A library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. |
| [yfinance](https://github.com/ranaroussi/yfinance) | Download market data from Yahoo! Finance's API |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
| [surya](https://github.com/VikParuchuri/surya) | OCR, layout analysis, reading order, table recognition in 90+ languages |
| [platform](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) |
| [papermark](https://github.com/mfts/papermark) | Papermark is the open-source DocSend alternative with built-in analytics and custom domains. |
| [twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [hanko](https://github.com/teamhanko/hanko) | Authentication and User Management solution for developers. Open source alternative to Clerk & Auth0. |
| [siyuan](https://github.com/siyuan-note/siyuan) | A privacy-first, self-hosted, fully open source personal knowledge management software, written in typescript and golang. |
| [CS-Notes](https://github.com/CyC2018/CS-Notes) | 📚 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| [formbricks](https://github.com/formbricks/formbricks) | Open Source Survey Platform |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [llama-stack](https://github.com/meta-llama/llama-stack) | Model components of the Llama Stack APIs |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🔥🕷️ Crawl4AI: Open-source LLM Friendly Web Crawler & Scrapper |
| [platform](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) |
| [screenpipe](https://github.com/mediar-ai/screenpipe) | 24/7 local AI screen & mic recording. Works with Ollama. Llama3.2 control your computer. Alternative to Rewind.ai & Zapier. Open. Secure. You own your data. Rust. |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [kestra](https://github.com/kestra-io/kestra) | ⚡ Workflow Automation Platform. Orchestrate & Schedule code in any language, run anywhere, 500+ plugins. Alternative to Zapier, Rundeck, Camunda, Airflow... |
| [Pake](https://github.com/tw93/Pake) | 🤱🏻 Turn any webpage into a desktop app with Rust. 🤱🏻 利用 Rust 轻松构建轻量级多端桌面应用 |
| [formbricks](https://github.com/formbricks/formbricks) | Open Source Survey Platform |
| [manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
<!-- END OF MONTHLY_TOP10_REPOS -->
