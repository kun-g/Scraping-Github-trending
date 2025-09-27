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
| [ZuodaoTech/everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | 人人都能用英语 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | "RAG-Anything: All-in-One RAG Framework" |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI to solve hard problems in complex codebases. |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
| [basecamp/omarchy](https://github.com/basecamp/omarchy) | Opinionated Arch/Hyprland Setup |
| [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | Open Source AI Platform - AI Chat with advanced features that works with every LLM |
| [ericciarla/trendFinder](https://github.com/ericciarla/trendFinder) | Stay on top of trending topics on social media and the web with AI |
| [netdata/netdata](https://github.com/netdata/netdata) | The fastest path to AI-powered full stack observability, even for lean teams. |
| [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | The Free Software Media System - Server Backend & API |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | The official repo for “Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting”, ACL, 2025. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [get-convex/chef](https://github.com/get-convex/chef) | The only AI app builder that knows backend |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | The official repo for “Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting”, ACL, 2025. |
| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | Free and Open Source, Distributed, RESTful Search Engine |
| [LazyVim/LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | A modern formatting library |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | very good whiteboard SDK / infinite canvas SDK |
| [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) | WebGoat is a deliberately insecure application |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) | Real-time & local speech-to-text, translation, and speaker diarization. With server & web UI. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [dataease/SQLBot](https://github.com/dataease/SQLBot) | 🔥 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG. |
| [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) | Clone a voice in 5 seconds to generate arbitrary speech in real-time |
| [uutils/coreutils](https://github.com/uutils/coreutils) | Cross-platform Rust rewrite of the GNU coreutils |
<!-- END OF MONTHLY_TOP10_REPOS -->
