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
| [kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
| [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | Agent framework and applications built upon Qwen>=2.0, featuring Function Calling, Code Interpreter, RAG, and Chrome extension. |
| [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | DeepSeek Coder: Let the Code Write Itself |
| [monolith](https://github.com/bytedance/monolith) | A Lightweight Recommendation System |
| [sxt-proof-of-sql](https://github.com/spaceandtimelabs/sxt-proof-of-sql) | Space and Time | Proof of SQL |
| [nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |
| [jan](https://github.com/janhq/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [arnis](https://github.com/louis-e/arnis) | Generate any location from the real world in Minecraft Java Edition with a high level of detail. |
| [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | This repo includes ChatGPT prompt curation to use ChatGPT better. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [clay](https://github.com/nicbarker/clay) | High performance UI layout library in C. |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | A generative world for general-purpose robotics & embodied AI learning. |
| [monolith](https://github.com/bytedance/monolith) | A Lightweight Recommendation System |
| [cobalt](https://github.com/imputnet/cobalt) | best way to save what you love |
| [yazi](https://github.com/sxyazi/yazi) | 💥 Blazing fast terminal file manager written in Rust, based on async I/O. |
| [project-based-learning](https://github.com/practical-tutorials/project-based-learning) | Curated list of project-based tutorials |
| [tldraw](https://github.com/tldraw/tldraw) | whiteboard / infinite canvas SDK |
| [anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [uBlock](https://github.com/gorhill/uBlock) | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [eliza](https://github.com/elizaOS/eliza) | Autonomous agents for everyone |
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [cobalt](https://github.com/imputnet/cobalt) | best way to save what you love |
| [stock](https://github.com/myhhub/stock) | stock股票.获取股票数据,计算股票指标,识别股票形态,综合选股,选股策略,股票验证回测,股票自动交易,支持PC及移动设备。 |
| [fish-speech](https://github.com/fishaudio/fish-speech) | SOTA Open Source TTS |
| [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) | Python APIs for web automation, testing, and bypassing bot-detection. |
| [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Convert ebooks to audiobooks with chapters and metadata using dynamic AI models and voice cloning. Supports 1,107+ languages! |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Qwen / DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS/Plugins/Artifacts). One-click FREE deployment of your private ChatGPT/ Claude application. |
| [weekly](https://github.com/ruanyf/weekly) | 科技爱好者周刊，每周五发布 |
<!-- END OF MONTHLY_TOP10_REPOS -->
