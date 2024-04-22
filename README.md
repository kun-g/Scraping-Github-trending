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
| [llama3](https://github.com/meta-llama/llama3) | The official Meta Llama 3 GitHub site |
| [PurpleLlama](https://github.com/meta-llama/PurpleLlama) | Set of tools to assess and improve LLM security. |
| [codellama](https://github.com/meta-llama/codellama) | Inference code for CodeLlama models |
| [puter](https://github.com/HeyPuter/puter) | 🌐 The Internet OS! Free, Open-Source, and Self-Hostable. |
| [chess](https://github.com/code100x/chess) | A multiplayer chess platform |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 3, Mistral, Gemma, and other large language models. |
| [LocalAI](https://github.com/mudler/LocalAI) | 🤖 The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. It allows to generate Text, Audio, Video, Images. Also with voice cloning capabilities. |
| [center-randomize](https://github.com/moest-np/center-randomize) | Script is to assign exam centers to students |
| [zig](https://github.com/ziglang/zig) | General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [MaxKB](https://github.com/1Panel-dev/MaxKB) | 💬 基于 LLM 大语言模型的知识库问答系统。开箱即用，支持快速嵌入到第三方业务系统，1Panel 官方出品。 |
| [MiniGemini](https://github.com/dvlab-research/MiniGemini) | Official implementation for Mini-Gemini |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [aiXcoder-7B](https://github.com/aixcoder-plugin/aiXcoder-7B) | official repository of aiXcoder-7B Code Large Language Model |
| [zed](https://github.com/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [torchtune](https://github.com/pytorch/torchtune) | A Native-PyTorch Library for LLM Fine-tuning |
| [social-app](https://github.com/bluesky-social/social-app) | The Bluesky Social application for Web, iOS, and Android |
| [ssr-benchmark](https://github.com/eknkc/ssr-benchmark) | Benchmarking JS web framework SSR performance |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [devika](https://github.com/stitionai/devika) | Devika is an Agentic AI Software Engineer that can understand high-level human instructions, break them down into steps, research relevant information, and write code to achieve the given objective. Devika aims to be a competitive open-source alternative to Devin by Cognition AI. |
| [OpenDevin](https://github.com/OpenDevin/OpenDevin) | 🐚 OpenDevin: Code Less, Make More |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [mojo](https://github.com/modularml/mojo) | The Mojo Programming Language |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
| [01](https://github.com/OpenInterpreter/01) | The open-source language model computer |
| [solana-trading-bot](https://github.com/warp-id/solana-trading-bot) | Solana Trading Bot - Beta |
| [hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
<!-- END OF MONTHLY_TOP10_REPOS -->
