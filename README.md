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
| [clash-verge](https://github.com/zzzgydi/clash-verge) | A Clash GUI based on tauri. Supports Windows, macOS and Linux. |
| [smallchat](https://github.com/antirez/smallchat) | A minimal programming example for a chat server |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with Llama 2 and other large language models locally |
| [v2ray-core](https://github.com/v2fly/v2ray-core) | A platform for building proxies to bypass network restrictions. |
| [sing-box](https://github.com/SagerNet/sing-box) | The universal proxy platform |
| [DagorEngine](https://github.com/GaijinEntertainment/DagorEngine) | Dagor Engine and Tools source code from Gaijin Games KFT |
| [whisper.cpp](https://github.com/ggerganov/whisper.cpp) | Port of OpenAI's Whisper model in C/C++ |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 12 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ChatGLM3](https://github.com/THUDM/ChatGLM3) | ChatGLM3 series: Open Bilingual Chat LLMs | 开源双语对话语言模型 |
| [sing-box](https://github.com/SagerNet/sing-box) | The universal proxy platform |
| [hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
| [v2rayN](https://github.com/2dust/v2rayN) | A GUI client for Windows, support Xray core and v2fly core and others |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [Xray-core](https://github.com/XTLS/Xray-core) | Xray, Penetrates Everything. Also the best v2ray-core, with XTLS support. Fully compatible configuration. |
| [Chat2DB](https://github.com/chat2db/Chat2DB) | 🔥 🔥 🔥 An intelligent and versatile general-purpose SQL client and reporting tool for databases which integrates ChatGPT capabilities.(智能的通用数据库SQL客户端和报表工具) |
| [v2rayNG](https://github.com/2dust/v2rayNG) | A V2Ray client for Android, support Xray core and v2fly core |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [odigos](https://github.com/keyval-dev/odigos) | Distributed tracing without code changes. 🚀 Instantly monitor any application using OpenTelemetry and eBPF |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [autogen](https://github.com/microsoft/autogen) | Enable Next-Gen Large Language Model Applications. Join our Discord: https://discord.gg/pAbnFJrkgZ |
| [LLaVA](https://github.com/haotian-liu/LLaVA) | [NeurIPS'23 Oral] Visual Instruction Tuning: LLaVA (Large Language-and-Vision Assistant) built towards GPT-4V level capabilities. |
| [DocsGPT](https://github.com/arc53/DocsGPT) | GPT-powered chat for documentation, chat with your documents |
| [clash-verge](https://github.com/zzzgydi/clash-verge) | A Clash GUI based on tauri. Supports Windows, macOS and Linux. |
| [localsend](https://github.com/localsend/localsend) | An open source cross-platform alternative to AirDrop |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
| [formbricks](https://github.com/formbricks/formbricks) | Open Source Survey Toolbox |
<!-- END OF MONTHLY_TOP10_REPOS -->
