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
| [StableStudio](https://github.com/Stability-AI/StableStudio) | Community interface for generative AI |
| [quivr](https://github.com/StanGirard/quivr) | Dump all your files and thoughts into your GenerativeAI Second Brain and chat with it |
| [TOTK-Mods-collection](https://github.com/HolographicWings/TOTK-Mods-collection) | Mod repo for TOTK on Yuzu emulator. |
| [llm-numbers](https://github.com/ray-project/llm-numbers) | Numbers every LLM developer should know |
| [dub](https://github.com/steven-tey/dub) | An open-source link shortener with built-in analytics + free custom domains. |
| [developer](https://github.com/smol-ai/developer) | with 100k context windows on the way, it's now feasible for every dev to have their own smol developer |
| [guidance](https://github.com/microsoft/guidance) | A guidance language for controlling large language models. |
| [project-ideas](https://github.com/hkirat/project-ideas) | Projects to get you started on full stack |
| [JavaGuide](https://github.com/Snailclimb/JavaGuide) | 「Java学习+面试指南」一份涵盖大部分 Java 程序员所需要掌握的核心知识。准备 Java 面试，首选 JavaGuide！ |
| [ImHex](https://github.com/WerWolv/ImHex) | 🔍 A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [privateGPT](https://github.com/imartinez/privateGPT) | Interact privately with your documents using the power of GPT, 100% privately, no data leaks |
| [plugins-quickstart](https://github.com/openai/plugins-quickstart) | Get a ChatGPT plugin up and running in under 5 minutes! |
| [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | Free MLOps course from DataTalks.Club |
| [FlipperAmiibo](https://github.com/Gioman101/FlipperAmiibo) | Made to be used with Flipper just drag the folder into NFC |
| [LocalAI](https://github.com/go-skynet/LocalAI) | 🤖 Self-hosted, community-driven, local OpenAI-compatible API. Drop-in replacement for OpenAI running LLMs on consumer-grade hardware. No GPU required. LocalAI is a RESTful API to run ggml compatible models: llama.cpp, alpaca.cpp, gpt4all.cpp, rwkv.cpp, whisper.cpp, vicuna, koala, gpt4all-j, cerebras and many others! |
| [yuzu](https://github.com/yuzu-emu/yuzu) | Nintendo Switch Emulator |
| [epic-stack](https://github.com/epicweb-dev/epic-stack) | This is a Remix Stack with the foundational things setup and configured for you to hit the ground running on your next EPIC idea. |
| [Bard](https://github.com/acheong08/Bard) | Python SDK/API for reverse engineered Google Bard |
| [yuzu-mainline](https://github.com/yuzu-emu/yuzu-mainline) |  |
| [Digital_Life_Server](https://github.com/zixiiu/Digital_Life_Server) | Yet another voice assistant, but alive. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) | An experimental open-source attempt to make GPT-4 fully autonomous. |
| [AgentGPT](https://github.com/reworkd/AgentGPT) | 🤖 Assemble, configure, and deploy autonomous AI Agents in your browser. |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective. |
| [wolverine](https://github.com/biobootloader/wolverine) |  |
| [Open-Assistant](https://github.com/LAION-AI/Open-Assistant) | OpenAssistant is a chat-based assistant that understands tasks, can interact with third-party systems, and retrieve information dynamically to do so. |
| [babyagi](https://github.com/yoheinakajima/babyagi) |  |
| [taxonomy](https://github.com/shadcn/taxonomy) | An open source application built using the new router, server components and everything new in Next.js 13. |
| [so-vits-svc-fork](https://github.com/voicepaw/so-vits-svc-fork) | so-vits-svc fork with realtime support, improved interface and more features. |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [langchain-ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM) | langchain-ChatGLM, local knowledge based ChatGLM with langchain ｜ 基于本地知识库的 ChatGLM 问答 |
<!-- END OF MONTHLY_TOP10_REPOS -->
