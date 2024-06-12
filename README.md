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
| [LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [nanoGPT](https://github.com/karpathy/nanoGPT) | The simplest, fastest repository for training/finetuning medium-sized GPTs. |
| [coolify](https://github.com/coollabsio/coolify) | An open-source & self-hostable Heroku / Netlify / Vercel alternative. |
| [transformers.js](https://github.com/xenova/transformers.js) | State-of-the-art Machine Learning for the web. Run 🤗 Transformers directly in your browser, with no need for a server! |
| [piku](https://github.com/piku/piku) | The tiniest PaaS you've ever seen. Piku allows you to do git push deployments to your own servers. |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [gpt-2](https://github.com/openai/gpt-2) | Code for the paper "Language Models are Unsupervised Multitask Learners" |
| [frigate](https://github.com/blakeblackshear/frigate) | NVR with realtime local object detection for IP cameras |
| [nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |
| [hiring-without-whiteboards](https://github.com/poteto/hiring-without-whiteboards) | ⭐️ Companies that don't have a broken hiring process |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone |
| [duckdb](https://github.com/duckdb/duckdb) | DuckDB is an analytical in-process SQL database management system |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [litgpt](https://github.com/Lightning-AI/litgpt) | Pretrain, finetune, deploy 20+ LLMs on your own data. Uses state-of-the-art techniques: flash attention, FSDP, 4-bit, LoRA, and more. |
| [pyvideotrans](https://github.com/jianchang512/pyvideotrans) | Translate the video from one language to another and add dubbing. 将视频从一种语言翻译为另一种语言，并添加配音 |
| [aider](https://github.com/paul-gauthier/aider) | aider is AI pair programming in your terminal |
| [lazy.nvim](https://github.com/folke/lazy.nvim) | 💤 A modern plugin manager for Neovim |
| [syncthing](https://github.com/syncthing/syncthing) | Open Source Continuous File Synchronization |
| [LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone |
| [nocobase](https://github.com/nocobase/nocobase) | NocoBase is a scalability-first, open-source no-code/low-code platform for building business applications and enterprise solutions. |
| [ChatGPT](https://github.com/lencx/ChatGPT) | 🔮 ChatGPT Desktop Application (Mac, Windows and Linux) |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Assistants with memory, knowledge and tools. |
| [bulletproof-react](https://github.com/alan2207/bulletproof-react) | 🛡️ ⚛️ A simple, scalable, and powerful architecture for building production ready React applications. |
| [Scrapegraph-ai](https://github.com/VinciGit00/Scrapegraph-ai) | Python scraper based on AI |
| [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | Free MLOps course from DataTalks.Club |
| [EasySpider](https://github.com/NaiboWang/EasySpider) | A visual no-code/code-free web crawler/spider易采集：一个可视化浏览器自动化测试/数据采集/爬虫软件，可以无代码图形化的设计和执行爬虫任务。别名：ServiceWrapper面向Web应用的智能化服务封装系统。 |
| [it-tools](https://github.com/CorentinTh/it-tools) | Collection of handy online tools for developers, with great UX. |
<!-- END OF MONTHLY_TOP10_REPOS -->
