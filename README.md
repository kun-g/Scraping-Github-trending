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
| [tokio](https://github.com/tokio-rs/tokio) | A runtime for writing reliable asynchronous applications with Rust. Provides I/O, networking, scheduling, timers, ... |
| [mem0](https://github.com/mem0ai/mem0) | The memory layer for Personalized AI |
| [runner-images](https://github.com/actions/runner-images) | GitHub Actions runner images |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | A WebUI for Efficient Fine-Tuning of 100+ LLMs (ACL 2024) |
| [git-credential-manager](https://github.com/git-ecosystem/git-credential-manager) | Secure, cross-platform Git credential storage with authentication to GitHub, Azure Repos, and other popular Git hosting services. |
| [Win11Debloat](https://github.com/Raphire/Win11Debloat) | A simple, easy to use PowerShell script to remove pre-installed apps from windows, disable telemetry, remove Bing from windows search as well as perform various other changes to declutter and improve your windows experience. This script works for both windows 10 and windows 11. |
| [terraform-aws-eks](https://github.com/terraform-aws-modules/terraform-aws-eks) | Terraform module to create Amazon Elastic Kubernetes (EKS) resources 🇺🇦 |
| [lo](https://github.com/samber/lo) | 💥 A Lodash-style Go library based on Go 1.18+ Generics (map, filter, contains, find...) |
| [vault](https://github.com/hashicorp/vault) | A tool for secrets management, encryption as a service, and privileged access management |
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
| [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 30 days of Python programming challenge is a step-by-step guide to learn the Python programming language in 30 days. This challenge may take more than100 days, follow your own pace. These videos may help too: https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [HowToCook](https://github.com/Anduin2017/HowToCook) | 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only). |
| [mindsdb](https://github.com/mindsdb/mindsdb) | The platform for building AI from enterprise data |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | Open-Sora: Democratizing Efficient Video Production for All |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Brand new TTS solution |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
<!-- END OF MONTHLY_TOP10_REPOS -->
