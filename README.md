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
| [network-api](https://github.com/nexus-xyz/network-api) | High-performance interface for supplying compute to the Nexus network. |
| [ghidra](https://github.com/NationalSecurityAgency/ghidra) | Ghidra is a software reverse engineering (SRE) framework |
| [source-sdk-2013](https://github.com/ValveSoftware/source-sdk-2013) | The 2013 edition of the Source SDK |
| [amazon-kindle-bulk-downloader](https://github.com/treetrum/amazon-kindle-bulk-downloader) | Allows you to bulk download all your Kindle eBook in a more automated fashion. This tool allows you to create backup copies of the books you've already purchased. |
| [mastra](https://github.com/mastra-ai/mastra) | the TypeScript AI agent framework |
| [pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | Chat with your database or your datalake (SQL, CSV, parquet). PandasAI makes data analysis conversational using LLMs and RAG. |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [bootstrap](https://github.com/twbs/bootstrap) | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| [firebase-ios-sdk](https://github.com/firebase/firebase-ios-sdk) | Firebase SDK for Apple App Development |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [OmniParser](https://github.com/microsoft/OmniParser) | A simple screen parsing tool towards pure vision based GUI agent |
| [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Automate the process of making money online. |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
| [rustowl](https://github.com/cordx56/rustowl) | Visualize Ownership and Lifetimes in Rust |
| [hummingbot](https://github.com/hummingbot/hummingbot) | Open source software that helps you create and deploy high-frequency crypto trading bots |
| [docmost](https://github.com/docmost/docmost) | Docmost is an open-source collaborative wiki and documentation software. It is an open-source alternative to Confluence and Notion. |
| [markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | Build your own AI friend |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [OmniParser](https://github.com/microsoft/OmniParser) | A simple screen parsing tool towards pure vision based GUI agent |
| [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | DeepSeek Coder: Let the Code Write Itself |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 2, and other large language models. |
| [unsloth](https://github.com/unslothai/unsloth) | Finetune Llama 3.3, DeepSeek-R1 & Reasoning LLMs 2x faster with 70% less memory! 🦥 |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, and more. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [browser-use](https://github.com/browser-use/browser-use) | Make websites accessible for AI agents |
| [onlook](https://github.com/onlook-dev/onlook) | The open source Cursor for Designers. Design directly in your live React app and publish your changes to code. |
| [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) | DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence |
<!-- END OF MONTHLY_TOP10_REPOS -->
