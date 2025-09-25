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
| [cloudflare/capnweb](https://github.com/cloudflare/capnweb) | JavaScript/TypeScript-native, low-boilerplate, object-capability RPC system |
| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | Free and Open Source, Distributed, RESTful Search Engine |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | "RAG-Anything: All-in-One RAG Framework" |
| [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | Ultralytics YOLO 🚀 |
| [istio/istio](https://github.com/istio/istio) | Connect, secure, control, and observe services. |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
| [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | Free, open source crypto trading bot |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | The official repo for “Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting”, ACL, 2025. |
| [aliasrobotics/cai](https://github.com/aliasrobotics/cai) | Cybersecurity AI (CAI), the framework for AI Security |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [category-labs/monad](https://github.com/category-labs/monad) |  |
| [LazyVim/LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
| [nocodb/nocodb](https://github.com/nocodb/nocodb) | 🔥 🔥 🔥 Open Source Airtable Alternative |
| [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) | WebGoat is a deliberately insecure application |
| [TEN-framework/ten-framework](https://github.com/TEN-framework/ten-framework) | Open-source framework for conversational voice AI agents. |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | very good whiteboard SDK / infinite canvas SDK |
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | A modern formatting library |
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
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [dataease/SQLBot](https://github.com/dataease/SQLBot) | 🔥 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG. |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
<!-- END OF MONTHLY_TOP10_REPOS -->
