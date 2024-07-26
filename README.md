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
| [maestro](https://github.com/Netflix/maestro) | Maestro: Netflix’s Workflow Orchestrator |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [llama3](https://github.com/meta-llama/llama3) | The official Meta Llama 3 GitHub site |
| [dotnet-starter-kit](https://github.com/fullstackhero/dotnet-starter-kit) | Production Grade Cloud-Ready .NET 8 Starter Kit (Web API + Blazor Client) with Multitenancy Support, and Clean/Modular Architecture that saves roughly 200+ Development Hours! All Batteries Included. |
| [LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [hoppscotch](https://github.com/hoppscotch/hoppscotch) | Open source API development ecosystem - https://hoppscotch.io (open-source alternative to Postman, Insomnia) |
| [lz4](https://github.com/lz4/lz4) | Extremely Fast Compression algorithm |
| [spdlog](https://github.com/gabime/spdlog) | Fast C++ logging library. |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | LLM inference in C/C++ |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [books](https://github.com/free-educa/books) | o armazém de livros |
| [llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder) | Neo4j graph construction from unstructured data using LLMs |
| [MinerU](https://github.com/opendatalab/MinerU) | A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。 |
| [tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant |
| [pytube](https://github.com/pytube/pytube) | A lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos. |
| [crawlee-python](https://github.com/apify/crawlee-python) | Crawlee—A web scraping and browser automation library for Python to build reliable crawlers. Extract data for AI, LLMs, RAG, or GPTs. Download HTML, PDF, JPG, PNG, and other files from websites. Works with BeautifulSoup, Playwright, and raw HTTP. Both headful and headless mode. With proxy rotation. |
| [git-credential-manager](https://github.com/git-ecosystem/git-credential-manager) | Secure, cross-platform Git credential storage with authentication to GitHub, Azure Repos, and other popular Git hosting services. |
| [helix](https://github.com/helix-editor/helix) | A post-modern modal text editor. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ImHex](https://github.com/WerWolv/ImHex) | 🔍 A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 30 days of Python programming challenge is a step-by-step guide to learn the Python programming language in 30 days. This challenge may take more than100 days, follow your own pace. These videos may help too: https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [mindsdb](https://github.com/mindsdb/mindsdb) | The platform for building AI from enterprise data |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Brand new TTS solution |
| [maestro](https://github.com/Doriandarko/maestro) | A framework for Claude Opus to intelligently orchestrate subagents. |
| [books](https://github.com/free-educa/books) | o armazém de livros |
<!-- END OF MONTHLY_TOP10_REPOS -->
