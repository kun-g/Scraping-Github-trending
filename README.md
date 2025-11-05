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
| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
| [sst/opentui](https://github.com/sst/opentui) | OpenTUI is a library for building terminal user interfaces (TUIs) |
| [GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm) | Nano vLLM |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🤖 The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI, running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference |
| [1Panel-dev/MaxKB](https://github.com/1Panel-dev/MaxKB) | 🔥 MaxKB is an open-source platform for building enterprise-grade agents. MaxKB 是强大易用的开源企业级智能体平台。 |
| [imthenachoman/How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server) | An evolving how-to guide for securing a Linux server. |
| [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | A simple, lightweight PowerShell script to remove pre-installed apps, disable telemetry, as well as perform various other changes to customize, declutter and improve your Windows experience. Win11Debloat works for both Windows 10 and Windows 11. |
| [DearVa/Everywhere](https://github.com/DearVa/Everywhere) | A context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools. |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. 🔔 Official updates only via twitter @Martin993886460 (Beware of fake account) |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) | API, CLI, and Web App for analyzing and finding a person's profile in 1000 social media \ websites |
| [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 24 Lessons, 12 Weeks, Get Started as a Web Developer |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |
| [get-convex/chef](https://github.com/get-convex/chef) | The only AI app builder that knows backend |
| [longbridge/gpui-component](https://github.com/longbridge/gpui-component) | Rust GUI components for building fantastic cross-platform desktop application by using GPUI. |
| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |
| [cjpais/Handy](https://github.com/cjpais/Handy) | A free, open source, and extensible speech-to-text application that works completely offline. |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |
| [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | Stremio - Freedom to Stream |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Generate audiobooks from e-books, voice cloning & 1107+ languages! |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [evershopcommerce/evershop](https://github.com/evershopcommerce/evershop) | 🛍️ Typescript E-commerce Platform |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
<!-- END OF MONTHLY_TOP10_REPOS -->
