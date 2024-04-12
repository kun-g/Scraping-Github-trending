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
| [llm.c](https://github.com/karpathy/llm.c) | LLM training in simple, raw C/CUDA |
| [FreeAskInternet](https://github.com/nashsu/FreeAskInternet) | FreeAskInternet is a completely free, PRIVATE and LOCALLY running search aggregator & answer generate using MULTI LLMs, without GPU needed. The user can ask a question and the system will make a multi engine search and combine the search result to LLM and generate the answer based on search results. It's all FREE to use. |
| [morphic](https://github.com/miurla/morphic) | An AI-powered answer engine with a generative UI |
| [googletest](https://github.com/google/googletest) | GoogleTest - Google Testing and Mocking Framework |
| [llama2.c](https://github.com/karpathy/llama2.c) | Inference Llama 2 in one file of pure C |
| [Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan) | This project aim to reproduce Sora (Open AI T2V model), we wish the open source community contribute to this project. |
| [auto-code-rover](https://github.com/nus-apr/auto-code-rover) | A project structure aware autonomous software engineer aiming for autonomous program improvement |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) | Python - 100天从新手到大师 |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [OpenDevin](https://github.com/OpenDevin/OpenDevin) | 🐚 OpenDevin: Code Less, Make More |
| [VoiceCraft](https://github.com/jasonppy/VoiceCraft) | Zero-Shot Speech Editing and Text-to-Speech in the Wild |
| [valkey](https://github.com/valkey-io/valkey) | A new project to resume development on the formerly open-source Redis project. We're calling it Valkey, since it's a twist on the key-value datastore. |
| [llm-answer-engine](https://github.com/developersdigest/llm-answer-engine) | Build a Perplexity-Inspired Answer Engine Using Next.js, Groq, Mixtral, Langchain, OpenAI, Brave & Serper |
| [AniPortrait](https://github.com/Zejun-Yang/AniPortrait) | AniPortrait: Audio-Driven Synthesis of Photorealistic Portrait Animation |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Create Customized Software using Natural Language Idea (through LLM-powered Multi-Agent Collaboration) |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [helix](https://github.com/helix-editor/helix) | A post-modern modal text editor. |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | Open-Sora: Democratizing Efficient Video Production for All |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | The first real AI developer |
| [ui](https://github.com/atherosai/ui) | Simple UI examples from my social media |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
| [rolldown](https://github.com/rolldown/rolldown) | Fast Rust bundler for JavaScript with Rollup-compatible API. |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
| [bruno](https://github.com/usebruno/bruno) | Opensource IDE For Exploring and Testing Api's (lightweight alternative to postman/insomnia) |
<!-- END OF MONTHLY_TOP10_REPOS -->
