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
| [glance](https://github.com/glanceapp/glance) | A self-hosted dashboard that puts all your feeds in one place |
| [ChatGPT](https://github.com/lencx/ChatGPT) | 🔮 ChatGPT Desktop Application (Mac, Windows and Linux) |
| [timesfm](https://github.com/google-research/timesfm) | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
| [IC-Light](https://github.com/lllyasviel/IC-Light) | More relighting! |
| [it-tools](https://github.com/CorentinTh/it-tools) | Collection of handy online tools for developers, with great UX. |
| [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | Free MLOps course from DataTalks.Club |
| [bulletproof-react](https://github.com/alan2207/bulletproof-react) | 🛡️ ⚛️ A simple, scalable, and powerful architecture for building production ready React applications. |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly WebUI for LLMs (Formerly Ollama WebUI) |
| [hydra](https://github.com/hydralauncher/hydra) | Hydra is a game launcher with its own embedded bittorrent client and a self-managed repack scraper. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [llama3](https://github.com/meta-llama/llama3) | The official Meta Llama 3 GitHub site |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning by MyShell. |
| [douyin](https://github.com/zyronon/douyin) | Vue3 + Pinia 仿抖音，Vue 在移动端的最佳实践 . Imitate TikTok ，Vue Best practices on Mobile |
| [openui](https://github.com/wandb/openui) | OpenUI let's you describe UI using your imagination, then see it rendered live. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly WebUI for LLMs (Formerly Ollama WebUI) |
| [it-tools](https://github.com/CorentinTh/it-tools) | Collection of handy online tools for developers, with great UX. |
| [unsloth](https://github.com/unslothai/unsloth) | Finetune Llama 3, Mistral & Gemma LLMs 2-5x faster with 80% less memory |
| [twenty](https://github.com/twentyhq/twenty) | Building a modern alternative to Salesforce, powered by the community. |
| [maestro](https://github.com/Doriandarko/maestro) | A framework for Claude Opus to intelligently orchestrate subagents. |
<!-- END OF MONTHLY_TOP10_REPOS -->
