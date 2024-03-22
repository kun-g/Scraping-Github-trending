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
| [garnet](https://github.com/microsoft/garnet) | Garnet is a remote cache-store from Microsoft Research that offers strong performance (throughput and latency), scalability, storage, recovery, cluster sharding, key migration, and replication features. Garnet can work with existing Redis clients. |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | Open-Sora: Democratizing Efficient Video Production for All |
| [ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | 🔥 官方推荐 🔥 RuoYi-Vue 全新 Pro 版本，优化重构所有功能。基于 Spring Boot + MyBatis Plus + Vue & Element 实现的后台管理系统 + 微信小程序，支持 RBAC 动态权限、数据权限、SaaS 多租户、Flowable 工作流、三方登录、支付、短信、商城、CRM、ERP 等功能。你的 ⭐️ Star ⭐️，是作者生发的动力！ |
| [supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
| [jnv](https://github.com/ynqa/jnv) | interactive JSON filter using jq |
| [retina](https://github.com/microsoft/retina) | eBPF distributed networking observability tool for Kubernetes |
| [lynis](https://github.com/CISOfy/lynis) | Lynis - Security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening. Agentless, and installation optional. |
| [ColossalAI](https://github.com/hpcaitech/ColossalAI) | Making large AI models cheaper, faster and more accessible |
| [smartcomponents](https://github.com/dotnet-smartcomponents/smartcomponents) | Experimental, end-to-end AI features for .NET apps |
| [vmail](https://github.com/yesmore/vmail) | Open source temporary email tool. 开源临时邮箱工具 👉 vmail.dev |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [gleam](https://github.com/gleam-lang/gleam) | ⭐️ A friendly language for building type-safe, scalable systems! |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [rolldown](https://github.com/rolldown/rolldown) | Fast Rust bundler for JavaScript with Rollup-compatible API. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
| [OpenGFW](https://github.com/apernet/OpenGFW) | OpenGFW is a flexible, easy-to-use, open source implementation of GFW (Great Firewall of China) on Linux |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [daytona](https://github.com/daytonaio/daytona) | The Open Source Dev Environment Manager. |
| [bruno](https://github.com/usebruno/bruno) | Opensource IDE For Exploring and Testing Api's (lightweight alternative to postman/insomnia) |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | The first real AI developer |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [web-check](https://github.com/Lissy93/web-check) | 🕵️‍♂️ All-in-one OSINT tool for analysing any website |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [uv](https://github.com/astral-sh/uv) | An extremely fast Python package installer and resolver, written in Rust. |
| [gptscript](https://github.com/gptscript-ai/gptscript) | Natural Language Programming |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 2, Mistral, Gemma, and other large language models. |
| [sherlock](https://github.com/sherlock-project/sherlock) | 🔎 Hunt down social media accounts by username across social networks |
<!-- END OF MONTHLY_TOP10_REPOS -->
