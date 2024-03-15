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
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [teable](https://github.com/teableio/teable) | ✨ A Super fast, Real-time, Professional, Developer friendly, No code database |
| [Data-Science-Gen-AI-Playlist-2024](https://github.com/krishnaik06/Data-Science-Gen-AI-Playlist-2024) |  |
| [framework](https://github.com/laravel/framework) | The Laravel Framework. |
| [aspnetcore](https://github.com/dotnet/aspnetcore) | ASP.NET Core is a cross-platform .NET framework for building modern cloud-based web applications on Windows, Mac, or Linux. |
| [gleam](https://github.com/gleam-lang/gleam) | ⭐️ A friendly language for building type-safe, scalable systems! |
| [autocomplete](https://github.com/withfig/autocomplete) | IDE-style autocomplete for your existing terminal & shell |
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
