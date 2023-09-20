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
| [TTS](https://github.com/coqui-ai/TTS) | 🐸💬 - a deep learning toolkit for Text-to-Speech, battle-tested in research and production |
| [Rerender_A_Video](https://github.com/williamyang1991/Rerender_A_Video) | Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation |
| [agents](https://github.com/aiwaves-cn/agents) | An Open-source Framework for Autonomous Language Agents |
| [nuejs](https://github.com/nuejs/nuejs) | Build user interfaces with cleaner code. Alternative to React, Vue, and Svelte |
| [plane](https://github.com/makeplane/plane) | 🔥 🔥 🔥 Open Source JIRA, Linear and Height Alternative. Plane helps you track your issues, epics, and product roadmaps in the simplest way possible. |
| [memos](https://github.com/usememos/memos) | A privacy-first, lightweight note-taking service. Easily capture and share your great thoughts. |
| [NExT-GPT](https://github.com/NExT-GPT/NExT-GPT) | Code and models for NExT-GPT: Any-to-Any Multimodal Large Language Model |
| [90DaysOfCyberSecurity](https://github.com/farhanashrafdev/90DaysOfCyberSecurity) | This repository contains a 90-day cybersecurity study plan, along with resources and materials for learning various cybersecurity concepts and technologies. The plan is organized into daily tasks, covering topics such as Network+, Security+, Linux, Python, Traffic Analysis, Git, ELK, AWS, Azure, and Hacking. The repository also includes a `LEARN.md |
| [soybean-admin](https://github.com/honghuangdc/soybean-admin) | A fresh and elegant admin template, based on Vue3,Vite3,TypeScript,NaiveUI and UnoCSS [一个基于Vue3、Vite3、TypeScript、NaiveUI 和 UnoCSS的清新优雅的中后台模版] |
| [meshery](https://github.com/meshery/meshery) | Meshery, the cloud native manager |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) | OpenAI's Code Interpreter in your terminal, running locally |
| [godot](https://github.com/godotengine/godot) | Godot Engine – Multi-platform 2D and 3D game engine |
| [mojo](https://github.com/modularml/mojo) | The Mojo Programming Language |
| [DiffBIR](https://github.com/XPixelGroup/DiffBIR) |  |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Create Customized Software using Natural Language Idea (through Multi-Agent Collaboration) |
| [aidea](https://github.com/mylxsw/aidea) | AIdea 是一款支持 GPT 以及国产大语言模型通义千问、文心一言等，支持 Stable Diffusion 文生图、图生图、 SDXL1.0、超分辨率、图片上色的全能型 APP。 |
| [rinha-de-compiler](https://github.com/aripiprazole/rinha-de-compiler) | 🥖 | Rinha de compiladores (ou interpretadores kkkk |
| [AnimateDiff](https://github.com/guoyww/AnimateDiff) | Official implementation of AnimateDiff. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [llama-gpt](https://github.com/getumbrel/llama-gpt) | A self-hosted, offline, ChatGPT-like chatbot. Powered by Llama 2. 100% private, with no data leaving your device. New: Code Llama support! |
| [awesome-english-ebooks](https://github.com/hehonghui/awesome-english-ebooks) | 经济学人(含音频)、纽约客、卫报、连线、大西洋月刊等英语杂志免费下载,支持epub、mobi、pdf格式, 每周更新 |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating |
| [manifesto](https://github.com/opentffoundation/manifesto) | The OpenTF Manifesto expresses concern over HashiCorp's switch of the Terraform license from open-source to the Business Source License (BSL) and calls for the tool's return to a truly open-source license. |
| [DevOpsGPT](https://github.com/kuafuai/DevOpsGPT) | Multi agent system for AI-driven software development. Combine LLM with DevOps tools to convert natural language requirements into working software. Supports any development language and extends the existing code. |
| [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering" |
| [hackingtool](https://github.com/Z4nzu/hackingtool) | ALL IN ONE Hacking Tool For Hackers |
| [rinha-de-backend-2023-q3](https://github.com/zanfranceschi/rinha-de-backend-2023-q3) | Rinha de Backend - Edição 2023 Q3 |
<!-- END OF MONTHLY_TOP10_REPOS -->
