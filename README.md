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
| [skyvern](https://github.com/Skyvern-AI/skyvern) | Automate browser-based workflows with LLMs and Computer Vision |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [Follow](https://github.com/RSSNext/Follow) | 🧡 Next generation information browser. |
| [courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [EasySpider](https://github.com/NaiboWang/EasySpider) | A visual no-code/code-free web crawler/spider易采集：一个可视化浏览器自动化测试/数据采集/爬虫软件，可以无代码图形化的设计和执行爬虫任务。别名：ServiceWrapper面向Web应用的智能化服务封装系统。 |
| [dittofeed](https://github.com/dittofeed/dittofeed) | Open-source customer engagement. Automate transactional and marketing messages across email, SMS, mobile push, WhatsApp, Slack, and more 📨 |
| [TV](https://github.com/Guovin/TV) | 📺IPTV电视直播源更新工具🚀：包含💰央视(付费)、📡卫视、🏠广东、🌊港·澳·台、🎬电影、🎥咪咕、🏀体育、🪁动画、🎮游戏、🎵音乐、🏛经典剧场；支持自定义增加频道；支持组播源、酒店源、订阅源、关键字搜索；每天自动更新两次，结果可用于TVBox等播放软件；支持工作流、Docker(amd64/arm64)、命令行、GUI运行方式 | IPTV live TV source update tool |
| [ragflow](https://github.com/infiniflow/ragflow) | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. |
| [ViMusic](https://github.com/vfsfitvnm/ViMusic) | An Android application for streaming music from YouTube Music. |
| [cypress](https://github.com/cypress-io/cypress) | Fast, easy and reliable testing for anything that runs in a browser. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Agents with memory, knowledge, tools and reasoning. Chat with them using a beautiful Agent UI. |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database diagram editor and SQL generator. |
| [co-tracker](https://github.com/facebookresearch/co-tracker) | CoTracker is a model for tracking any point (pixel) on a video. |
| [social-app](https://github.com/bluesky-social/social-app) | The Bluesky Social application for Web, iOS, and Android |
| [mindcraft](https://github.com/kolbytn/mindcraft) |  |
| [yfinance](https://github.com/ranaroussi/yfinance) | Download market data from Yahoo! Finance's API |
| [deepface](https://github.com/serengil/deepface) | A Lightweight Face Recognition and Facial Attribute Analysis (Age, Gender, Emotion and Race) Library for Python |
| [cocos-engine](https://github.com/cocos/cocos-engine) | Cocos simplifies game creation and distribution with Cocos Creator, a free, open-source, cross-platform game engine. Empowering millions of developers to create high-performance, engaging 2D/3D games and instant web entertainment. |
| [fingerprintjs](https://github.com/fingerprintjs/fingerprintjs) | The most advanced browser fingerprinting library. |
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
