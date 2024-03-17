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
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [LaVague](https://github.com/lavague-ai/LaVague) | Automate automation with Large Action Model framework |
| [suyu](https://github.com/suyu-emu/suyu) | suyu is the continuation of the world's most popular, open-source, Nintendo Switch emulator, yuzu. It is written in C++ with portability in mind, and we actively maintain builds for Windows, Linux and Android. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [oh-my-rime](https://github.com/Mintimate/oh-my-rime) | The Simple Config Template Of Rime By Mintimate. QQ Chat-Group: 703260572 |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | The first real AI developer |
| [ios-diia](https://github.com/diia-open-source/ios-diia) |  |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [data-engineer-handbook](https://github.com/DataEngineer-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
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
