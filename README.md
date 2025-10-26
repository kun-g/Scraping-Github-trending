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
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) | Standard Open Arm 100 |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
| [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark) | Blind&Invisible Watermark ，图片盲水印，提取水印无须原图！ |
| [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | A community-supported supercharged document management system: scan, index and archive all your documents |
| [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr) | Primary Git Repository for the Zephyr Project. Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures. |
| [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) | Open source API development ecosystem -https://hoppscotch.io(open-source alternative to Postman, Insomnia) |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud) | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, K8s, AI inference, and IAM services. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | A feature-rich command-line audio/video downloader |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |
| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Generate audiobooks from e-books, voice cloning & 1107+ languages! |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
| [minio/minio](https://github.com/minio/minio) | MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
| [huggingface/chat-ui](https://github.com/huggingface/chat-ui) | Open source codebase powering the HuggingChat app |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | Multiplayer at the speed of light |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [evershopcommerce/evershop](https://github.com/evershopcommerce/evershop) | 🛍️ Typescript E-commerce Platform |
| [TibixDev/winboat](https://github.com/TibixDev/winboat) | Run Windows apps on 🐧 Linux with ✨ seamless integration |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Generate audiobooks from e-books, voice cloning & 1107+ languages! |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
<!-- END OF MONTHLY_TOP10_REPOS -->
