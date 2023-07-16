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
| [BlackLotus](https://github.com/ldpreload/BlackLotus) | BlackLotus UEFI Windows Bootkit |
| [npc_gzip](https://github.com/bazingagin/npc_gzip) |  |
| [annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 🧑‍🏫 60 Implementations/tutorials of deep learning papers with side-by-side notes 📝; including transformers (original, xl, switch, feedback, vit, ...), optimizers (adam, adabelief, sophia, ...), gans(cyclegan, stylegan2, ...), 🎮 reinforcement learning (ppo, dqn), capsnet, distillation, ... 🧠 |
| [haystack](https://github.com/deepset-ai/haystack) | 🔍 Haystack is an open source NLP framework to interact with your data using Transformer models and LLMs (GPT-4, Falcon and alike). Haystack offers production-ready tools to quickly build complex question answering, semantic search, text generation applications, and more. |
| [virgo](https://github.com/system76/virgo) | System76 Virgo Laptop Project |
| [mux](https://github.com/gorilla/mux) | Package gorilla/mux is a powerful HTTP router and URL matcher for building Go web servers with 🦍 |
| [wandb](https://github.com/wandb/wandb) | 🔥 A tool for visualizing and tracking your machine learning experiments. This repo contains the CLI and Python API. |
| [Charts](https://github.com/danielgindi/Charts) | Beautiful charts for iOS/tvOS/OSX! The Apple side of the crossplatform MPAndroidChart. |
| [vanmoof-encryption-key-exporter](https://github.com/grossartig/vanmoof-encryption-key-exporter) | Export all bike details (such as encryption key) of your VanMoof bikes. |
| [Book1_Python-For-Beginners](https://github.com/Visualize-ML/Book1_Python-For-Beginners) | Book_1_《编程不难》 | 鸢尾花书：从加减乘除到机器学习；开始上传PDF草稿、Jupyter笔记。文件还会经过至少两轮修改，改动会很大，大家注意下载最新版本。请多提意见，谢谢 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Meta Programming Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [quivr](https://github.com/StanGirard/quivr) | 🧠 Dump all your files and chat with it using your Generative AI Second Brain using LLMs ( GPT 3.5/4, Private, Anthropic, VertexAI ) & Embeddings 🧠 |
| [danswer](https://github.com/danswer-ai/danswer) | Ask Questions in natural language and get Answers backed by private sources. Connects to tools like Slack, GitHub, Confluence, etc. |
| [igl](https://github.com/facebook/igl) | Intermediate Graphics Library (IGL) is a cross-platform library that commands the GPU. It provides a single low-level cross-platform interface on top of various graphics APIs (e.g. OpenGL, Metal and Vulkan). |
| [noodle](https://github.com/ixahmedxi/noodle) | Open Source Education Platform |
| [memos](https://github.com/usememos/memos) | A privacy-first, lightweight note-taking service. Easily capture and share your great thoughts. |
| [htmx](https://github.com/bigskysoftware/htmx) | </> htmx - high power tools for HTML |
| [typescript-book](https://github.com/gibbok/typescript-book) | The Concise TypeScript Book: A Concise Guide to Effective Development in TypeScript. Free and Open Source. |
| [InternLM](https://github.com/InternLM/InternLM) | InternLM has open-sourced a 7 billion parameter base model, a chat model tailored for practical scenarios and the training system. |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | A powerful and modular stable diffusion GUI with a graph/nodes interface. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [gpt-engineer](https://github.com/AntonOsika/gpt-engineer) | Specify what you want it to build, the AI asks for clarification, and then builds it. |
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | Data-Centric FinGPT. Open-source for open finance! Revolutionize 🔥 We'll soon release the trained model. |
| [quivr](https://github.com/StanGirard/quivr) | 🧠 Dump all your files and chat with it using your Generative AI Second Brain using LLMs ( GPT 3.5/4, Private, Anthropic, VertexAI ) & Embeddings 🧠 |
| [tinygrad](https://github.com/tinygrad/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [ali-dbhub](https://github.com/alibaba/ali-dbhub) | 🔥 🔥 🔥 An intelligent and versatile general-purpose SQL client and reporting tool for databases which integrates ChatGPT capabilities.(智能的通用数据库SQL客户端和报表工具) |
| [platforms](https://github.com/vercel/platforms) | A full-stack Next.js app with multi-tenancy and custom domain support. Built with Next.js App Router and the Vercel Domains API. |
| [h2ogpt](https://github.com/h2oai/h2ogpt) | Private Q&A and summarization of documents+images or chat with local GPT, 100% private, no data leaks, Apache 2.0. Demo: https://gpt.h2o.ai/ |
| [AFFiNE](https://github.com/toeverything/AFFiNE) | There can be more than Notion and Miro. AFFiNE is a next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, open-source, customizable and ready to use. |
| [CodeEdit](https://github.com/CodeEditApp/CodeEdit) | CodeEdit App for macOS – Elevate your code editing experience. Open source, free forever. |
| [svelte](https://github.com/sveltejs/svelte) | Cybernetically enhanced web apps |
<!-- END OF MONTHLY_TOP10_REPOS -->
