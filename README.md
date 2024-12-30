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
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
| [pathway](https://github.com/pathwaycom/pathway) | Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG. |
| [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Convert ebooks to audiobooks with chapters and metadata using dynamic AI models and voice cloning. Supports 1,107+ languages! |
| [the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more. |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [siyuan](https://github.com/siyuan-note/siyuan) | A privacy-first, self-hosted, fully open source personal knowledge management software, written in typescript and golang. |
| [cherry-studio](https://github.com/kangfenmao/cherry-studio) | 🍒 Cherry Studio is a desktop client that supports for multiple LLM providers |
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
| [stock](https://github.com/myhhub/stock) | stock股票.获取股票数据,计算股票指标,识别股票形态,综合选股,选股策略,股票验证回测,股票自动交易,支持PC及移动设备。 |
| [cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/Docker |
| [aisuite](https://github.com/andrewyng/aisuite) | Simple, unified interface to multiple Generative AI providers |
| [cobalt](https://github.com/imputnet/cobalt) | best way to save what you love |
| [fish-speech](https://github.com/fishaudio/fish-speech) | SOTA Open Source TTS |
| [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) | Python APIs for web automation, testing, and bypassing bot-detection. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Qwen / DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS/Plugins/Artifacts). One-click FREE deployment of your private ChatGPT/ Claude application. |
| [langflow](https://github.com/langflow-ai/langflow) | Langflow is a low-code app builder for RAG and multi-agent AI applications. It’s Python-based and agnostic to any model, API, or database. |
<!-- END OF MONTHLY_TOP10_REPOS -->
