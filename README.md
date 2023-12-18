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
| [namada](https://github.com/anoma/namada) | Rust implementation of Namada, a Proof-of-Stake L1 for interchain asset-agnostic privacy |
| [weak-to-strong](https://github.com/openai/weak-to-strong) |  |
| [OutfitAnyone](https://github.com/HumanAIGC/OutfitAnyone) | Outfit Anyone: Ultra-high quality virtual try-on for Any Clothing and Any Person |
| [sing-box](https://github.com/SagerNet/sing-box) | The universal proxy platform |
| [Polaris](https://github.com/vectorisvector/Polaris) |  |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤖 Lobe Chat - an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application. |
| [immich](https://github.com/immich-app/immich) | Self-hosted photo and video backup solution directly from your mobile phone. |
| [threestudio](https://github.com/threestudio-project/threestudio) | A unified framework for 3D content generation. |
| [i2vgen-xl](https://github.com/damo-vilab/i2vgen-xl) | Official repo for VGen: a holistic video generation ecosystem for video generation building on diffusion models |
| [ord](https://github.com/ordinals/ord) | 👁‍🗨 Rare and exotic sats |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Open-source ChatGPT experience for both open and closed source LLMs, embedders, and vector databases. Unlimited documents, messages, and concurrent users with permission management in one app. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤖 Lobe Chat - an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application. |
| [project-based-learning](https://github.com/practical-tutorials/project-based-learning) | Curated list of project-based tutorials |
| [mlx-examples](https://github.com/ml-explore/mlx-examples) | Examples in the MLX framework |
| [superduperdb](https://github.com/SuperDuperDB/superduperdb) | 🔮 SuperDuperDB. Bring AI to your database; integrate, train and manage any AI models and APIs directly with your database and your data. |
| [page-spy-web](https://github.com/HuolalaTech/page-spy-web) | Debug remotely and easily like chrome devtools. |
| [vmprotect-3.5.1](https://github.com/jmpoep/vmprotect-3.5.1) |  |
| [mistral-src](https://github.com/mistralai/mistral-src) | Reference implementation of Mistral AI 7B v0.1 model. |
| [DemoFusion](https://github.com/PRIS-CV/DemoFusion) | Let us democratise high-resolution generation! (arXiv 2023) |
| [GPTs](https://github.com/linexjlin/GPTs) | leaked prompts of GPTs |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [gpt-crawler](https://github.com/BuilderIO/gpt-crawler) | Crawl a site to generate knowledge files to create your own custom GPT from a URL |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤖 Lobe Chat - an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application. |
| [seamless_communication](https://github.com/facebookresearch/seamless_communication) | Foundational Models for State-of-the-Art Speech and Text Translation |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 12 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [tldraw](https://github.com/tldraw/tldraw) | a very good whiteboard |
| [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
| [ollama-webui](https://github.com/ollama-webui/ollama-webui) | ChatGPT-Style Web UI Client for Ollama 🦙 |
<!-- END OF MONTHLY_TOP10_REPOS -->
