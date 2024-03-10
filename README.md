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
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [Kingfisher](https://github.com/onevcat/Kingfisher) | A lightweight, pure-Swift library for downloading and caching images from the web. |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [Helldivers-2-Internal-Hack-Dll-Proxy-PoC](https://github.com/emoisback/Helldivers-2-Internal-Hack-Dll-Proxy-PoC) | Proof of Concept Internal Hack Using Dll Proxy for Helldivers 2 |
| [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Implementing a ChatGPT-like LLM from scratch, step by step |
| [saas-starter-kit](https://github.com/boxyhq/saas-starter-kit) | 🔥 Enterprise SaaS Starter Kit - Kickstart your enterprise app development with the Next.js SaaS boilerplate 🚀 |
| [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | Agent framework and applications built upon Qwen1.5, featuring Function Calling, Code Interpreter, RAG, and Chrome extension. |
| [multipleWindow3dScene](https://github.com/bgstaal/multipleWindow3dScene) | A quick example of how one can "synchronize" a 3d scene across multiple windows using three.js and localStorage |
| [maxtext](https://github.com/google/maxtext) | A simple, performant and scalable Jax LLM! |
| [TripoSR](https://github.com/VAST-AI-Research/TripoSR) |  |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) | A launch point for your personal nvim configuration |
| [pingora](https://github.com/cloudflare/pingora) | A library for building fast, reliable and evolvable network services. |
| [windows](https://github.com/dockur/windows) | Windows in a Docker container. |
| [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
| [web-check](https://github.com/Lissy93/web-check) | 🕵️‍♂️ All-in-one OSINT tool for analysing any website |
| [starcoder2](https://github.com/bigcode-project/starcoder2) | Home of StarCoder2! |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [web-check](https://github.com/Lissy93/web-check) | 🕵️‍♂️ All-in-one OSINT tool for analysing any website |
| [my-tv](https://github.com/lizongying/my-tv) | 我的电视 电视直播软件，安装即可使用 |
| [OLMo](https://github.com/allenai/OLMo) | Modeling, training, eval, and inference code for OLMo |
| [maybe](https://github.com/maybe-finance/maybe) | The OS for your personal finances |
| [yuzu](https://github.com/yuzu-emu/yuzu) | Nintendo Switch emulator |
| [sherlock](https://github.com/sherlock-project/sherlock) | 🔎 Hunt down social media accounts by username across social networks |
| [campus-imaotai](https://github.com/oddfar/campus-imaotai) | i茅台app自动预约，每日自动预约，支持docker一键部署（本项目不提供成品，使用的是已淘汰的算法） |
| [plura-production](https://github.com/webprodigies/plura-production) |  |
| [zed](https://github.com/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
<!-- END OF MONTHLY_TOP10_REPOS -->
