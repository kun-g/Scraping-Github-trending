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
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [valkey](https://github.com/valkey-io/valkey) | A new project to resume development on the formerly open-source Redis project. We're calling it Valkey, since it's a twist on the key-value datastore. |
| [gpt_academic](https://github.com/binary-husky/gpt_academic) | 为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。 |
| [otel-profiling-agent](https://github.com/elastic/otel-profiling-agent) | The production-scale datacenter profiler |
| [ATAC](https://github.com/Julien-cpsn/ATAC) | A simple API client (postman like) in your terminal |
| [MiniGemini](https://github.com/dvlab-research/MiniGemini) | Official implementation for Mini-Gemini |
| [harbor](https://github.com/goharbor/harbor) | An open source trusted cloud native registry project that stores, signs, and scans content. |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [Descent3](https://github.com/kevinbentley/Descent3) | Descent 3 by Outrage Entertainment |
| [code-connect](https://github.com/figma/code-connect) | A tool for connecting your design system components in code with your design system in Figma |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [plandex](https://github.com/plandex-ai/plandex) | An AI coding engine for complex tasks |
| [ore-cli](https://github.com/HardhatChad/ore-cli) |  |
| [ragflow](https://github.com/infiniflow/ragflow) | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. |
| [Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan) | This project aim to reproduce Sora (Open AI T2V model), we wish the open source community contribute to this project. |
| [llama2.c](https://github.com/karpathy/llama2.c) | Inference Llama 2 in one file of pure C |
| [cs-self-learning](https://github.com/PKUFlyingPig/cs-self-learning) | 计算机自学指南 |
| [SWE-agent](https://github.com/princeton-nlp/SWE-agent) | SWE-agent takes a GitHub issue and tries to automatically fix it, using GPT-4, or your LM of choice. It solves 12.29% of bugs in the SWE-bench evaluation set and takes just 1.5 minutes to run. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [proposal-signals](https://github.com/tc39/proposal-signals) | A proposal to add signals to JavaScript. |
| [aurora](https://github.com/aurora-develop/aurora) | free |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫 |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | Open-Sora: Democratizing Efficient Video Production for All |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | The first real AI developer |
| [supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
| [open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | A natural language interface for computers |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [source-code-hunter](https://github.com/doocs/source-code-hunter) | 😱 从源码层面，剖析挖掘互联网行业主流技术的底层实现原理，为广大开发者 “提升技术深度” 提供便利。目前开放 Spring 全家桶，Mybatis、Netty、Dubbo 框架，及 Redis、Tomcat 中间件等 |
| [skyvern](https://github.com/Skyvern-AI/skyvern) | Automate browser-based workflows with LLMs and Computer Vision |
<!-- END OF MONTHLY_TOP10_REPOS -->
