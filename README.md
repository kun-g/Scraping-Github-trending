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
| [MiniCPM](https://github.com/OpenBMB/MiniCPM) | MiniCPM3-4B: An edge-side LLM that surpasses GPT-3.5-Turbo. |
| [Follow](https://github.com/RSSNext/Follow) | 🧡 Next generation information browser |
| [wealthfolio](https://github.com/afadil/wealthfolio) | A Beautiful Private and Secure Desktop Investment Tracking Application |
| [dice](https://github.com/DiceDB/dice) | DiceDB is an in-memory real-time database with SQL-based reactivity. It is hyper-optimized for building and scaling truly real-time applications on modern hardware while being a drop-in replacement for Redis. |
| [nginx](https://github.com/nginx/nginx) | The official NGINX Open Source repository. |
| [rustdesk](https://github.com/rustdesk/rustdesk) | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [MusicFree](https://github.com/maotoumao/MusicFree) | 插件化、定制化、无广告的免费音乐播放器 |
| [helix](https://github.com/helix-editor/helix) | A post-modern modal text editor. |
| [jd](https://github.com/josephburnett/jd) | JSON diff and patch |
| [langflow](https://github.com/langflow-ai/langflow) | Langflow is a low-code app builder for RAG and multi-agent AI applications. It’s Python-based and agnostic to any model, API, or database. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [linutil](https://github.com/ChrisTitusTech/linutil) | Chris Titus Tech's Linux Toolbox - Linutil is a distro-agnostic toolbox designed to simplify everyday Linux tasks. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Azure / DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT/ Claude application. |
| [firecrawl](https://github.com/mendableai/firecrawl) | 🔥 Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl and extract with a single API. |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is an AI collaborative workspace where you achieve more without losing control of your data. The best open source alternative to Notion. |
| [anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [dokku](https://github.com/dokku/dokku) | A docker-powered PaaS that helps you build and manage the lifecycle of applications |
| [faceswap](https://github.com/deepfakes/faceswap) | Deepfakes Software For All |
| [continue](https://github.com/continuedev/continue) | ⏩ Continue is the leading open-source AI code assistant. You can connect any models and any context to build custom autocomplete and chat experiences inside VS Code and JetBrains |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
| [authentik](https://github.com/goauthentik/authentik) | The authentication glue you need. |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is an AI collaborative workspace where you achieve more without losing control of your data. The best open source alternative to Notion. |
| [roop](https://github.com/s0md3v/roop) | one-click face swap |
| [erpnext](https://github.com/frappe/erpnext) | Free and Open Source Enterprise Resource Planning (ERP) |
| [CogVideo](https://github.com/THUDM/CogVideo) | Text-to-video generation: CogVideoX (2024) and CogVideo (ICLR 2023) |
| [FlClash](https://github.com/chen08209/FlClash) | A multi-platform proxy client based on ClashMeta,simple and easy to use, open-source and ad-free. |
| [sherlock](https://github.com/sherlock-project/sherlock) | Hunt down social media accounts by username across social networks |
<!-- END OF MONTHLY_TOP10_REPOS -->
