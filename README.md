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
| [MobileSAM](https://github.com/ChaoningZhang/MobileSAM) | This is the official code for Faster Segment Anything (MobileSAM) project that makes SAM lightweight for mobile applications and beyond! |
| [mpt-30B-inference](https://github.com/abacaj/mpt-30B-inference) | Run inference on MPT-30B using CPU |
| [Block-Pornographic-Replies](https://github.com/slarkvan/Block-Pornographic-Replies) | 屏蔽推特回复下的黄推。Block pornographic replies below the tweet. |
| [open-source-course](https://github.com/WeMakeDevs/open-source-course) |  |
| [PowerShell](https://github.com/PowerShell/PowerShell) | PowerShell for every system! |
| [DragGAN](https://github.com/XingangPan/DragGAN) | Official Code for DragGAN (SIGGRAPH 2023) |
| [folly](https://github.com/facebook/folly) | An open-source C++ library developed and used at Facebook. |
| [Tkinter-Designer](https://github.com/ParthJadhav/Tkinter-Designer) | An easy and fast way to create a Python GUI 🐍 |
| [papers-we-love](https://github.com/papers-we-love/papers-we-love) | Papers from the computer science community to read and discuss. |
| [LLMs-In-China](https://github.com/wgwang/LLMs-In-China) | 中国大模型 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [ai-getting-started](https://github.com/a16z-infra/ai-getting-started) | A Javascript AI getting started stack for weekend projects, including image/text models, vector stores, auth, and deployment configs |
| [svelte](https://github.com/sveltejs/svelte) | Cybernetically enhanced web apps |
| [vllm](https://github.com/vllm-project/vllm) | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [sd-webui-roop](https://github.com/s0md3v/sd-webui-roop) | roop extension for StableDiffusion web-ui |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
| [papers-we-love](https://github.com/papers-we-love/papers-we-love) | Papers from the computer science community to read and discuss. |
| [chatgpt-retrieval](https://github.com/techleadhd/chatgpt-retrieval) |  |
| [InjectLib](https://github.com/QiuChenlyOpenSource/InjectLib) | 基于Ruby编写的命令行注入版本 |
| [kaguya](https://github.com/ykdojo/kaguya) | A ChatGPT plugin that allows you to load and edit your local files in a controlled way, as well as run any Python, JavaScript, and bash script. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to build, manage & run useful autonomous agents quickly and reliably. |
| [OpenChat](https://github.com/openchatai/OpenChat) | LLMs custom-chatbots console ⚡ |
| [gpt4free-ts](https://github.com/xiangsx/gpt4free-ts) | Providing a free OpenAI GPT-4 API ! This is a replication project for the typescript version of xtekky/gpt4free |
| [Chat2DB](https://github.com/alibaba/Chat2DB) | 🔥 🔥 🔥 An intelligent and versatile general-purpose SQL client and reporting tool for databases which integrates ChatGPT capabilities.(智能的通用数据库SQL客户端和报表工具) |
| [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [roop](https://github.com/s0md3v/roop) | one-click deepfake (face swap) |
| [go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 用 Vue3 和 Go 搭建的微软 New Bing 演示站点，拥有一致的 UI 体验，支持 ChatGPT 提示词，国内可用。 |
| [invidious](https://github.com/iv-org/invidious) | Invidious is an alternative front-end to YouTube |
| [ggml](https://github.com/ggerganov/ggml) | Tensor library for machine learning |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
<!-- END OF MONTHLY_TOP10_REPOS -->
