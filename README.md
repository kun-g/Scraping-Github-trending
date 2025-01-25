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
| [shadPS4](https://github.com/shadps4-emu/shadPS4) | PlayStation 4 emulator for Windows, Linux and macOS written in C++ |
| [midscene](https://github.com/web-infra-dev/midscene) | AI-Driven Browser Automation with Chrome Extensions, JavaScript, and YAML Scripts. |
| [it-tools](https://github.com/CorentinTh/it-tools) | Collection of handy online tools for developers, with great UX. |
| [Reactive-Resume](https://github.com/AmruthPillai/Reactive-Resume) | A one-of-a-kind resume builder that keeps your privacy in mind. Completely secure, customizable, portable, open-source and free forever. Try it out today! |
| [storybook](https://github.com/storybookjs/storybook) | Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation |
| [mlx-swift-examples](https://github.com/ml-explore/mlx-swift-examples) | Examples using MLX Swift |
| [saas-starter](https://github.com/nextjs/saas-starter) | Get started quickly with Next.js, Postgres, Stripe, and shadcn/ui. |
| [firecrawl](https://github.com/mendableai/firecrawl) | 🔥 Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl and extract with a single API. |
| [ragflow](https://github.com/infiniflow/ragflow) | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. |
| [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) |  |
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
