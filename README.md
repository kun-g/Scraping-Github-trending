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
| [ChatTTS](https://github.com/2noise/ChatTTS) | ChatTTS is a generative speech model for daily dialogue. |
| [V-Express](https://github.com/tencent-ailab/V-Express) | V-Express aims to generate a talking head video under the control of a reference image, an audio, and a sequence of V-Kps images. |
| [llama-fs](https://github.com/iyaja/llama-fs) | A self-organizing file system with llama 3 |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [surya](https://github.com/VikParuchuri/surya) | OCR, layout analysis, reading order, line detection in 90+ languages |
| [mlflow](https://github.com/mlflow/mlflow) | Open source platform for the machine learning lifecycle |
| [connect](https://github.com/redpanda-data/connect) | Fancy stream processing made operationally mundane |
| [git_rce](https://github.com/amalmurali47/git_rce) | Exploit PoC for CVE-2024-32002 |
| [MusePose](https://github.com/TMElyralab/MusePose) | MusePose: a Pose-Driven Image-to-Video Framework for Virtual Human Generation |
| [kong](https://github.com/Kong/kong) | 🦍 The Cloud-Native API Gateway and AI Gateway. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [fabric](https://github.com/danielmiessler/fabric) | fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
| [khoj](https://github.com/khoj-ai/khoj) | Your AI second brain. Get answers to your questions, whether they be online or in your own notes. Use online AI models (e.g gpt4) or private, local LLMs (e.g llama3). Self-host locally or use our cloud instance. Access from Obsidian, Emacs, Desktop app, Web or Whatsapp. |
| [SWE-agent](https://github.com/princeton-nlp/SWE-agent) | SWE-agent takes a GitHub issue and tries to automatically fix it, using GPT-4, or your LM of choice. It solves 12.47% of bugs in the SWE-bench evaluation set and takes just 1.5 minutes to run. |
| [CopilotKit](https://github.com/CopilotKit/CopilotKit) | A framework for building custom AI Copilots 🤖 in-app AI chatbots, in-app AI Agents, & AI-powered Textareas. |
| [farfalle](https://github.com/rashadphz/farfalle) | 🔍 AI search engine - self-host with local or cloud LLMs |
| [CogVLM2](https://github.com/THUDM/CogVLM2) | GPT4V-level open-source multi-modal model based on Llama3-8B |
| [MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone |
| [outlines](https://github.com/outlines-dev/outlines) | Structured Text Generation |
| [LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [univer](https://github.com/dream-num/univer) | Univer is an open-source alternative to Google Sheets, Slides, and Docs |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [pykan](https://github.com/KindXiaoming/pykan) | Kolmogorov Arnold Networks |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Assistants with memory, knowledge and tools. |
| [openui](https://github.com/wandb/openui) | OpenUI let's you describe UI using your imagination, then see it rendered live. |
| [MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone |
| [hydra](https://github.com/hydralauncher/hydra) | Hydra is a game launcher with its own embedded bittorrent client and a self-managed repack scraper. |
| [it-tools](https://github.com/CorentinTh/it-tools) | Collection of handy online tools for developers, with great UX. |
| [ChatGPT](https://github.com/lencx/ChatGPT) | 🔮 ChatGPT Desktop Application (Mac, Windows and Linux) |
| [Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | A Windows and Office activator using HWID / Ohook / KMS38 / Online KMS activation methods, with a focus on open-source code and fewer antivirus detections. |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly WebUI for LLMs (Formerly Ollama WebUI) |
<!-- END OF MONTHLY_TOP10_REPOS -->
