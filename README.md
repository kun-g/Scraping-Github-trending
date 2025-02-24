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
| [aibrix](https://github.com/vllm-project/aibrix) | Cost-efficient and pluggable Infrastructure components for GenAI inference |
| [mastra](https://github.com/mastra-ai/mastra) | the TypeScript AI agent framework |
| [FreeTube](https://github.com/FreeTubeApp/FreeTube) | An Open Source YouTube app for privacy |
| [invoify](https://github.com/al1abb/invoify) | An invoice generator app built using Next.js, Typescript, and Shadcn |
| [shadPS4](https://github.com/shadps4-emu/shadPS4) | PlayStation 4 emulator for Windows, Linux and macOS written in C++ |
| [llm-scraper](https://github.com/mishushakov/llm-scraper) | Turn any webpage into structured data using LLMs |
| [zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) |  |
| [browser-use](https://github.com/browser-use/browser-use) | Make websites accessible for AI agents |
| [pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | Chat with your database or your datalake (SQL, CSV, parquet). PandasAI makes data analysis conversational using LLMs and RAG. |
| [neovim](https://github.com/neovim/neovim) | Vim-fork focused on extensibility and usability |
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
