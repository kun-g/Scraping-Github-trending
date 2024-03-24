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
| [retina](https://github.com/microsoft/retina) | eBPF distributed networking observability tool for Kubernetes |
| [garnet](https://github.com/microsoft/garnet) | Garnet is a remote cache-store from Microsoft Research that offers strong performance (throughput and latency), scalability, storage, recovery, cluster sharding, key migration, and replication features. Garnet can work with existing Redis clients. |
| [jnv](https://github.com/ynqa/jnv) | interactive JSON filter using jq |
| [transformers](https://github.com/huggingface/transformers) | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. |
| [dev-rewards](https://github.com/fluencelabs/dev-rewards) |  |
| [auto-dev](https://github.com/unit-mesh/auto-dev) | 🧙‍AutoDev: The AI-powered coding wizard with multilingual support 🌐, auto code generation 🏗️, and a helpful bug-slaying assistant 🐞! Customizable prompts 🎨 and a magic Auto Dev/Testing/Document/Agent feature 🧪 included! 🚀 |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用大模型，一键生成短视频 |
| [embedded-app-sdk](https://github.com/discord/embedded-app-sdk) | 🚀 The Discord Embedded App SDK lets you build rich, multiplayer experiences as Activities inside Discord. |
| [rive-renderer](https://github.com/rive-app/rive-renderer) | Downstream repo for Rive renderer |
| [MediaCrawler](https://github.com/lewis-007/MediaCrawler) |  |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫 |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | Open-Sora: Democratizing Efficient Video Production for All |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | The first real AI developer |
| [skyvern](https://github.com/Skyvern-AI/skyvern) | Automate browser-based workflows with LLMs and Computer Vision |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [solana-sniper-bot](https://github.com/fdundjer/solana-sniper-bot) | Solana Sniper Bot - Proof of Concept |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [winterjs](https://github.com/wasmerio/winterjs) | Winter is coming... ❄️ |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [private-gpt](https://github.com/zylon-ai/private-gpt) | Interact with your documents using the power of GPT, 100% privately, no data leaks |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [web-check](https://github.com/Lissy93/web-check) | 🕵️‍♂️ All-in-one OSINT tool for analysing any website |
| [yolov9](https://github.com/WongKinYiu/yolov9) | Implementation of paper - YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 该项目可以让你通过订阅的方式使用Cloudflare WARP+，自动获取流量。This project enables you to use Cloudflare WARP+ through subscription, automatically acquiring traffic. |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) | A launch point for your personal nvim configuration |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
<!-- END OF MONTHLY_TOP10_REPOS -->
