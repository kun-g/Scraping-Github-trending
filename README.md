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
| [heyform](https://github.com/heyform/heyform) | HeyForm is an open-source form builder that allows anyone to create engaging conversational forms for surveys, questionnaires, quizzes, and polls. No coding skills required. |
| [VoiceCraft](https://github.com/jasonppy/VoiceCraft) | Zero-Shot Speech Editing and Text-to-Speech in the Wild |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Create Customized Software using Natural Language Idea (through LLM-powered Multi-Agent Collaboration) |
| [nunu](https://github.com/go-nunu/nunu) | A CLI tool for building Go applications. |
| [openui](https://github.com/wandb/openui) | OpenUI let's you describe UI using your imagination, then see it rendered live. |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [dioxus](https://github.com/DioxusLabs/dioxus) | Fullstack GUI library for web, desktop, mobile, and more. |
| [OpenDevin](https://github.com/OpenDevin/OpenDevin) | 🐚 OpenDevin: Code Less, Make More |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [devika](https://github.com/stitionai/devika) | Devika is an Agentic AI Software Engineer that can understand high-level human instructions, break them down into steps, research relevant information, and write code to achieve the given objective. Devika aims to be a competitive open-source alternative to Devin by Cognition AI. |
| [OpenDevin](https://github.com/OpenDevin/OpenDevin) | 🐚 OpenDevin: Code Less, Make More |
| [01](https://github.com/OpenInterpreter/01) | The open-source language model computer |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [gpt-prompt-engineer](https://github.com/mshumer/gpt-prompt-engineer) |  |
| [garnet](https://github.com/microsoft/garnet) | Garnet is a remote cache-store from Microsoft Research that offers strong performance (throughput and latency), scalability, storage, recovery, cluster sharding, key migration, and replication features. Garnet can work with existing Redis clients. |
| [hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
| [retina](https://github.com/microsoft/retina) | eBPF distributed networking observability tool for Kubernetes |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | locally hosted web application that allows you to perform various operations on PDF files |
| [mojo](https://github.com/modularml/mojo) | The Mojo Programming Language |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | The first real AI developer |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [windows](https://github.com/dockur/windows) | Windows in a Docker container. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
<!-- END OF MONTHLY_TOP10_REPOS -->
