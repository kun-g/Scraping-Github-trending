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
| [data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [GetQzonehistory](https://github.com/LibraHp/GetQzonehistory) | 获取QQ空间发布的历史说说 |
| [douyin](https://github.com/zyronon/douyin) | Vue3 + Pinia 仿抖音，Vue 在移动端的最佳实践 . Imitate TikTok ，Vue Best practices on Mobile |
| [chatnio](https://github.com/zmh-program/chatnio) | 🚀 Next Generation AI One-Stop Internationalization Solution. 🚀 下一代 AI 一站式 B/C 端解决方案，支持 OpenAI，Midjourney，Claude，讯飞星火，Stable Diffusion，DALL·E，ChatGLM，通义千问，腾讯混元，360 智脑，百川 AI，火山方舟，新必应，Gemini，Moonshot 等模型，支持对话分享，自定义预设，云端同步，模型市场，支持弹性计费和订阅计划模式，支持图片解析，支持联网搜索，支持模型缓存，丰富美观的后台管理与仪表盘数据统计。 |
| [best-of-ml-python](https://github.com/ml-tooling/best-of-ml-python) | 🏆 A ranked list of awesome machine learning Python libraries. Updated weekly. |
| [grafana](https://github.com/grafana/grafana) | The open and composable observability and data visualization platform. Visualize metrics, logs, and traces from multiple sources like Prometheus, Loki, Elasticsearch, InfluxDB, Postgres and many more. |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [bootstrap](https://github.com/twbs/bootstrap) | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| [immich](https://github.com/immich-app/immich) | High performance self-hosted photo and video management solution. |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🙌 OpenHands: Code Less, Make More |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [skyvern](https://github.com/Skyvern-AI/skyvern) | Automate browser-based workflows with LLMs and Computer Vision |
| [courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [TV](https://github.com/Guovin/TV) | 📺IPTV电视直播源更新工具🚀：包含💰央视(付费)、📡卫视、🏠广东、🌊港·澳·台、🎬电影、🎥咪咕、🏀体育、🪁动画、🎮游戏、🎵音乐、🏛经典剧场；支持自定义增加频道；支持组播源、酒店源、订阅源、关键字搜索；每天自动更新两次，结果可用于TVBox等播放软件；支持工作流、Docker(amd64/arm64)、命令行、GUI运行方式 | IPTV live TV source update tool |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | A community-supported supercharged version of paperless: scan, index and archive all your physical documents |
| [ToolJet](https://github.com/ToolJet/ToolJet) | Low-code platform for building business applications. Connect to databases, cloud storages, GraphQL, API endpoints, Airtable, Google sheets, OpenAI, etc and build apps using drag and drop application builder. Built using JavaScript/TypeScript. 🚀 |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | The best and simplest free open source web page change detection, website watcher, restock monitor and notification service. Restock Monitor, change detection. Designed for simplicity - Simply monitor which websites had a text change for free. Free Open source web page change detection, Website defacement monitoring, Price change notification |
| [PowerShell](https://github.com/PowerShell/PowerShell) | PowerShell for every system! |
| [mindcraft](https://github.com/kolbytn/mindcraft) |  |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [platform](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Agents with memory, knowledge, tools and reasoning. Chat with them using a beautiful Agent UI. |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
| [surya](https://github.com/VikParuchuri/surya) | OCR, layout analysis, reading order, table recognition in 90+ languages |
| [formbricks](https://github.com/formbricks/formbricks) | Open Source Survey Platform |
| [videos](https://github.com/3b1b/videos) | Code for the manim-generated scenes used in 3blue1brown videos |
| [agents](https://github.com/livekit/agents) | Build real-time multimodal AI applications 🤖🎙️📹 |
| [mindcraft](https://github.com/kolbytn/mindcraft) |  |
<!-- END OF MONTHLY_TOP10_REPOS -->
