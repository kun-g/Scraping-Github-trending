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
| [tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant |
| [qwerty-learner](https://github.com/RealKai42/qwerty-learner) | 为键盘工作者设计的单词记忆与英语肌肉记忆锻炼软件 / Words learning and English muscle memory training software designed for keyboard workers |
| [ubicloud](https://github.com/ubicloud/ubicloud) | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, and IAM services in public beta. |
| [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Convert ebooks to audiobooks with chapters and metadata using dynamic AI models and voice cloning. Supports 1,107+ languages! |
| [GlaDOS](https://github.com/dnhkng/GlaDOS) | This is the Personality Core for GLaDOS, the first steps towards a real-life implementation of the AI from the Portal series by Valve. |
| [automatisch](https://github.com/automatisch/automatisch) | The open source Zapier alternative. Build workflow automation without spending time and money. |
| [agent-service-toolkit](https://github.com/JoshuaC215/agent-service-toolkit) | Full toolkit for running an AI agent service built with LangGraph, FastAPI and Streamlit |
| [winutil](https://github.com/ChrisTitusTech/winutil) | Chris Titus Tech's Windows Utility - Install Programs, Tweaks, Fixes, and Updates |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is the AI collaborative workspace where you achieve more without losing control of your data. The leading open source Notion alternative. |
| [Perplexica](https://github.com/ItzCrazyKns/Perplexica) | Perplexica is an AI-powered search engine. It is an Open source alternative to Perplexity AI |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [swarms](https://github.com/kyegomez/swarms) | The Enterprise-Grade Production-Ready Multi-Agent Orchestration Framework Join our Community: https://discord.gg/jM3Z6M9uMq |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [miniperplx](https://github.com/zaidmukaddam/miniperplx) | A minimalistic AI-powered search engine that helps you find information on the internet. Powered by Vercel AI SDK! Search with models like Grok 2.0. |
| [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | Build your own AI friend |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🙌 OpenHands: Code Less, Make More |
| [cline](https://github.com/cline/cline) | Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. |
| [nv-ingest](https://github.com/NVIDIA/nv-ingest) | NVIDIA Ingest is an early access set of microservices for parsing hundreds of thousands of complex, messy unstructured PDFs and other enterprise documents into metadata and text to embed into retrieval systems. |
| [WrenAI](https://github.com/Canner/WrenAI) | 🤖 Open-source AI Agent that empowers data-driven teams to chat with their data to generate Text-to-SQL, charts, spreadsheets, reports, and BI. 📈📊📋🧑‍💻 |
| [arnis](https://github.com/louis-e/arnis) | Generate any location from the real world in Minecraft Java Edition with a high level of detail. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [eliza](https://github.com/elizaOS/eliza) | Autonomous agents for everyone |
| [cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [cline](https://github.com/cline/cline) | Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. |
| [khoj](https://github.com/khoj-ai/khoj) | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free. |
| [KAG](https://github.com/OpenSPG/KAG) | KAG is a logical form-guided reasoning and retrieval framework based on OpenSPG engine and LLMs. It is used to build logical reasoning and factual Q&A solutions for professional domain knowledge bases. It can effectively overcome the shortcomings of the traditional RAG vector similarity calculation model. |
| [limbo](https://github.com/tursodatabase/limbo) | Limbo is a work-in-progress, in-process OLTP database management system, compatible with SQLite. |
| [cobalt](https://github.com/imputnet/cobalt) | best way to save what you love |
<!-- END OF MONTHLY_TOP10_REPOS -->
