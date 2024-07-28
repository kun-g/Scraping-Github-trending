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
| [awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
| [lean4](https://github.com/leanprover/lean4) | Lean 4 programming language and theorem prover |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [folly](https://github.com/facebook/folly) | An open-source C++ library developed and used at Facebook. |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [llama3](https://github.com/meta-llama/llama3) | The official Meta Llama 3 GitHub site |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 3.1, Mistral, Gemma 2, and other large language models. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Bedrock / Azure / Mistral / Perplexity ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application. |
| [spdlog](https://github.com/gabime/spdlog) | Fast C++ logging library. |
| [bulma](https://github.com/jgthms/bulma) | Modern CSS framework based on Flexbox |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mem0](https://github.com/mem0ai/mem0) | The memory layer for Personalized AI |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [open-gpu-kernel-modules](https://github.com/NVIDIA/open-gpu-kernel-modules) | NVIDIA Linux open GPU kernel module source |
| [awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
| [MinerU](https://github.com/opendatalab/MinerU) | A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。 |
| [composio](https://github.com/ComposioHQ/composio) | Composio equips agents with well-crafted tools empowering them to tackle complex tasks |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
| [javascript](https://github.com/airbnb/javascript) | JavaScript Style Guide |
| [hoppscotch](https://github.com/hoppscotch/hoppscotch) | Open source API development ecosystem - https://hoppscotch.io (open-source alternative to Postman, Insomnia) |
| [unleashed-firmware](https://github.com/DarkFlippers/unleashed-firmware) | Flipper Zero Unleashed Firmware |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ImHex](https://github.com/WerWolv/ImHex) | 🔍 A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [gs-quant](https://github.com/goldmansachs/gs-quant) | Python toolkit for quantitative finance |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 30 days of Python programming challenge is a step-by-step guide to learn the Python programming language in 30 days. This challenge may take more than100 days, follow your own pace. These videos may help too: https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Brand new TTS solution |
| [mindsdb](https://github.com/mindsdb/mindsdb) | The platform for building AI from enterprise data |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [books](https://github.com/free-educa/books) | o armazém de livros |
| [everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | 人人都能用英语 |
<!-- END OF MONTHLY_TOP10_REPOS -->
