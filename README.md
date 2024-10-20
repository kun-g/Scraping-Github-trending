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
| [googleapis](https://github.com/googleapis/googleapis) | Public interface definitions of Google APIs. |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [openvmm](https://github.com/microsoft/openvmm) | Home of OpenVMM and OpenHCL. |
| [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | Learn Low Level Design (LLD) and prepare for interviews using free resources. |
| [json](https://github.com/nlohmann/json) | JSON for Modern C++ |
| [mbedtls](https://github.com/Mbed-TLS/mbedtls) | An open source, portable, easy to use, readable and flexible TLS library, and reference implementation of the PSA Cryptography API. Releases are on a varying cadence, typically around 3 - 6 months between releases. |
| [fingerprintjs](https://github.com/fingerprintjs/fingerprintjs) | The most advanced browser fingerprinting library. |
| [iree](https://github.com/iree-org/iree) | A retargetable MLIR-based machine learning compiler and runtime toolkit. |
| [cocos-engine](https://github.com/cocos/cocos-engine) | Cocos simplifies game creation and distribution with Cocos Creator, a free, open-source, cross-platform game engine. Empowering millions of developers to create high-performance, engaging 2D/3D games and instant web entertainment. |
| [chat-langchain](https://github.com/langchain-ai/chat-langchain) |  |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
| [surya](https://github.com/VikParuchuri/surya) | OCR, layout analysis, reading order, table recognition in 90+ languages |
| [platform](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) |
| [papermark](https://github.com/mfts/papermark) | Papermark is the open-source DocSend alternative with built-in analytics and custom domains. |
| [twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [hanko](https://github.com/teamhanko/hanko) | Authentication and User Management solution for developers. Open source alternative to Clerk & Auth0. |
| [siyuan](https://github.com/siyuan-note/siyuan) | A privacy-first, self-hosted, fully open source personal knowledge management software, written in typescript and golang. |
| [CS-Notes](https://github.com/CyC2018/CS-Notes) | 📚 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| [formbricks](https://github.com/formbricks/formbricks) | Open Source Survey Platform |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [llama-stack](https://github.com/meta-llama/llama-stack) | Model components of the Llama Stack APIs |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🔥🕷️ Crawl4AI: Open-source LLM Friendly Web Crawler & Scrapper |
| [platform](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) |
| [screenpipe](https://github.com/mediar-ai/screenpipe) | 24/7 local AI screen & mic recording. Works with Ollama. Llama3.2 control your computer. Alternative to Rewind.ai & Zapier. Open. Secure. You own your data. Rust. |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [manim](https://github.com/3b1b/manim) | Animation engine for explanatory math videos |
| [kestra](https://github.com/kestra-io/kestra) | ⚡ Workflow Automation Platform. Orchestrate & Schedule code in any language, run anywhere, 500+ plugins. Alternative to Zapier, Rundeck, Camunda, Airflow... |
| [Pake](https://github.com/tw93/Pake) | 🤱🏻 Turn any webpage into a desktop app with Rust. 🤱🏻 利用 Rust 轻松构建轻量级多端桌面应用 |
| [formbricks](https://github.com/formbricks/formbricks) | Open Source Survey Platform |
| [manim](https://github.com/ManimCommunity/manim) | A community-maintained Python framework for creating mathematical animations. |
<!-- END OF MONTHLY_TOP10_REPOS -->
