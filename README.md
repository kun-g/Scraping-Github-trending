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
| [audiocraft](https://github.com/facebookresearch/audiocraft) | Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning. |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with Llama 2 and other large language models locally |
| [The-Art-of-Linear-Algebra](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra) | Graphic notes on Gilbert Strang's "Linear Algebra for Everyone" |
| [weekly](https://github.com/ruanyf/weekly) | 科技爱好者周刊，每周五发布 |
| [LLaMA2-Accessory](https://github.com/Alpha-VLLM/LLaMA2-Accessory) | An Open-source Toolkit for LLM Development |
| [manticoresearch](https://github.com/manticoresoftware/manticoresearch) | Easy to use open source fast database for search | Good alternative to Elasticsearch now | Drop-in replacement for E in the ELK soon |
| [Summer2024-Internships](https://github.com/SimplifyJobs/Summer2024-Internships) | Collection of Summer 2023 & Summer 2024 tech internships! |
| [codecov-api](https://github.com/codecov/codecov-api) | Code for the API of Codecov |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [nextui](https://github.com/nextui-org/nextui) | 🚀 Beautiful, fast and modern React UI library. |
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
