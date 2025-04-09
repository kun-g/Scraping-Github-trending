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
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | "LightRAG: Simple and Fast Retrieval-Augmented Generation" |
| [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) | Connect Supabase to your AI assistants |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [getmaxun/maxun](https://github.com/getmaxun/maxun) | 🔥Open Source No Code Web Data Extraction Platform. Turn Websites To APIs & Spreadsheets With No-Code Robots In Minutes🔥 |
| [datawhalechina/llm-cookbook](https://github.com/datawhalechina/llm-cookbook) | 面向开发者的 LLM 入门教程，吴恩达大模型系列课程中文版 |
| [SimplifyJobs/Summer2025-Internships](https://github.com/SimplifyJobs/Summer2025-Internships) | Collection of Summer 2025 tech internships! |
| [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | Multiplayer at the speed of light |
| [modelscope/FunASR](https://github.com/modelscope/FunASR) | A Fundamental End-to-End Speech Recognition Toolkit and Open Source SOTA Pretrained Models, Supporting Speech Recognition, Voice Activity Detection, Text Post-processing etc. |
| [chartdb/chartdb](https://github.com/chartdb/chartdb) | Database diagrams editor that allows you to visualize and design your DB with a single query. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [th-ch/youtube-music](https://github.com/th-ch/youtube-music) | YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader) |
| [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) | Free, simple, fast interactive diagrams for any GitHub repository |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | A collection of MCP servers. |
| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools. |
| [Flowseal/zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) |  |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [yetone/avante.nvim](https://github.com/yetone/avante.nvim) | Use your Neovim like using Cursor AI IDE! |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here:https://discord.gg/jP8KfhDhyN |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | A collection of MCP servers. |
| [GuijiAI/HeyGem.ai](https://github.com/GuijiAI/HeyGem.ai) |  |
| [glanceapp/glance](https://github.com/glanceapp/glance) | A self-hosted dashboard that puts all your feeds in one place |
| [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) | Free, simple, fast interactive diagrams for any GitHub repository |
| [th-ch/youtube-music](https://github.com/th-ch/youtube-music) | YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader) |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | 📄 A curated list of awesome .cursorrules files |
| [DiceDB/dice](https://github.com/DiceDB/dice) | DiceDB is an open-source, fast, reactive, in-memory database optimized for modern hardware. |
<!-- END OF MONTHLY_TOP10_REPOS -->
