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
| [Amphion](https://github.com/open-mmlab/Amphion) | Amphion (/æmˈfaɪən/) is a toolkit for Audio, Music, and Speech Generation. Its purpose is to support reproducible research and help junior researchers and engineers get started in the field of audio, music, and speech generation research and development. |
| [memos](https://github.com/usememos/memos) | An open-source, lightweight note-taking solution. The pain-less way to create your meaningful notes. Your Notes, Your Way. |
| [llama-recipes](https://github.com/meta-llama/llama-recipes) | Scripts for fine-tuning Meta Llama with composable FSDP & PEFT methods to cover single/multi-node GPUs. Supports default & custom datasets for applications such as summarization and Q&A. Supporting a number of candid inference solutions such as HF TGI, VLLM for local or cloud deployment. Demo apps to showcase Meta Llama for WhatsApp & Messenger. |
| [omnivore](https://github.com/omnivore-app/omnivore) | Omnivore is a complete, open source read-it-later solution for people who like reading. |
| [novu](https://github.com/novuhq/novu) | Open-Source Notification Platform. Embeddable Notification Center, E-mail, Push and Slack Integrations. |
| [ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | 分流规则、重写写规则及脚本。 |
| [rustdesk](https://github.com/rustdesk/rustdesk) | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is an AI collaborative workspace where you achieve more without losing control of your data. The best open source alternative to Notion. |
| [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | A community-supported supercharged version of paperless: scan, index and archive all your physical documents |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | The best and simplest free open source web page change detection, website watcher, restock monitor and notification service. Restock Monitor, change detection. Designed for simplicity - Simply monitor which websites had a text change for free. Free Open source web page change detection, Website defacement monitoring, Price change notification |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Agents with memory, knowledge, tools and reasoning. Chat with them using a beautiful Agent UI. |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database diagram editor and SQL generator. |
| [co-tracker](https://github.com/facebookresearch/co-tracker) | CoTracker is a model for tracking any point (pixel) on a video. |
| [social-app](https://github.com/bluesky-social/social-app) | The Bluesky Social application for Web, iOS, and Android |
| [mindcraft](https://github.com/kolbytn/mindcraft) |  |
| [yfinance](https://github.com/ranaroussi/yfinance) | Download market data from Yahoo! Finance's API |
| [deepface](https://github.com/serengil/deepface) | A Lightweight Face Recognition and Facial Attribute Analysis (Age, Gender, Emotion and Race) Library for Python |
| [cocos-engine](https://github.com/cocos/cocos-engine) | Cocos simplifies game creation and distribution with Cocos Creator, a free, open-source, cross-platform game engine. Empowering millions of developers to create high-performance, engaging 2D/3D games and instant web entertainment. |
| [fingerprintjs](https://github.com/fingerprintjs/fingerprintjs) | The most advanced browser fingerprinting library. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🔥🕷️ Crawl4AI: Open-source LLM Friendly Web Crawler & Scrapper |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [platform](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) |
| [screenpipe](https://github.com/mediar-ai/screenpipe) | 24/7 local AI screen & mic recording. Start recording your screen today ... or be left behind. Works with Ollama. Alternative to Rewind.ai & Zapier. Open. Secure. You own your data. Rust. |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [llama-stack](https://github.com/meta-llama/llama-stack) | Model components of the Llama Stack APIs |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Agents with memory, knowledge, tools and reasoning. Chat with them using a beautiful Agent UI. |
| [kestra](https://github.com/kestra-io/kestra) | ⚡ Workflow Automation Platform. Orchestrate & Schedule code in any language, run anywhere, 500+ plugins. Alternative to Zapier, Rundeck, Camunda, Airflow... |
| [surya](https://github.com/VikParuchuri/surya) | OCR, layout analysis, reading order, table recognition in 90+ languages |
| [videos](https://github.com/3b1b/videos) | Code for the manim-generated scenes used in 3blue1brown videos |
<!-- END OF MONTHLY_TOP10_REPOS -->
