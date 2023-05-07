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
| [pandas-ai](https://github.com/gventuri/pandas-ai) | Pandas AI is a Python library that integrates generative artificial intelligence capabilities into Pandas, making dataframes conversational |
| [alpaca-lora](https://github.com/tloen/alpaca-lora) | Instruct-tune LLaMA on consumer hardware |
| [super-gradients](https://github.com/Deci-AI/super-gradients) | Easily train or fine-tune SOTA computer vision models with one open source training library. The home of Yolo-NAS. |
| [Discord-Chatbot-Gpt4Free](https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free) | This is a Python-based Discord Chatbot. This is all free due to the GPT4FREE project |
| [vue-vben-admin](https://github.com/vbenjs/vue-vben-admin) | A modern vue admin. It is based on Vue3, vite and TypeScript. It's fast！ |
| [prompt-engineering-for-developers](https://github.com/datawhalechina/prompt-engineering-for-developers) | 吴恩达《ChatGPT Prompt Engineering for Developers》课程中文版 |
| [Azure-Sentinel](https://github.com/Azure/Azure-Sentinel) | Cloud-native SIEM for intelligent security analytics for your entire enterprise. |
| [v](https://github.com/vlang/v) | Simple, fast, safe, compiled language for developing maintainable software. Compiles itself in <1s with zero library dependencies. Supports automatic C => V translation. https://vlang.io |
| [mojo](https://github.com/modularml/mojo) | The Mojo Programming Language |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
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
| [FastChat](https://github.com/lm-sys/FastChat) | The release repo for "Vicuna: An Open Chatbot Impressing GPT-4" |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective. |
| [ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web) | One-Click to deploy well-designed ChatGPT web UI on Vercel. 一键拥有你自己的 ChatGPT 网页服务。 |
| [wolverine](https://github.com/biobootloader/wolverine) |  |
| [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 中文LLaMA&Alpaca大语言模型+本地CPU/GPU部署 (Chinese LLaMA & Alpaca LLMs) |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | gpt4all: an ecosystem of open-source chatbots trained on a massive collections of clean assistant data including code, stories and dialogue |
| [taxonomy](https://github.com/shadcn/taxonomy) | An open source application built using the new router, server components and everything new in Next.js 13. |
| [langchain](https://github.com/hwchase17/langchain) | ⚡ Building applications with LLMs through composability ⚡ |
| [chroma](https://github.com/chroma-core/chroma) | the AI-native open-source embedding database |
| [text-generation-webui](https://github.com/oobabooga/text-generation-webui) | A gradio web UI for running Large Language Models like LLaMA, llama.cpp, GPT-J, Pythia, OPT, and GALACTICA. |
<!-- END OF MONTHLY_TOP10_REPOS -->
