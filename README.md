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
| [novu](https://github.com/novuhq/novu) | 🔥 The open-source notification infrastructure with fully functional embedded notification center 🚀🚀🚀 |
| [autogen](https://github.com/microsoft/autogen) | Enable Next-Gen Large Language Model Applications. Join our Discord: https://discord.gg/pAbnFJrkgZ |
| [dreamgaussian](https://github.com/dreamgaussian/dreamgaussian) | Generative Gaussian Splatting for Efficient 3D Content Creation |
| [appwrite](https://github.com/appwrite/appwrite) | Build like a team of hundreds_ |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [CleanArchitecture](https://github.com/jasontaylordev/CleanArchitecture) | Clean Architecture Solution Template for ASP.NET Core |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [quill](https://github.com/joschan21/quill) | Quill - A Modern SaaS-Platform Built With Next.js 13 |
| [bitcoin](https://github.com/bitcoin/bitcoin) | Bitcoin Core integration/staging tree |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [Qwen](https://github.com/QwenLM/Qwen) | The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. |
| [gitness](https://github.com/harness/gitness) | Gitness is an Open Source developer platform with Source Control management, Continuous Integration and Continuous Delivery. |
| [ColossalAI](https://github.com/hpcaitech/ColossalAI) | Making large AI models cheaper, faster and more accessible |
| [javascript](https://github.com/airbnb/javascript) | JavaScript Style Guide |
| [Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) | Clone a voice in 5 seconds to generate arbitrary speech in real-time |
| [ProPainter](https://github.com/sczhou/ProPainter) | [ICCV 2023] ProPainter: Improving Propagation and Transformer for Video Inpainting |
| [xenminer](https://github.com/jacklevin74/xenminer) |  |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Create Customized Software using Natural Language Idea (through LLM-powered Multi-Agent Collaboration) |
| [openv0](https://github.com/raidendotai/openv0) | AI generated UI components |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [godot](https://github.com/godotengine/godot) | Godot Engine – Multi-platform 2D and 3D game engine |
| [mojo](https://github.com/modularml/mojo) | The Mojo Programming Language |
| [nougat](https://github.com/facebookresearch/nougat) | Implementation of Nougat Neural Optical Understanding for Academic Documents |
| [aidea](https://github.com/mylxsw/aidea) | AIdea 是一款支持 GPT 以及国产大语言模型通义千问、文心一言等，支持 Stable Diffusion 文生图、图生图、 SDXL1.0、超分辨率、图片上色的全能型 APP。 |
| [TTS](https://github.com/coqui-ai/TTS) | 🐸💬 - a deep learning toolkit for Text-to-Speech, battle-tested in research and production |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [gitness](https://github.com/harness/gitness) | Gitness is an Open Source developer platform with Source Control management, Continuous Integration and Continuous Delivery. |
| [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering" |
<!-- END OF MONTHLY_TOP10_REPOS -->
