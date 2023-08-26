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
| [facefusion](https://github.com/facefusion/facefusion) | Next generation face swapper and enhancer |
| [seamless_communication](https://github.com/facebookresearch/seamless_communication) | Foundational Models for State-of-the-Art Speech and Text Translation |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | PoC for a scalable dev tool that writes entire apps from scratch while the developer oversees the implementation |
| [rustdesk](https://github.com/rustdesk/rustdesk) | An open-source remote desktop, and alternative to TeamViewer. |
| [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) | A WhatsApp client library for NodeJS that connects through the WhatsApp Web browser app |
| [funNLP](https://github.com/fighting41love/funNLP) | 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术… |
| [sqlcoder](https://github.com/defog-ai/sqlcoder) | SoTA LLM for converting natural language questions to SQL queries |
| [terraform-aws-eks](https://github.com/terraform-aws-modules/terraform-aws-eks) | Terraform module to create an Elastic Kubernetes (EKS) cluster and associated resources 🇺🇦 |
| [zap](https://github.com/uber-go/zap) | Blazing fast, structured, leveled logging in Go. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [generative_agents](https://github.com/joonspk-research/generative_agents) | Generative Agents: Interactive Simulacra of Human Behavior |
| [rift](https://github.com/morph-labs/rift) | Rift: an AI-native language server for your personal AI software engineer |
| [hackingtool](https://github.com/Z4nzu/hackingtool) | ALL IN ONE Hacking Tool For Hackers |
| [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering" |
| [SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | Multiplayer at the speed of light |
| [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | GPT based autonomous agent that does online comprehensive research on any given topic |
| [quake2-rerelease-dll](https://github.com/id-Software/quake2-rerelease-dll) |  |
| [candle](https://github.com/huggingface/candle) | Minimalist ML framework for Rust |
| [themes](https://github.com/radix-ui/themes) | Radix Themes is an open-source component library optimized for fast development, easy maintenance, and accessibility. Maintained by @workos. |
| [1Panel](https://github.com/1Panel-dev/1Panel) | 🔥 🔥 🔥 现代化、开源的 Linux 服务器运维管理面板。 |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [devops-exercises](https://github.com/bregman-arie/devops-exercises) | Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions |
| [TypeChat](https://github.com/microsoft/TypeChat) | TypeChat is a library that makes it easy to build natural language interfaces using types. |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with Llama 2 and other large language models locally |
| [Llama2-Chinese](https://github.com/FlagAlpha/Llama2-Chinese) | Llama中文社区，最好的中文Llama大模型，完全开源可商用 |
| [nextui](https://github.com/nextui-org/nextui) | 🚀 Beautiful, fast and modern React UI library. |
| [llama](https://github.com/facebookresearch/llama) | Inference code for LLaMA models |
| [ToolBench](https://github.com/OpenBMB/ToolBench) | An open platform for training, serving, and evaluating large language model for tool learning. |
| [ShortGPT](https://github.com/RayVentura/ShortGPT) | 🚀🎬 ShortGPT - Experimental AI framework for automated short/video content creation. |
| [web-check](https://github.com/Lissy93/web-check) | 🕵️‍♂️ All-in-one OSINT tool for analysing any website |
<!-- END OF MONTHLY_TOP10_REPOS -->
