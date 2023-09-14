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
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating |
| [tldraw](https://github.com/tldraw/tldraw) | a very good whiteboard |
| [makepad](https://github.com/makepad/makepad) | Makepad is a creative software development platform for Rust that compiles to wasm/webGL, osx/metal, windows/dx11 linux/opengl |
| [aidea-server](https://github.com/mylxsw/aidea-server) | AIdea 是一款支持 GPT 以及国产大语言模型通义千问、文心一言等，支持 Stable Diffusion 文生图、图生图、 SDXL1.0、超分辨率、图片上色的全能型 APP。 |
| [facechain](https://github.com/modelscope/facechain) | FaceChain is a deep-learning toolchain for generating your Digital-Twin. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [aidea](https://github.com/mylxsw/aidea) | AIdea 是一款支持 GPT 以及国产大语言模型通义千问、文心一言等，支持 Stable Diffusion 文生图、图生图、 SDXL1.0、超分辨率、图片上色的全能型 APP。 |
| [d2l-zh](https://github.com/d2l-ai/d2l-zh) | 《动手学深度学习》：面向中文读者、能运行、可讨论。中英文版被70多个国家的500多所大学用于教学。 |
| [machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) | The code from the Machine Learning Bookcamp book and a free course based on the book |
| [voice-changer](https://github.com/w-okada/voice-changer) | リアルタイムボイスチェンジャー Realtime Voice Changer |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) | OpenAI's Code Interpreter in your terminal, running locally |
| [mojo](https://github.com/modularml/mojo) | The Mojo Programming Language |
| [CasaOS](https://github.com/IceWhaleTech/CasaOS) | CasaOS - A simple, easy-to-use, elegant open-source Personal Cloud system. |
| [bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [DevToys](https://github.com/veler/DevToys) | A Swiss Army knife for developers. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering" |
| [ColossalAI](https://github.com/hpcaitech/ColossalAI) | Making large AI models cheaper, faster and more accessible |
| [jq](https://github.com/jqlang/jq) | Command-line JSON processor |
| [Infinity-For-Reddit](https://github.com/Docile-Alligator/Infinity-For-Reddit) | A Reddit client for Android |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [awesome-english-ebooks](https://github.com/hehonghui/awesome-english-ebooks) | 经济学人(含音频)、纽约客、卫报、连线、大西洋月刊等英语杂志免费下载,支持epub、mobi、pdf格式, 每周更新 |
| [generative_agents](https://github.com/joonspk-research/generative_agents) | Generative Agents: Interactive Simulacra of Human Behavior |
| [hackingtool](https://github.com/Z4nzu/hackingtool) | ALL IN ONE Hacking Tool For Hackers |
| [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering" |
| [DevOpsGPT](https://github.com/kuafuai/DevOpsGPT) | Multi agent system for AI-driven software development. Combine LLM with DevOps tools to convert natural language requirements into working software. Supports any development language and extends the existing code. |
| [DevToys](https://github.com/veler/DevToys) | A Swiss Army knife for developers. |
| [organicmaps](https://github.com/organicmaps/organicmaps) | 🍃 Organic Maps is a free Android & iOS offline maps app for travelers, tourists, hikers, and cyclists. It uses crowd-sourced OpenStreetMap data and is developed with love by MapsWithMe (MapsMe) founders and our community. No ads, no tracking, no data collection, no crapware. Please donate to support the development! |
| [Chinese-LLaMA-Alpaca-2](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2) | 中文LLaMA-2 & Alpaca-2大模型二期项目 + 16K超长上下文模型 (Chinese LLaMA-2 & Alpaca-2 LLMs, including 16K long context models) |
| [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | A list of Free Software network services and web applications which can be hosted on your own servers |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
<!-- END OF MONTHLY_TOP10_REPOS -->
