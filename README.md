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
| [protobuf](https://github.com/protocolbuffers/protobuf) | Protocol Buffers - Google's data interchange format |
| [ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web) | A well-designed cross-platform ChatGPT UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT 应用。 |
| [pgx](https://github.com/jackc/pgx) | PostgreSQL driver and toolkit for Go |
| [CVE-2023-44487](https://github.com/bcdannyboy/CVE-2023-44487) | Basic vulnerability scanning to see if web servers may be vulnerable to CVE-2023-44487 |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [leetcode](https://github.com/doocs/leetcode) | 🔥LeetCode solutions in any programming language | 多种编程语言实现 LeetCode、《剑指 Offer（第 2 版）》、《程序员面试金典（第 6 版）》题解 |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [CogVLM](https://github.com/THUDM/CogVLM) | a state-of-the-art-level open visual language model |
| [LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [DocsGPT](https://github.com/arc53/DocsGPT) | GPT-powered chat for documentation, chat with your documents |
| [LLaVA](https://github.com/haotian-liu/LLaVA) | [NeurIPS 2023 Oral] Visual Instruction Tuning: LLaVA (Large Language-and-Vision Assistant) built towards multimodal GPT-4 level capabilities. |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
| [autogen](https://github.com/microsoft/autogen) | Enable Next-Gen Large Language Model Applications. Join our Discord: https://discord.gg/pAbnFJrkgZ |
| [genai-stack](https://github.com/docker/genai-stack) | Langchain + Docker + Neo4j |
| [comprehensive-rust](https://github.com/google/comprehensive-rust) | This is the Rust course used by the Android team at Google. It provides you the material to quickly teach Rust. |
| [promptflow](https://github.com/microsoft/promptflow) | Build high-quality LLM apps - from prototyping, testing to production deployment and monitoring. |
| [twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [bruno](https://github.com/usebruno/bruno) | Opensource IDE For Exploring and Testing Api's (lightweight alternative to postman/insomnia) |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [bun](https://github.com/oven-sh/bun) | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Create Customized Software using Natural Language Idea (through LLM-powered Multi-Agent Collaboration) |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) | OpenAI's Code Interpreter in your terminal, running locally |
| [godot](https://github.com/godotengine/godot) | Godot Engine – Multi-platform 2D and 3D game engine |
| [opentofu](https://github.com/opentofu/opentofu) | OpenTofu lets you declaratively manage your cloud infrastructure. |
| [tldraw](https://github.com/tldraw/tldraw) | a very good whiteboard |
| [mojo](https://github.com/modularml/mojo) | The Mojo Programming Language |
| [appwrite](https://github.com/appwrite/appwrite) | Build like a team of hundreds_ |
| [novu](https://github.com/novuhq/novu) | 🔥 The open-source notification infrastructure with fully functional embedded notification center 🚀🚀🚀 |
<!-- END OF MONTHLY_TOP10_REPOS -->
