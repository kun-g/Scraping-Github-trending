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
| [geektime-books](https://github.com/it-ebooks-0/geektime-books) | 📚 极客时间电子书 |
| [khoj](https://github.com/khoj-ai/khoj) | Your AI second brain. A copilot to get answers to your questions, whether they be from your own notes or from the internet. Use powerful, online (e.g gpt4) or private, local (e.g llama3) LLMs. Self-host locally or use our cloud instance. Access from Obsidian, Emacs, Desktop app, Web or Whatsapp. |
| [MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone |
| [Amber](https://github.com/Ph0enixKM/Amber) | 💎 Amber the programming language compiled to bash |
| [realworld](https://github.com/gothinkster/realworld) | "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more |
| [cover-agent](https://github.com/Codium-ai/cover-agent) | CodiumAI Cover-Agent: An AI-Powered Tool for Automated Test Generation and Code Coverage Enhancement! 💻🤖🧪🐞 |
| [angular](https://github.com/angular/angular) | Deliver web apps with confidence 🚀 |
| [neosync](https://github.com/nucleuscloud/neosync) | Open source data anonymization and synthetic data orchestration for developers. Create high fidelity synthetic data and sync it across your environments. |
| [llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [GitHub-Chinese-Top-Charts](https://github.com/GrowingGit/GitHub-Chinese-Top-Charts) | 🇨🇳 GitHub中文排行榜，各语言分设「软件 | 资料」榜单，精准定位中文好项目。各取所需，高效学习。 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Bend](https://github.com/HigherOrderCO/Bend) | A massively parallel, high-level programming language |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [java-design-patterns](https://github.com/iluwatar/java-design-patterns) | Design patterns implemented in Java |
| [HVM](https://github.com/HigherOrderCO/HVM) | A massively parallel, optimal functional runtime in Rust |
| [firecrawl](https://github.com/mendableai/firecrawl) | 🔥 Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl, search and extract with a single API. |
| [EasySpider](https://github.com/NaiboWang/EasySpider) | A visual no-code/code-free web crawler/spider易采集：一个可视化浏览器自动化测试/数据采集/爬虫软件，可以无代码图形化的设计和执行爬虫任务。别名：ServiceWrapper面向Web应用的智能化服务封装系统。 |
| [bulletproof-react](https://github.com/alan2207/bulletproof-react) | 🛡️ ⚛️ A simple, scalable, and powerful architecture for building production ready React applications. |
| [oblivion-desktop](https://github.com/bepass-org/oblivion-desktop) | Oblivion Desktop - Unofficial Warp Client for Windows/Mac/Linux |
| [ChatGPT](https://github.com/lencx/ChatGPT) | 🔮 ChatGPT Desktop Application (Mac, Windows and Linux) |
| [pokerogue](https://github.com/pagefaultgames/pokerogue) | A browser based Pokémon fangame heavily inspired by the roguelite genre. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MS-DOS](https://github.com/microsoft/MS-DOS) | The original sources of MS-DOS 1.25, 2.0, and 4.0 for reference purposes |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Assistants with memory, knowledge and tools. |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning by MyShell. |
| [nocobase](https://github.com/nocobase/nocobase) | NocoBase is a scalability-first, open-source no-code/low-code platform for building business applications and enterprise solutions. |
| [openui](https://github.com/wandb/openui) | OpenUI let's you describe UI using your imagination, then see it rendered live. |
| [douyin](https://github.com/zyronon/douyin) | Vue3 + Pinia 仿抖音，Vue 在移动端的最佳实践 . Imitate TikTok ，Vue Best practices on Mobile |
| [ChatGPT](https://github.com/lencx/ChatGPT) | 🔮 ChatGPT Desktop Application (Mac, Windows and Linux) |
| [it-tools](https://github.com/CorentinTh/it-tools) | Collection of handy online tools for developers, with great UX. |
| [pokerogue](https://github.com/pagefaultgames/pokerogue) | A browser based Pokémon fangame heavily inspired by the roguelite genre. |
| [corenet](https://github.com/apple/corenet) | CoreNet: A library for training deep neural networks |
<!-- END OF MONTHLY_TOP10_REPOS -->
