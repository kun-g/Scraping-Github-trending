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
| [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [rarbg](https://github.com/2004content/rarbg) | Backup of magnets from RARBG |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to build, manage & run useful autonomous agents quickly and reliably. |
| [go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 用 Vue3 和 Go 搭建的微软 New Bing 演示站点，拥有一致的 UI 体验，支持 ChatGPT 提示词，国内可用。 |
| [box](https://github.com/liu673cn/box) | TVbox开源版（空壳-自行配置） |
| [main](https://github.com/Not-Quite-RARBG/main) | Not Quite RARBG's main website. |
| [CodeTF](https://github.com/salesforce/CodeTF) | CodeTF: One-stop Transformer Library for State-of-the-art Code LLM |
| [Redream](https://github.com/Fictiverse/Redream) | Realtime Diffusion, using Automatic1111 Stable Diffusion API |
| [chainlit](https://github.com/Chainlit/chainlit) | Build Python LLM apps in minutes ⚡️ |
| [StableDiffusion-CheatSheet](https://github.com/SupaGruen/StableDiffusion-CheatSheet) | A list of StableDiffusion styles and some notes for offline use. Pure HTML, CSS and a bit of JS. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ecoute](https://github.com/SevaSk/ecoute) | Ecoute is a live transcription tool that provides real-time transcripts for both the user's microphone input (You) and the user's speakers output (Speaker) in a textbox. It also generates a suggested response using OpenAI's GPT-3.5 for the user to say based on the live transcription of the conversation. |
| [gptlink](https://github.com/gptlink/gptlink) | 10分钟搭建自己可免费商用的ChatGPT环境，搭建简单，包含用户，订单，任务，付费等功能 |
| [DeepFaceLive](https://github.com/iperov/DeepFaceLive) | Real-time face swap for PC streaming or video calls |
| [qlora](https://github.com/artidoro/qlora) | QLoRA: Efficient Finetuning of Quantized LLMs |
| [tinygrad](https://github.com/geohot/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库, 唐宋两朝近一万四千古诗人, 接近5.5万首唐诗加26万宋诗. 两宋时期1564位词人，21050首词。 |
| [pandora](https://github.com/pengzhile/pandora) | 潘多拉，一个让你呼吸顺畅的ChatGPT。Pandora, a ChatGPT that helps you breathe smoothly. |
| [MyMacsAppCrack](https://github.com/QiuChenly/MyMacsAppCrack) | MacBook 自用软件破解（macOS Intel） |
| [tree-of-thoughts](https://github.com/kyegomez/tree-of-thoughts) | Plug in and Play Implementation of Tree of Thoughts: Deliberate Problem Solving with Large Language Models that Elevates Model Reasoning by atleast 70% |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [starcoder](https://github.com/bigcode-project/starcoder) | Home of StarCoder: fine-tuning & inference! |
| [pandora](https://github.com/pengzhile/pandora) | 潘多拉，一个让你呼吸顺畅的ChatGPT。Pandora, a ChatGPT that helps you breathe smoothly. |
| [comprehensive-rust](https://github.com/google/comprehensive-rust) | This is the Rust course used by the Android team at Google. It provides you the material to quickly teach Rust to everyone. |
| [fairseq](https://github.com/facebookresearch/fairseq) | Facebook AI Research Sequence-to-Sequence Toolkit written in Python. |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag & drop UI to build your customized LLM flow using LangchainJS |
| [yuzu](https://github.com/yuzu-emu/yuzu) | Nintendo Switch Emulator |
| [plane](https://github.com/makeplane/plane) | 🔥 🔥 🔥 Open Source JIRA, Linear and Height Alternative. Plane helps you track your issues, epics, and product roadmaps in the simplest way possible. |
| [tinygrad](https://github.com/geohot/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [FlipperAmiibo](https://github.com/Gioman101/FlipperAmiibo) | Made to be used with Flipper just drag the folder into NFC |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》是一本动画图解、能运行、可提问的数据结构与算法入门书，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Zig 等语言。 |
<!-- END OF MONTHLY_TOP10_REPOS -->
