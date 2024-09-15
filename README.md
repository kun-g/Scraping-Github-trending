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
| [ecapture](https://github.com/gojue/ecapture) | Capturing SSL/TLS plaintext without a CA certificate using eBPF. Supported on Linux/Android kernels for amd64/arm64. |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Brand new TTS solution |
| [paper-qa](https://github.com/Future-House/paper-qa) | High accuracy RAG for answering questions from scientific documents with citations |
| [jax](https://github.com/google/jax) | Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more |
| [svelte](https://github.com/sveltejs/svelte) | Cybernetically enhanced web apps |
| [GoodbyeDPI](https://github.com/ValdikSS/GoodbyeDPI) | GoodbyeDPI — Deep Packet Inspection circumvention utility (for Windows) |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [taipy](https://github.com/Avaiga/taipy) | Turns Data and AI algorithms into production-ready web applications in no time. |
| [computer-science](https://github.com/ossu/computer-science) | 🎓 Path to a free self-taught education in Computer Science! |
| [googletest](https://github.com/google/googletest) | GoogleTest - Google Testing and Mocking Framework |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Follow](https://github.com/RSSNext/Follow) | 🧡 Next generation information browser. |
| [MiniCPM](https://github.com/OpenBMB/MiniCPM) | MiniCPM3-4B: An edge-side LLM that surpasses GPT-3.5-Turbo. |
| [it-tools](https://github.com/CorentinTh/it-tools) | Collection of handy online tools for developers, with great UX. |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more. |
| [dice](https://github.com/DiceDB/dice) | DiceDB is an in-memory real-time database with SQL-based reactivity. It is hyper-optimized for building and scaling truly real-time applications on modern hardware while being a drop-in replacement for Redis. |
| [bitcoin](https://github.com/bitcoin/bitcoin) | Bitcoin Core integration/staging tree |
| [linutil](https://github.com/ChrisTitusTech/linutil) | Chris Titus Tech's Linux Toolbox - Linutil is a distro-agnostic toolbox designed to simplify everyday Linux tasks. |
| [nginx](https://github.com/nginx/nginx) | The official NGINX Open Source repository. |
| [PowerToys](https://github.com/microsoft/PowerToys) | Windows system utilities to maximize productivity |
| [HivisionIDPhotos](https://github.com/Zeyi-Lin/HivisionIDPhotos) | ⚡️HivisionIDPhotos: a lightweight and efficient AI ID photos tools. 一个轻量级的AI证件照制作算法。 |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [midday](https://github.com/midday-ai/midday) | Run your business smarter 🪄 |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is an AI collaborative workspace where you achieve more without losing control of your data. The best open source alternative to Notion. |
| [authentik](https://github.com/goauthentik/authentik) | The authentication glue you need. |
| [Follow](https://github.com/RSSNext/Follow) | 🧡 Next generation information browser. |
| [sherlock](https://github.com/sherlock-project/sherlock) | Hunt down social media accounts by username across social networks |
| [lerobot](https://github.com/huggingface/lerobot) | 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning |
| [ai-toolkit](https://github.com/ostris/ai-toolkit) | Various AI scripts. Mostly Stable Diffusion stuff. |
| [roop](https://github.com/s0md3v/roop) | one-click face swap |
<!-- END OF MONTHLY_TOP10_REPOS -->
