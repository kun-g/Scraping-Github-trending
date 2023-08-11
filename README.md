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
| [candle](https://github.com/huggingface/candle) | Minimalist ML framework for Rust |
| [one-api](https://github.com/songquanpeng/one-api) | OpenAI 接口管理 & 分发系统，支持 Azure、Anthropic Claude、Google PaLM 2、智谱 ChatGLM、百度文心一言、讯飞星火认知以及阿里通义千问，可用于二次分发管理 key，仅单可执行文件，已打包好 Docker 镜像，一键部署，开箱即用. OpenAI key management & redistribution system, using a single API for all LLMs, and features an English UI. |
| [generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | Sample code and notebooks for Generative AI on Google Cloud |
| [generative_agents](https://github.com/joonspk-research/generative_agents) | Generative Agents: Interactive Simulacra of Human Behavior |
| [AudioLDM2](https://github.com/haoheliu/AudioLDM2) | Text-to-Audio/Music Generation |
| [themes](https://github.com/radix-ui/themes) | Radix Themes is an open-source component library optimized for fast development, easy maintenance, and accessibility. Maintained by @workos. |
| [run](https://github.com/The-Run-Philosophy-Organization/run) | 润学全球官方指定GITHUB，整理润学宗旨、纲领、理论和各类润之实例；解决为什么润，润去哪里，怎么润三大问题； 并成为新中国人的核心宗教，核心信念。 |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [benjamincrozat.com](https://github.com/benjamincrozat/benjamincrozat.com) | Source code for Benjamin Crozat's blog built using the TALL stack and getting more than 30K monthly visitors. |
| [project-based-learning](https://github.com/practical-tutorials/project-based-learning) | Curated list of project-based tutorials |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [devops-exercises](https://github.com/bregman-arie/devops-exercises) | Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions |
| [audiocraft](https://github.com/facebookresearch/audiocraft) | Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning. |
| [gorilla](https://github.com/ShishirPatil/gorilla) | Gorilla: An API store for LLMs |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [mentat](https://github.com/biobootloader/mentat) | Mentat - The AI Coding Assistant |
| [Graphite](https://github.com/GraphiteEditor/Graphite) | 2D raster & vector editor that melds traditional layers & tools with a modern node-based, fully non-destructive procedural workflow. |
| [Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | Open Source Free ATS Tool to compare Resumes with Job Descriptions and create a score to rank them. |
| [awesome-english-ebooks](https://github.com/hehonghui/awesome-english-ebooks) | 经济学人(含音频)、纽约客、卫报、连线、大西洋月刊等英语杂志免费下载,支持epub、mobi、pdf格式, 每周更新 |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | A powerful and modular stable diffusion GUI with a graph/nodes interface. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [llama](https://github.com/facebookresearch/llama) | Inference code for LLaMA models |
| [devops-exercises](https://github.com/bregman-arie/devops-exercises) | Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | A powerful and modular stable diffusion GUI with a graph/nodes interface. |
| [noodle](https://github.com/ixahmedxi/noodle) | Open Source Education Platform |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [quivr](https://github.com/StanGirard/quivr) | 🧠 Dump all your files and chat with it using your Generative AI Second Brain using LLMs ( GPT 3.5/4, Private, Anthropic, VertexAI ) & Embeddings 🧠 |
| [h2ogpt](https://github.com/h2oai/h2ogpt) | Private Q&A and summarization of documents+images or chat with local GPT, 100% private, Apache 2.0. Supports LLaMa2, llama.cpp, and more. Demo: https://gpt.h2o.ai/ |
| [typescript-book](https://github.com/gibbok/typescript-book) | The Concise TypeScript Book: A Concise Guide to Effective Development in TypeScript. Free and Open Source. |
| [htmx](https://github.com/bigskysoftware/htmx) | </> htmx - high power tools for HTML |
<!-- END OF MONTHLY_TOP10_REPOS -->
