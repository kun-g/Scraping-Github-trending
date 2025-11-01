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
| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |
| [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | CRS-自建Claude Code镜像，一站式开源中转服务，让 Claude、OpenAI、Gemini、Droid 订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 |
| [ventoy/Ventoy](https://github.com/ventoy/Ventoy) | A new bootable USB solution. |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) | Community curated list of templates for the nuclei engine to find security vulnerabilities. |
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | A modern formatting library |
| [qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) | API, CLI, and Web App for analyzing and finding a person's profile in 1000 social media \ websites |
| [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) | OpenTelemetry Collector |
| [yhirose/cpp-httplib](https://github.com/yhirose/cpp-httplib) | A C++ header-only HTTP/HTTPS server and client library |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.49.x]（Reset Cursor AI MachineID & Bypass Higher Token Limit） Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [cjpais/Handy](https://github.com/cjpais/Handy) | A free, open source, and extensible speech-to-text application that works completely offline. |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | There can be more than Notion and Miro. AFFiNE(pronounced [ə‘fain]) is a next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, open-source, customizable and ready to use. |
| [minio/minio](https://github.com/minio/minio) | MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. |
| [allenai/olmocr](https://github.com/allenai/olmocr) | Toolkit for linearizing PDFs for LLM datasets/training |
| [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark) | Blind&Invisible Watermark ，图片盲水印，提取水印无须原图！ |
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [cjpais/Handy](https://github.com/cjpais/Handy) | A free, open source, and extensible speech-to-text application that works completely offline. |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Generate audiobooks from e-books, voice cloning & 1107+ languages! |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [evershopcommerce/evershop](https://github.com/evershopcommerce/evershop) | 🛍️ Typescript E-commerce Platform |
| [TibixDev/winboat](https://github.com/TibixDev/winboat) | Run Windows apps on 🐧 Linux with ✨ seamless integration |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | An Open Source implementation of Notebook LM with more flexibility and features |
<!-- END OF MONTHLY_TOP10_REPOS -->
