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
| [noodle](https://github.com/ixahmedxi/noodle) | Open Source Education Platform |
| [typescript-book](https://github.com/gibbok/typescript-book) | The Concise TypeScript Book: A Concise Guide to Effective Development in TypeScript. Free and Open Source. |
| [Price-Tracking-Web-Scraper](https://github.com/techwithtim/Price-Tracking-Web-Scraper) | An automated price tracker that uses bright data, playwright, react and flask. |
| [h2ogpt](https://github.com/h2oai/h2ogpt) | Join us at H2O.ai to make the world's best open-source GPT with document and image Q&A, 100% private chat, no data leaks, Apache 2.0 https://arxiv.org/pdf/2306.08161.pdf Live Demo: https://gpt.h2o.ai/ |
| [platforms](https://github.com/vercel/platforms) | A full-stack Next.js app with multi-tenancy and custom domain support. Built with Next.js App Router and the Vercel Domains API. |
| [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) | The official GitHub page for the survey paper "A Survey of Large Language Models". |
| [pilotord-kit-onboarding](https://github.com/bacen/pilotord-kit-onboarding) | Documentação e arquivos de configuração para participação no Piloto do Real Digital |
| [gpt-migrate](https://github.com/0xpayne/gpt-migrate) | Easily migrate your codebase from one framework or language to another. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | The Multi-Agent Meta Programming Framework: Given one line Requirement, return PRD, Design, Tasks, Repo | 多智能体元编程框架：给定老板需求，输出产品文档、架构设计、任务列表、代码 |
| [unilm](https://github.com/microsoft/unilm) | Large-scale Self-supervised Pre-training Across Tasks, Languages, and Modalities |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [ai-getting-started](https://github.com/a16z-infra/ai-getting-started) | A Javascript AI getting started stack for weekend projects, including image/text models, vector stores, auth, and deployment configs |
| [svelte](https://github.com/sveltejs/svelte) | Cybernetically enhanced web apps |
| [vllm](https://github.com/vllm-project/vllm) | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [sd-webui-roop](https://github.com/s0md3v/sd-webui-roop) | roop extension for StableDiffusion web-ui |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
| [papers-we-love](https://github.com/papers-we-love/papers-we-love) | Papers from the computer science community to read and discuss. |
| [chatgpt-retrieval](https://github.com/techleadhd/chatgpt-retrieval) |  |
| [InjectLib](https://github.com/QiuChenlyOpenSource/InjectLib) | 基于Ruby编写的命令行注入版本 |
| [kaguya](https://github.com/ykdojo/kaguya) | A ChatGPT plugin that allows you to load and edit your local files in a controlled way, as well as run any Python, JavaScript, and bash script. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to build, manage & run useful autonomous agents quickly and reliably. |
| [OpenChat](https://github.com/openchatai/OpenChat) | LLMs custom-chatbots console ⚡ |
| [gpt4free-ts](https://github.com/xiangsx/gpt4free-ts) | Providing a free OpenAI GPT-4 API ! This is a replication project for the typescript version of xtekky/gpt4free |
| [Chat2DB](https://github.com/alibaba/Chat2DB) | 🔥 🔥 🔥 An intelligent and versatile general-purpose SQL client and reporting tool for databases which integrates ChatGPT capabilities.(智能的通用数据库SQL客户端和报表工具) |
| [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [roop](https://github.com/s0md3v/roop) | one-click deepfake (face swap) |
| [go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 用 Vue3 和 Go 搭建的微软 New Bing 演示站点，拥有一致的 UI 体验，支持 ChatGPT 提示词，国内可用。 |
| [invidious](https://github.com/iv-org/invidious) | Invidious is an alternative front-end to YouTube |
| [ggml](https://github.com/ggerganov/ggml) | Tensor library for machine learning |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
<!-- END OF MONTHLY_TOP10_REPOS -->
