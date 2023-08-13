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
| [candle](https://github.com/huggingface/candle) | Minimalist ML framework for Rust |
| [SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | Multiplayer at the speed of light |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [themes](https://github.com/radix-ui/themes) | Radix Themes is an open-source component library optimized for fast development, easy maintenance, and accessibility. Maintained by @workos. |
| [generative_agents](https://github.com/joonspk-research/generative_agents) | Generative Agents: Interactive Simulacra of Human Behavior |
| [PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book) | 面向网络安全从业者的知识文库🍃 |
| [rift](https://github.com/morph-labs/rift) | Rift: an AI-native language server for your personal AI software engineer |
| [putting-the-you-in-cpu](https://github.com/hackclub/putting-the-you-in-cpu) | A technical explainer by @kognise of how your computer runs programs, from start to finish. |
| [arpchat](https://github.com/kognise/arpchat) | Answering the question nobody asked: what if you wanted to text your friends using only ARP? |
| [remotes](https://github.com/remote-es/remotes) | This is a repository listing companies which offer full-time remote jobs with Spanish contracts |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [azurechatgpt](https://github.com/microsoft/azurechatgpt) | 🤖 Azure ChatGPT: Private & secure ChatGPT for internal enterprise use 💼 |
| [nextui](https://github.com/nextui-org/nextui) | 🚀 Beautiful, fast and modern React UI library. |
| [Qwen-7B](https://github.com/QwenLM/Qwen-7B) | The official repo of Qwen-7B (通义千问-7B) chat & pretrained large language model proposed by Alibaba Cloud. |
| [dioxus](https://github.com/DioxusLabs/dioxus) | Fullstack GUI library for desktop, web, mobile, and more. |
| [audiocraft](https://github.com/facebookresearch/audiocraft) | Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning. |
| [commerce](https://github.com/vercel/commerce) | Next.js Commerce |
| [FastGPT](https://github.com/labring/FastGPT) | FastGPT is a knowledge-based question answering system based on the LLM language model, providing out-of-the-box capabilities for data processing, model invocation, and more. It also allows for complex question answering scenarios through visual workflow orchestration using Flow! |
| [one-api](https://github.com/songquanpeng/one-api) | OpenAI 接口管理 & 分发系统，支持 Azure、Anthropic Claude、Google PaLM 2、智谱 ChatGLM、百度文心一言、讯飞星火认知以及阿里通义千问，可用于二次分发管理 key，仅单可执行文件，已打包好 Docker 镜像，一键部署，开箱即用. OpenAI key management & redistribution system, using a single API for all LLMs, and features an English UI. |
| [web-check](https://github.com/Lissy93/web-check) | 🌐 All-in-one OSINT tool for analysing any website |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [llama](https://github.com/facebookresearch/llama) | Inference code for LLaMA models |
| [devops-exercises](https://github.com/bregman-arie/devops-exercises) | Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | A powerful and modular stable diffusion GUI with a graph/nodes interface. |
| [noodle](https://github.com/ixahmedxi/noodle) | Open Source Education Platform |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [quivr](https://github.com/StanGirard/quivr) | 🧠 Dump all your files and chat with it using your Generative AI Second Brain using LLMs ( GPT 3.5/4, Private, Anthropic, VertexAI ) & Embeddings 🧠 |
| [h2ogpt](https://github.com/h2oai/h2ogpt) | Private Q&A and summarization of documents+images or chat with local GPT, 100% private, Apache 2.0. Supports LLaMa2, llama.cpp, and more. Demo: https://gpt.h2o.ai/ |
| [typescript-book](https://github.com/gibbok/typescript-book) | The Concise TypeScript Book: A Concise Guide to Effective Development in TypeScript. Free and Open Source. |
| [htmx](https://github.com/bigskysoftware/htmx) | </> htmx - high power tools for HTML |
<!-- END OF MONTHLY_TOP10_REPOS -->
