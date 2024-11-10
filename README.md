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
| [prefect](https://github.com/PrefectHQ/prefect) | Prefect is a workflow orchestration framework for building resilient data pipelines in Python. |
| [Bjorn](https://github.com/infinition/Bjorn) | Bjorn is a powerful network scanning and offensive security tool for the Raspberry Pi with a 2.13-inch e-Paper HAT. It discovers network targets, identifies open ports, exposed services, and potential vulnerabilities. Bjorn can perform brute force attacks, file stealing, host zombification, and supports custom attack scripts. |
| [immich](https://github.com/immich-app/immich) | High performance self-hosted photo and video management solution. |
| [payload](https://github.com/payloadcms/payload) | Payload is the open-source, fullstack Next.js framework, giving you instant backend superpowers. Get a full TypeScript backend and admin panel instantly. Use Payload as a headless CMS or for building powerful applications. |
| [CogVideo](https://github.com/THUDM/CogVideo) | text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023) |
| [GetQzonehistory](https://github.com/LibraHp/GetQzonehistory) | 获取QQ空间发布的历史说说 |
| [go2rtc](https://github.com/AlexxIT/go2rtc) | Ultimate camera streaming application with support RTSP, RTMP, HTTP-FLV, WebRTC, MSE, HLS, MP4, MJPEG, HomeKit, FFmpeg, etc. |
| [black](https://github.com/psf/black) | The uncompromising Python code formatter |
| [SmartTube](https://github.com/yuliskov/SmartTube) | SmartTube - an advanced player for set-top boxes and tvs running Android OS |
| [Sa-Token](https://github.com/dromara/Sa-Token) | 一个轻量级 Java 权限认证框架，让鉴权变得简单、优雅！—— 登录认证、权限认证、分布式Session会话、微服务网关鉴权、单点登录、OAuth2.0 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [docling](https://github.com/DS4SD/docling) | Get your documents ready for gen AI |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🙌 OpenHands: Code Less, Make More |
| [diagrams](https://github.com/mingrammer/diagrams) | 🎨 Diagram as Code for prototyping cloud system architectures |
| [jsoncrack.com](https://github.com/AykutSarac/jsoncrack.com) | ✨ Innovative and open-source visualization application that transforms various data formats, such as JSON, YAML, XML, CSV and more, into interactive graphs. |
| [kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
| [localsend](https://github.com/localsend/localsend) | An open-source cross-platform alternative to AirDrop |
| [kestra](https://github.com/kestra-io/kestra) | ⚡ Workflow Automation Platform. Orchestrate & Schedule code in any language, run anywhere, 500+ plugins. Alternative to Zapier, Rundeck, Camunda, Airflow... |
| [twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [khoj](https://github.com/khoj-ai/khoj) | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (e.g gpt, claude, gemini, llama, qwen, mistral). |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Agents with memory, knowledge, tools and reasoning. Chat with them using a beautiful Agent UI. |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [docling](https://github.com/DS4SD/docling) | Get your documents ready for gen AI |
| [videos](https://github.com/3b1b/videos) | Code for the manim-generated scenes used in 3blue1brown videos |
| [twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
| [surya](https://github.com/VikParuchuri/surya) | OCR, layout analysis, reading order, table recognition in 90+ languages |
| [social-app](https://github.com/bluesky-social/social-app) | The Bluesky Social application for Web, iOS, and Android |
| [platform](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
<!-- END OF MONTHLY_TOP10_REPOS -->
