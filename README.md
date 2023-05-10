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
| [shap-e](https://github.com/openai/shap-e) | Generate 3D objects conditioned on text or images |
| [open-chat-video-editor](https://github.com/SCUTlihaoyu/open-chat-video-editor) | Open source short video automatic generation tool |
| [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | SoftVC VITS Singing Voice Conversion |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》是一本动画图解、能运行、可提问的数据结构与算法入门书，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Zig 等语言。 |
| [extension](https://github.com/unisat-wallet/extension) | The first open-source browser extension wallet for Bitcoin NFTs |
| [Personalize-SAM](https://github.com/ZrrSkywalker/Personalize-SAM) | Personalize Segment Anything Model (SAM) with 1 shot in 10 seconds |
| [atuin](https://github.com/ellie/atuin) | 🐢 Magical shell history |
| [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 中文LLaMA&Alpaca大语言模型+本地CPU/GPU部署 (Chinese LLaMA & Alpaca LLMs) |
| [1Panel](https://github.com/1Panel-dev/1Panel) | 现代化、开源的 Linux 服务器运维管理面板。 |
| [gpt4free-ts](https://github.com/xiangsx/gpt4free-ts) | This is a replication project for the typescript version of xtekky/gpt4free |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [AudioGPT](https://github.com/AIGC-Audio/AudioGPT) | AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head |
| [gpt4free](https://github.com/xtekky/gpt4free) | decentralising the Ai Industry, just some language model api's... |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [IF](https://github.com/deep-floyd/IF) |  |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag & drop UI to build your customized LLM flow using LangchainJS |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | A GPT-empowered penetration testing tool |
| [chatgpt-clone](https://github.com/xtekky/chatgpt-clone) | ChatGPT interface with better UI |
| [cal.com](https://github.com/calcom/cal.com) | Scheduling infrastructure for absolutely everyone. |
| [atproto](https://github.com/bluesky-social/atproto) | Social networking technology created by Bluesky |
| [NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) | An experimental open-source attempt to make GPT-4 fully autonomous. |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective. |
| [babyagi](https://github.com/yoheinakajima/babyagi) |  |
| [wolverine](https://github.com/biobootloader/wolverine) |  |
| [taxonomy](https://github.com/shadcn/taxonomy) | An open source application built using the new router, server components and everything new in Next.js 13. |
| [langchain-ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM) | langchain-ChatGLM, local knowledge based ChatGLM with langchain ｜ 基于本地知识的 ChatGLM 问答 |
| [segment-anything](https://github.com/facebookresearch/segment-anything) | The repository provides code for running inference with the SegmentAnything Model (SAM), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. |
| [Open-Assistant](https://github.com/LAION-AI/Open-Assistant) | OpenAssistant is a chat-based assistant that understands tasks, can interact with third-party systems, and retrieve information dynamically to do so. |
| [ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web) | One-Click to deploy well-designed ChatGPT web UI on Vercel. 一键拥有你自己的 ChatGPT 网页服务。 |
| [langchain](https://github.com/hwchase17/langchain) | ⚡ Building applications with LLMs through composability ⚡ |
<!-- END OF MONTHLY_TOP10_REPOS -->
