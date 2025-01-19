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
| [MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | MiniCPM-o 2.6: A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming on Your Phone |
| [tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant |
| [server](https://github.com/nextcloud/server) | ☁️ Nextcloud server, a safe home for all your data |
| [fluentassertions](https://github.com/fluentassertions/fluentassertions) | A very extensive set of extension methods that allow you to more naturally specify the expected outcome of a TDD or BDD-style unit tests. Targets .NET Framework 4.7, as well as .NET Core 2.1, .NET Core 3.0, .NET 6, .NET Standard 2.0 and 2.1. Supports the unit test frameworks MSTest2, NUnit3, XUnit2, MSpec, and NSpec3. |
| [llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [terraform](https://github.com/hashicorp/terraform) | Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned. |
| [spree](https://github.com/spree/spree) | An open source eCommerce platform giving you full control and customizability. Modular and API-first. Multi-vendor, multi-tenant, multi-store, multi-currency, multi-language. Built using Ruby on Rails. Developed by @vendo-dev |
| [chainlit](https://github.com/Chainlit/chainlit) | Build Conversational AI in minutes ⚡️ |
| [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) | A robust, efficient, low-latency speech-to-text library with advanced voice activity detection, wake word activation and instant transcription. |
| [metabase](https://github.com/metabase/metabase) | The simplest, fastest way to get business intelligence and analytics to everyone in your company 😋 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant |
| [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) | A robust, efficient, low-latency speech-to-text library with advanced voice activity detection, wake word activation and instant transcription. |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [GlaDOS](https://github.com/dnhkng/GlaDOS) | This is the Personality Core for GLaDOS, the first steps towards a real-life implementation of the AI from the Portal series by Valve. |
| [WrenAI](https://github.com/Canner/WrenAI) | 🤖 Open-source AI Agent that empowers data-driven teams to chat with their data to generate Text-to-SQL, charts, spreadsheets, reports, and BI. 📈📊📋🧑‍💻 |
| [Sana](https://github.com/NVlabs/Sana) | SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer |
| [ton](https://github.com/ton-blockchain/ton) | Main TON monorepo |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper |
| [code2prompt](https://github.com/mufeedvh/code2prompt) | A CLI tool to convert your codebase into a single LLM prompt with source tree, prompt templating, and token counting. |
| [ultravox](https://github.com/fixie-ai/ultravox) | A fast multimodal LLM for real-time voice |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [clay](https://github.com/nicbarker/clay) | High performance UI layout library in C. |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [khoj](https://github.com/khoj-ai/khoj) | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free. |
| [eliza](https://github.com/elizaOS/eliza) | Autonomous agents for everyone |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper |
| [KAG](https://github.com/OpenSPG/KAG) | KAG is a logical form-guided reasoning and retrieval framework based on OpenSPG engine and LLMs. It is used to build logical reasoning and factual Q&A solutions for professional domain knowledge bases. It can effectively overcome the shortcomings of the traditional RAG vector similarity calculation model. |
| [cline](https://github.com/cline/cline) | Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. |
| [tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant |
| [nv-ingest](https://github.com/NVIDIA/nv-ingest) | NVIDIA Ingest is an early access set of microservices for parsing hundreds of thousands of complex, messy unstructured PDFs and other enterprise documents into metadata and text to embed into retrieval systems. |
<!-- END OF MONTHLY_TOP10_REPOS -->
