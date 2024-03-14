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
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
| [suyu](https://github.com/suyu-emu/suyu) | suyu, pronounced "sue-you" (wink wink) is the continuation of the world's most popular, open-source, Nintendo Switch emulator, yuzu. It is written in C++ with portability in mind, and we actively maintain builds for Windows, Linux and Android. |
| [gleam](https://github.com/gleam-lang/gleam) | ⭐️ A friendly language for building type-safe, scalable systems! |
| [DeepSeek-VL](https://github.com/deepseek-ai/DeepSeek-VL) | DeepSeek-VL: Towards Real-World Vision-Language Understanding |
| [OpenGFW](https://github.com/apernet/OpenGFW) | OpenGFW is a flexible, easy-to-use, open source implementation of GFW (Great Firewall of China) on Linux |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [chatnio](https://github.com/Deeptrain-Community/chatnio) | 🚀 Next Generation AI One-Stop Internationalization Solution. 🚀 下一代 AI 一站式解决方案，一站式 Chat + 中转 API 站点，支持 OpenAI，Midjourney，Claude，讯飞星火，Stable Diffusion，DALL·E，ChatGLM，通义千问，腾讯混元，360 智脑，百川 AI，火山方舟，新必应，Gemini，Moonshot 等模型，支持对话分享，自定义预设，云端同步，模型市场，支持弹性计费和订阅计划模式，支持图片解析，支持联网搜索，支持模型缓存，丰富美观的后台管理与仪表盘数据统计。 |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [aici](https://github.com/microsoft/aici) | AICI: Prompts as (Wasm) Programs |
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
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
| [campus-imaotai](https://github.com/oddfar/campus-imaotai) | i茅台app自动预约，每日自动预约，支持docker一键部署（本项目不提供成品，使用的是已淘汰的算法） |
| [metavoice-src](https://github.com/metavoiceio/metavoice-src) | Foundational model for human-like, expressive TTS |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [FastUI](https://github.com/pydantic/FastUI) | Build better UIs faster. |
| [pkl](https://github.com/apple/pkl) | A configuration as code language with rich validation and tooling. |
| [sherlock](https://github.com/sherlock-project/sherlock) | 🔎 Hunt down social media accounts by username across social networks |
| [openai-translator](https://github.com/openai-translator/openai-translator) | 基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用 - Browser extension and cross-platform desktop application for translation based on ChatGPT API. |
<!-- END OF MONTHLY_TOP10_REPOS -->
