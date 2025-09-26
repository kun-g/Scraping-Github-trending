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
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI to solve hard problems in complex codebases. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [ZuodaoTech/everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | 人人都能用英语 |
| [Olow304/memvid](https://github.com/Olow304/memvid) | Video-based AI memory library. Store millions of text chunks in MP4 files with lightning-fast semantic search. No database needed. |
| [TanStack/router](https://github.com/TanStack/router) | 🤖 Fully typesafe Router for React (and friends) w/ built-in caching, 1st class search-param APIs, client-side cache integration and isomorphic rendering. |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
| [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 30 days of Python programming challenge is a step-by-step guide to learn the Python programming language in 30 days. This challenge may take more than100 days, follow your own pace. These videos may help too:https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [LazyVim/LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
| [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) | WebGoat is a deliberately insecure application |
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | A modern formatting library |
| [category-labs/monad](https://github.com/category-labs/monad) |  |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | The official repo for “Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting”, ACL, 2025. |
| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | Free and Open Source, Distributed, RESTful Search Engine |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | very good whiteboard SDK / infinite canvas SDK |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
| [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) | Real-time & local speech-to-text, translation, and speaker diarization. With server & web UI. |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [dataease/SQLBot](https://github.com/dataease/SQLBot) | 🔥 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG. |
| [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) | Clone a voice in 5 seconds to generate arbitrary speech in real-time |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
<!-- END OF MONTHLY_TOP10_REPOS -->
