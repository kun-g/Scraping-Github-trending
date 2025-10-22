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
| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |
| [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | A fancy self-hosted monitoring tool |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Generate audiobooks from e-books, voice cloning & 1107+ languages! |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [sharkdp/bat](https://github.com/sharkdp/bat) | A cat(1) clone with wings. |
| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | Automate browser-based workflows with LLMs and Computer Vision |
| [oceanbase/miniob](https://github.com/oceanbase/miniob) | MiniOB is a compact database that assists developers in understanding the fundamental workings of a database. |
| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection. Support embedded systems, Android, iOS, HarmonyOS, Raspberry Pi, RISC-V, x86_64 servers, websocket server/client, support 12 programming languages |
| [servo/servo](https://github.com/servo/servo) | Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | CLI tool for configuring and monitoring Claude Code |
| [volcengine/MineContext](https://github.com/volcengine/MineContext) | MineContext is your proactive context-aware AI partner（Context-Engineering+ChatGPT Pulse） |
| [karpathy/micrograd](https://github.com/karpathy/micrograd) | A tiny scalar-valued autograd engine and a neural net library on top of it with PyTorch-like API |
| [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | Microsoft PowerToys is a collection of utilities that help you customize Windows and streamline everyday tasks |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [tile-ai/tilelang](https://github.com/tile-ai/tilelang) | Domain-specific language designed to streamline the development of high-performance GPU/CPU/Accelerators kernels |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [TibixDev/winboat](https://github.com/TibixDev/winboat) | Run Windows apps on 🐧 Linux with ✨ seamless integration |
| [evershopcommerce/evershop](https://github.com/evershopcommerce/evershop) | 🛍️ Typescript E-commerce Platform |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [audacity/audacity](https://github.com/audacity/audacity) | Audio Editor |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
<!-- END OF MONTHLY_TOP10_REPOS -->
