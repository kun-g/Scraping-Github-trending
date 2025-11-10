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
| [usestrix/strix](https://github.com/usestrix/strix) | ✨ Open-source AI hackers for your apps 👨🏻‍💻 |
| [umami-software/umami](https://github.com/umami-software/umami) | Umami is a modern, privacy-focused alternative to Google Analytics. |
| [thinking-machines-lab/tinker-cookbook](https://github.com/thinking-machines-lab/tinker-cookbook) | Post-training with Tinker |
| [mui/material-ui](https://github.com/mui/material-ui) | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| [google/adk-go](https://github.com/google/adk-go) | An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. |
| [axios/axios](https://github.com/axios/axios) | Promise based HTTP client for the browser and node.js |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Open-source platform to build and deploy AI agent workflows. |
| [airweave-ai/airweave](https://github.com/airweave-ai/airweave) | Context retrieval for AI agents across apps and databases |
| [HyDE-Project/HyDE](https://github.com/HyDE-Project/HyDE) | HyDE, your Development Environment 🖥️💻 |
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Stable Diffusion web UI |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
| [usestrix/strix](https://github.com/usestrix/strix) | ✨ Open-source AI hackers for your apps 👨🏻‍💻 |
| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | Automate browser based workflows with AI |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [nocobase/nocobase](https://github.com/nocobase/nocobase) | NocoBase is the most extensible AI-powered no-code/low-code platform for building business applications and enterprise solutions. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🤖 The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI, running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference |
| [GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm) | Nano vLLM |
| [sst/opentui](https://github.com/sst/opentui) | OpenTUI is a library for building terminal user interfaces (TUIs) |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [lima-vm/lima](https://github.com/lima-vm/lima) | Linux virtual machines, with a focus on running containers |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Generate audiobooks from e-books, voice cloning & 1107+ languages! |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
| [minio/minio](https://github.com/minio/minio) | MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. |
| [servo/servo](https://github.com/servo/servo) | Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications. |
<!-- END OF MONTHLY_TOP10_REPOS -->
