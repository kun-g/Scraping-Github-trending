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
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [gofiber/fiber](https://github.com/gofiber/fiber) | ⚡️ Express inspired web framework written in Go |
| [eslint/eslint](https://github.com/eslint/eslint) | Find and fix problems in your JavaScript code. |
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | A modern formatting library |
| [mtdvio/every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know) | A collection of (mostly) technical things every software developer should know about |
| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |
| [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | OpenZeppelin Contracts is a library for secure smart contract development. |
| [Gar-b-age/CookLikeHOC](https://github.com/Gar-b-age/CookLikeHOC) | 🥢像老乡鸡🐔那样做饭。主要部分于2024年完工，非老乡鸡官方仓库。文字来自《老乡鸡菜品溯源报告》，并做归纳、编辑与整理。CookLikeHOC. |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [category-labs/monad](https://github.com/category-labs/monad) |  |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [nocodb/nocodb](https://github.com/nocodb/nocodb) | 🔥 🔥 🔥 Open Source Airtable Alternative |
| [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | Perplexica is an AI-powered search engine. It is an Open source alternative to Perplexity AI |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) | WebGoat is a deliberately insecure application |
| [TEN-framework/ten-framework](https://github.com/TEN-framework/ten-framework) | Open-source framework for conversational voice AI agents. |
| [LazyVim/LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | all of the workflows of n8n i could find (also from the site itself) |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
| [dockur/windows](https://github.com/dockur/windows) | Windows inside a Docker container. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [dataease/SQLBot](https://github.com/dataease/SQLBot) | 🔥 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG. |
| [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) | Clone a voice in 5 seconds to generate arbitrary speech in real-time |
<!-- END OF MONTHLY_TOP10_REPOS -->
