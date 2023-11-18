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
| [gpt-crawler](https://github.com/BuilderIO/gpt-crawler) | Crawl a site to generate knowledge files to create your own custom GPT from a URL |
| [graphcast](https://github.com/google-deepmind/graphcast) |  |
| [ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
| [Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | A GPT-4 AI Tutor Prompt for customizable personalized learning experiences. |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 12 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [eShop](https://github.com/dotnet/eShop) | A reference .NET application implementing an eCommerce site |
| [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt) | store all chatgpt's system prompt |
| [dify](https://github.com/langgenius/dify) | An Open-Source Assistants API and GPTs alternative. Dify.AI is an LLM application development platform. It integrates the concepts of Backend as a Service and LLMOps, covering the core tech stack required for building generative AI-native applications, including a built-in RAG engine. |
| [terraform](https://github.com/hashicorp/terraform) | Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned. |
| [narrator](https://github.com/cbh123/narrator) | David Attenborough narrates your life |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [smallchat](https://github.com/antirez/smallchat) | A minimal programming example for a chat server |
| [Xray-core](https://github.com/XTLS/Xray-core) | Xray, Penetrates Everything. Also the best v2ray-core, with XTLS support. Fully compatible configuration. |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 12 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [v2rayN](https://github.com/2dust/v2rayN) | A GUI client for Windows, support Xray core and v2fly core and others |
| [sing-box](https://github.com/SagerNet/sing-box) | The universal proxy platform |
| [hysteria](https://github.com/apernet/hysteria) | Hysteria is a powerful, lightning fast and censorship resistant proxy. |
| [clash-verge](https://github.com/zzzgydi/clash-verge) | A Clash GUI based on tauri. Supports Windows, macOS and Linux. |
| [angular](https://github.com/angular/angular) | The modern web developer’s platform |
| [openai-cookbook](https://github.com/openai/openai-cookbook) | Examples and guides for using the OpenAI API |
| [openai-python](https://github.com/openai/openai-python) | The official Python library for the OpenAI API |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [clash-verge](https://github.com/zzzgydi/clash-verge) | A Clash GUI based on tauri. Supports Windows, macOS and Linux. |
| [localsend](https://github.com/localsend/localsend) | An open source cross-platform alternative to AirDrop |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [v2rayN](https://github.com/2dust/v2rayN) | A GUI client for Windows, support Xray core and v2fly core and others |
| [hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
| [sing-box](https://github.com/SagerNet/sing-box) | The universal proxy platform |
| [autogen](https://github.com/microsoft/autogen) | Enable Next-Gen Large Language Model Applications. Join our Discord: https://discord.gg/pAbnFJrkgZ |
| [Xray-core](https://github.com/XTLS/Xray-core) | Xray, Penetrates Everything. Also the best v2ray-core, with XTLS support. Fully compatible configuration. |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | IDURAR Open Code Source ERP CRM Alternative to SalesForce | Node Js React AntD MERN |
<!-- END OF MONTHLY_TOP10_REPOS -->
