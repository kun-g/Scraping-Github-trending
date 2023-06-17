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
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | Data-Centric FinGPT. Open-source for open finance! Revolutionize 🔥 We'll soon release the trained model. |
| [Chat2DB](https://github.com/alibaba/Chat2DB) | 🔥 🔥 🔥 An intelligent and versatile general-purpose SQL client and reporting tool for databases which integrates ChatGPT capabilities.(智能的通用数据库SQL客户端和报表工具) |
| [openai-cookbook](https://github.com/openai/openai-cookbook) | Examples and guides for using the OpenAI API |
| [machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Code for Machine Learning for Algorithmic Trading, 2nd edition. |
| [ijepa](https://github.com/facebookresearch/ijepa) | Official codebase for I-JEPA, the Image-based Joint-Embedding Predictive Architecture. First outlined in the CVPR paper, "Self-supervised learning from images with a joint-embedding predictive architecture." |
| [LongMem](https://github.com/Victorwz/LongMem) |  |
| [langchain](https://github.com/hwchase17/langchain) | ⚡ Building applications with LLMs through composability ⚡ |
| [ChatALL](https://github.com/sunner/ChatALL) | Concurrently chat with ChatGPT, Bing Chat, Bard, Alpaca, Vicuna, Claude, ChatGLM, MOSS, 讯飞星火, 文心一言 and more, discover the best answers |
| [LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning) | Fine-tuning LLaMA with PEFT (PT+SFT+RLHF with QLoRA) |
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
