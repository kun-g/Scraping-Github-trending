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
| [immich](https://github.com/immich-app/immich) | High performance self-hosted photo and video management solution. |
| [GPU-Puzzles](https://github.com/srush/GPU-Puzzles) | Solve puzzles. Learn CUDA. |
| [llama-recipes](https://github.com/meta-llama/llama-recipes) | Scripts for fine-tuning Meta Llama with composable FSDP & PEFT methods to cover single/multi-node GPUs. Supports default & custom datasets for applications such as summarization and Q&A. Supporting a number of candid inference solutions such as HF TGI, VLLM for local or cloud deployment. Demo apps to showcase Meta Llama for WhatsApp & Messenger. |
| [localsend](https://github.com/localsend/localsend) | An open-source cross-platform alternative to AirDrop |
| [llama-stack](https://github.com/meta-llama/llama-stack) | Model components of the Llama Stack APIs |
| [llama-stack-apps](https://github.com/meta-llama/llama-stack-apps) | Agentic components of the Llama Stack APIs |
| [anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [assistant-ui](https://github.com/Yonom/assistant-ui) | React Components for AI Chat 💬 🚀 |
| [dice](https://github.com/DiceDB/dice) | DiceDB is an in-memory real-time database with SQL-based reactivity. It is hyper-optimized for building and scaling truly real-time applications on modern hardware while being a drop-in replacement for Redis. |
| [hercules](https://github.com/src-d/hercules) | Gaining advanced insights from Git repository history. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [localsend](https://github.com/localsend/localsend) | An open-source cross-platform alternative to AirDrop |
| [supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
| [kamal](https://github.com/basecamp/kamal) | Deploy web apps anywhere. |
| [weekly](https://github.com/ruanyf/weekly) | 科技爱好者周刊，每周五发布 |
| [dice](https://github.com/DiceDB/dice) | DiceDB is an in-memory, real-time, and reactive database with Redis and SQL support optimized for modern hardware and building real-time applications. |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. |
| [anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | This repository is for active development of the Azure SDK for .NET. For consumers of the SDK we recommend visiting our public developer docs at https://learn.microsoft.com/dotnet/azure/ or our versioned developer docs at https://azure.github.io/azure-sdk-for-net. |
| [llama-stack](https://github.com/meta-llama/llama-stack) | Model components of the Llama Stack APIs |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ecapture](https://github.com/gojue/ecapture) | Capturing SSL/TLS plaintext without a CA certificate using eBPF. Supported on Linux/Android kernels for amd64/arm64. |
| [Follow](https://github.com/RSSNext/Follow) | 🧡 Next generation information browser. |
| [courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [firecrawl](https://github.com/mendableai/firecrawl) | 🔥 Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl and extract with a single API. |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [sherlock](https://github.com/sherlock-project/sherlock) | Hunt down social media accounts by username across social networks |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is an AI collaborative workspace where you achieve more without losing control of your data. The best open source alternative to Notion. |
| [nocodb](https://github.com/nocodb/nocodb) | 🔥 🔥 🔥 Open Source Airtable Alternative |
| [linutil](https://github.com/ChrisTitusTech/linutil) | Chris Titus Tech's Linux Toolbox - Linutil is a distro-agnostic toolbox designed to simplify everyday Linux tasks. |
| [erpnext](https://github.com/frappe/erpnext) | Free and Open Source Enterprise Resource Planning (ERP) |
<!-- END OF MONTHLY_TOP10_REPOS -->
