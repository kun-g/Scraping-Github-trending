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
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [commaai/openpilot](https://github.com/commaai/openpilot) | openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. |
| [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [Done-0/fuck-u-code](https://github.com/Done-0/fuck-u-code) | Legacy-Mess Detector – assess the “legacy-mess level” of your code and output a beautiful report | 屎山代码检测器，评估代码的“屎山等级”并输出美观的报告 |
| [frappe/erpnext](https://github.com/frappe/erpnext) | Free and Open Source Enterprise Resource Planning (ERP) |
| [snarktank/ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks) | A simple task management system for managing AI dev agents |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [adityatelange/hugo-PaperMod](https://github.com/adityatelange/hugo-PaperMod) | A fast, clean, responsive Hugo theme. |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 12 Lessons to Get Started Building AI Agents |
| [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | The Free Software Media System - Server Backend & API |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [Gar-b-age/CookLikeHOC](https://github.com/Gar-b-age/CookLikeHOC) | 🥢像老乡鸡🐔那样做饭。主要部分于2024年完工，非老乡鸡官方仓库。文字来自《老乡鸡菜品溯源报告》，并做归纳、编辑与整理。CookLikeHOC. |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | The official repo for “Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting”, ACL, 2025. |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | Free and Open Source, Distributed, RESTful Search Engine |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
| [WECENG/ticket-purchase](https://github.com/WECENG/ticket-purchase) | 大麦自动抢票，支持人员、城市、日期场次、价格选择 |
| [oauth2-proxy/oauth2-proxy](https://github.com/oauth2-proxy/oauth2-proxy) | A reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
| [bytebot-ai/bytebot](https://github.com/bytebot-ai/bytebot) | Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment. |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [dataease/SQLBot](https://github.com/dataease/SQLBot) | 🔥 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG. |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
<!-- END OF MONTHLY_TOP10_REPOS -->
