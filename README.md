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
| [gpt-engineer](https://github.com/AntonOsika/gpt-engineer) | Specify what you want it to build, the AI asks for clarification, and then builds it. |
| [FlagAI](https://github.com/FlagAI-Open/FlagAI) | FlagAI (Fast LArge-scale General AI models) is a fast, easy-to-use and extensible toolkit for large-scale model. |
| [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
| [intel-one-mono](https://github.com/intel/intel-one-mono) | Intel One Mono font repository |
| [ChatGPT-Midjourney](https://github.com/Licoy/ChatGPT-Midjourney) | 🎨 一键拥有你自己的 ChatGPT+Midjourney 网页服务 | Own your own ChatGPT+Midjourney web service with one click |
| [Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | A GPT-4 AI Tutor Prompt for customizable personalized learning experiences. |
| [openobserve](https://github.com/openobserve/openobserve) | 🚀 10x easier, 🚀 140x lower storage cost, 🚀 high performance, 🚀 petabyte scale - Elasticsearch/Splunk/Datadog alternative for 🚀 (logs, metrics, traces). |
| [unleashed-firmware](https://github.com/DarkFlippers/unleashed-firmware) | Flipper Zero Unleashed Firmware |
| [conference](https://github.com/gopherchina/conference) |  |
| [audiocraft](https://github.com/facebookresearch/audiocraft) | Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to build, manage & run useful autonomous agents quickly and reliably. |
| [OpenChat](https://github.com/openchatai/OpenChat) | LLMs custom-chatbots console ⚡ |
| [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [rarbg](https://github.com/2004content/rarbg) | Backup of magnets from RARBG |
| [go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 用 Vue3 和 Go 搭建的微软 New Bing 演示站点，拥有一致的 UI 体验，支持 ChatGPT 提示词，国内可用。 |
| [weekly](https://github.com/ruanyf/weekly) | 科技爱好者周刊，每周五发布 |
| [ggml](https://github.com/ggerganov/ggml) | Tensor library for machine learning |
| [MyMacsAppCrack](https://github.com/QiuChenlyOpenSource/MyMacsAppCrack) | MacBook 自用软件破解（macOS Intel） |
| [mlc-llm](https://github.com/mlc-ai/mlc-llm) | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices. |
| [lit-parrot](https://github.com/Lightning-AI/lit-parrot) | Implementation of the StableLM/Pythia/INCITE language models based on nanoGPT. Supports flash attention, LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [privateGPT](https://github.com/imartinez/privateGPT) | Interact privately with your documents using the power of GPT, 100% privately, no data leaks |
| [comprehensive-rust](https://github.com/google/comprehensive-rust) | This is the Rust course used by the Android team at Google. It provides you the material to quickly teach Rust to everyone. |
| [pandora](https://github.com/pengzhile/pandora) | 潘多拉，一个让你呼吸顺畅的ChatGPT。Pandora, a ChatGPT that helps you breathe smoothly. |
| [plane](https://github.com/makeplane/plane) | 🔥 🔥 🔥 Open Source JIRA, Linear and Height Alternative. Plane helps you track your issues, epics, and product roadmaps in the simplest way possible. |
| [fairseq](https://github.com/facebookresearch/fairseq) | Facebook AI Research Sequence-to-Sequence Toolkit written in Python. |
| [tinygrad](https://github.com/geohot/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag & drop UI to build your customized LLM flow using LangchainJS |
| [yuzu](https://github.com/yuzu-emu/yuzu) | Nintendo Switch Emulator |
| [LocalAI](https://github.com/go-skynet/LocalAI) | 🤖 Self-hosted, community-driven, local OpenAI-compatible API. Drop-in replacement for OpenAI running LLMs on consumer-grade hardware. Free Open Source OpenAI alternative. No GPU required. LocalAI is an API to run ggml compatible models: llama, gpt4all, rwkv, whisper, vicuna, koala, gpt4all-j, cerebras, falcon, dolly, starcoder, and many other |
| [DeepFaceLive](https://github.com/iperov/DeepFaceLive) | Real-time face swap for PC streaming or video calls |
<!-- END OF MONTHLY_TOP10_REPOS -->
