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
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper |
| [kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
| [loco](https://github.com/loco-rs/loco) | 🚂 🦀 The one-person framework for Rust for side-projects and startups |
| [swarms](https://github.com/kyegomez/swarms) | The Enterprise-Grade Production-Ready Multi-Agent Orchestration Framework Join our Community: https://discord.com/servers/agora-999382051935506503 |
| [core](https://github.com/home-assistant/core) | 🏡 Open source home automation that puts local control and privacy first. |
| [bitcoin](https://github.com/bitcoin/bitcoin) | Bitcoin Core integration/staging tree |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🙌 OpenHands: Code Less, Make More |
| [ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community) | CISO Assistant is a one-stop-shop for GRC, covering Risk, AppSec and Audit Management and supporting +70 frameworks worldwide with auto-mapping: NIST CSF, ISO 27001, SOC2, CIS, PCI DSS, NIS2, CMMC, PSPF, GDPR, HIPAA, Essential Eight, NYDFS-500, DORA, NIST AI RMF, 800-53, 800-171, CyFun, CJIS, AirCyber, NCSC, ECC, SCF and so much more |
| [arnis](https://github.com/louis-e/arnis) | Generate any location from the real world in Minecraft Java Edition with a high level of detail. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Convert ebooks to audiobooks with chapters and metadata using dynamic AI models and voice cloning. Supports 1,107+ languages! |
| [KAG](https://github.com/OpenSPG/KAG) | KAG is a logical form-guided reasoning and retrieval framework based on OpenSPG engine and LLMs. It is used to build logical reasoning and factual Q&A solutions for professional domain knowledge bases. It can effectively overcome the shortcomings of the traditional RAG vector similarity calculation model. |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [eliza](https://github.com/elizaOS/eliza) | Autonomous agents for everyone |
| [monolith](https://github.com/bytedance/monolith) | A Lightweight Recommendation System |
| [jan](https://github.com/janhq/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [eliza](https://github.com/elizaOS/eliza) | Autonomous agents for everyone |
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Convert ebooks to audiobooks with chapters and metadata using dynamic AI models and voice cloning. Supports 1,107+ languages! |
| [cobalt](https://github.com/imputnet/cobalt) | best way to save what you love |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent Framework / shim to use Pydantic with LLMs |
| [cline](https://github.com/cline/cline) | Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) | Python APIs for web automation, testing, and bypassing bot-detection. |
<!-- END OF MONTHLY_TOP10_REPOS -->
