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
| [developer](https://github.com/smol-ai/developer) | with 100k context windows on the way, it's now feasible for every dev to have their own smol developer |
| [quivr](https://github.com/StanGirard/quivr) | Dump all your files and thoughts into your GenerativeAI Second Brain and chat with it |
| [ChatALL](https://github.com/sunner/ChatALL) | Concurrently chat with ChatGPT, Bing Chat, bard, Alpaca, Vincuna, Claude, ChatGLM, MOSS, iFlytek Spark, ERNIE and more, discover the best answers |
| [guidance](https://github.com/microsoft/guidance) | A guidance language for controlling large language models. |
| [dify](https://github.com/langgenius/dify) | One API for plugins and datasets, one interface for prompt engineering and visual operation, all for creating powerful AI applications. |
| [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | Free MLOps course from DataTalks.Club |
| [Bard-API](https://github.com/dsdanielpark/Bard-API) | The python package that returns response of Google Bard through API. |
| [javascript](https://github.com/airbnb/javascript) | JavaScript Style Guide |
| [social-app](https://github.com/bluesky-social/social-app) | The Bluesky Social application for Web, iOS, and Android |
| [FlipperAmiibo](https://github.com/Gioman101/FlipperAmiibo) | Made to be used with Flipper just drag the folder into NFC |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [gpt4free](https://github.com/xtekky/gpt4free) | decentralising the Ai Industry, just some language model api's... |
| [mlc-llm](https://github.com/mlc-ai/mlc-llm) | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices. |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | A GPT-empowered penetration testing tool |
| [qdrant](https://github.com/qdrant/qdrant) | Qdrant - Vector Database for the next generation of AI applications. Also available in the cloud https://cloud.qdrant.io/ |
| [alpaca-lora](https://github.com/tloen/alpaca-lora) | Instruct-tune LLaMA on consumer hardware |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag & drop UI to build your customized LLM flow using LangchainJS |
| [Auto-GPT-Plugins](https://github.com/Significant-Gravitas/Auto-GPT-Plugins) | Plugins for Auto-GPT |
| [qwik](https://github.com/BuilderIO/qwik) | Instant-loading web apps, without effort |
| [ord](https://github.com/casey/ord) | 👁‍🗨 Rare and exotic sats |
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
