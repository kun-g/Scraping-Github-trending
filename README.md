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
| [google-indexing-script](https://github.com/goenning/google-indexing-script) | Script to get your site indexed on Google in less than 48 hours |
| [llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 2, Mistral, and other large language models locally. |
| [zed](https://github.com/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. |
| [devops-exercises](https://github.com/bregman-arie/devops-exercises) | Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions |
| [system-design-101](https://github.com/ByteByteGoHq/system-design-101) | Explain complex systems using visuals and simple terms. Help you prepare for system design interviews. |
| [papers-we-love](https://github.com/papers-we-love/papers-we-love) | Papers from the computer science community to read and discuss. |
| [RPG-DiffusionMaster](https://github.com/YangLing0818/RPG-DiffusionMaster) | Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs (PRG) |
| [Modern-CPP-Programming](https://github.com/federico-busato/Modern-CPP-Programming) | Modern C++ Programming Course (C++11/14/17/20) |
| [GenerativeAIExamples](https://github.com/NVIDIA/GenerativeAIExamples) | Generative AI reference workflows optimized for accelerated infrastructure and microservice architecture. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [maybe](https://github.com/maybe-finance/maybe) | Personal finance and wealth management app |
| [raddebugger](https://github.com/EpicGames/raddebugger) | A native, user-mode, multi-process, graphical debugger. |
| [everyone-can-use-english](https://github.com/xiaolai/everyone-can-use-english) | 人人都能用英语 |
| [QAnything](https://github.com/netease-youdao/QAnything) | Question and Answer based on Anything. |
| [tachiyomi](https://github.com/tachiyomiorg/tachiyomi) | Free and open source manga reader for Android. |
| [data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | Free Data Engineering course! |
| [gateway](https://github.com/Portkey-AI/gateway) | A Blazing Fast AI Gateway. Route to 100+ LLMs with 1 fast & friendly API. |
| [extensions](https://github.com/keiyoushi/extensions) | Source extensions for the Mihon/Tachiyomi app. |
| [LibreChat](https://github.com/danny-avila/LibreChat) | Enhanced ChatGPT Clone: Features OpenAI, GPT-4 Vision, Bing, Anthropic, OpenRouter, Google Gemini, AI model switching, message search, langchain, DALL-E-3, ChatGPT Plugins, OpenAI Functions, Secure Multi-User System, Presets, completely open-source for self-hosting. More features in development |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) | A natural language interface for computers |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion) | StreamDiffusion: A Pipeline-Level Solution for Real-Time Interactive Generation |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | locally hosted web application that allows you to perform various operations on PDF files |
| [tachiyomi](https://github.com/tachiyomiorg/tachiyomi) | Free and open source manga reader for Android. |
| [spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source Spotify client that doesn't require Premium nor uses Electron! Available for both desktop & mobile! |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) | The open-source AI chat app for everyone. |
| [data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | Free Data Engineering course! |
| [ui](https://github.com/shadcn-ui/ui) | Beautifully designed components that you can copy and paste into your apps. Accessible. Customizable. Open Source. |
| [TinyLlama](https://github.com/jzhang38/TinyLlama) | The TinyLlama project is an open endeavor to pretrain a 1.1B Llama model on 3 trillion tokens. |
| [Rope](https://github.com/Hillobar/Rope) | GUI-focused roop |
<!-- END OF MONTHLY_TOP10_REPOS -->
