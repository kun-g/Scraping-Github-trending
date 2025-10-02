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
| [Done-0/fuck-u-code](https://github.com/Done-0/fuck-u-code) | Legacy-Mess Detector – assess the “legacy-mess level” of your code and output a beautiful report | 屎山代码检测器，评估代码的“屎山等级”并输出美观的报告 |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) |  |
| [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern design AI chat framework. Supports multiple AI providers (OpenAI / Claude 4 / Gemini / DeepSeek / Ollama / Qwen), Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application. |
| [nextcloud/server](https://github.com/nextcloud/server) | ☁️ Nextcloud server, a safe home for all your data |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | Community-contributed instructions, prompts, and configurations to help you make the most of GitHub Copilot. |
| [SDWebImage/SDWebImage](https://github.com/SDWebImage/SDWebImage) | Asynchronous image downloader with cache support as a UIImageView category |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more |
| [lukas-blecher/LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) | pix2tex: Using a ViT to convert images of equations into LaTeX code. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | The official repo for “Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting”, ACL, 2025. |
| [TanStack/router](https://github.com/TanStack/router) | 🤖 Fully typesafe Router for React (and friends) w/ built-in caching, 1st class search-param APIs, client-side cache integration and isomorphic rendering. |
| [oauth2-proxy/oauth2-proxy](https://github.com/oauth2-proxy/oauth2-proxy) | A reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers. |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) |  |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
| [cloudflare/capnweb](https://github.com/cloudflare/capnweb) | JavaScript/TypeScript-native, low-boilerplate, object-capability RPC system |
| [QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [bytebot-ai/bytebot](https://github.com/bytebot-ai/bytebot) | Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment. |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [dataease/SQLBot](https://github.com/dataease/SQLBot) | 🔥 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG. |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
<!-- END OF MONTHLY_TOP10_REPOS -->
