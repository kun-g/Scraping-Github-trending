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
| [PowerInfer](https://github.com/SJTU-IPADS/PowerInfer) | High-speed Large Language Model Serving on PCs with Consumer-grade GPUs |
| [mamba-minimal](https://github.com/johnma2006/mamba-minimal) | Simple, minimal implementation of the Mamba SSM in one file of PyTorch. |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [gpt-engineer](https://github.com/gpt-engineer-org/gpt-engineer) | Specify what you want it to build, the AI asks for clarification, and then builds it. |
| [clone-voice](https://github.com/jianchang512/clone-voice) | 一个带web界面的声音克隆工具，使用你的音色或任意声音来录制音频 |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with Llama 2 and other large language models locally |
| [the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | Master the command line, in one page |
| [dlssg-to-fsr3](https://github.com/Nukem9/dlssg-to-fsr3) | Adds AMD FSR3 Frame Generation to games by replacing Nvidia DLSS-G Frame Generation (nvngx_dlssg). |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with Llama 2 and other large language models locally |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [promptbase](https://github.com/microsoft/promptbase) | All things prompt engineering |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [Amphion](https://github.com/open-mmlab/Amphion) | Amphion (/æmˈfaɪən/) is a toolkit for Audio, Music, and Speech Generation. Its purpose is to support reproducible research and help junior researchers and engineers get started in the field of audio, music, and speech generation research and development. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤖 Lobe Chat - an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application. |
| [templ](https://github.com/a-h/templ) | A language for writing HTML user interfaces in Go. |
| [gkd](https://github.com/gkd-kit/gkd) | 基于 无障碍 + 高级选择器 + 订阅规则 的自定义屏幕点击 Android APP |
| [localsend](https://github.com/localsend/localsend) | An open-source cross-platform alternative to AirDrop |
| [oxc](https://github.com/oxc-project/oxc) | ⚓ A collection of JavaScript tools written in Rust. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [GPTs](https://github.com/linexjlin/GPTs) | leaked prompts of GPTs |
| [multipleWindow3dScene](https://github.com/bgstaal/multipleWindow3dScene) | A quick example of how one can "synchronize" a 3d scene across multiple windows using three.js and localStorage |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤖 Lobe Chat - an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application. |
| [project-based-learning](https://github.com/practical-tutorials/project-based-learning) | Curated list of project-based tutorials |
| [deploy](https://github.com/pandora-next/deploy) | Pandora Cloud + Pandora Server + Shared Chat + BackendAPI Proxy + Chat2API + Signup Free = PandoraNext. New GPTs(Gizmo) UI, All in one! |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating |
| [seamless_communication](https://github.com/facebookresearch/seamless_communication) | Foundational Models for State-of-the-Art Speech and Text Translation |
| [rags](https://github.com/run-llama/rags) | Build ChatGPT over your data, all with natural language |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Open-source ChatGPT experience for both open and closed source LLMs, embedders, and vector databases. Unlimited documents, messages, and concurrent users with permission management in one app. |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
<!-- END OF MONTHLY_TOP10_REPOS -->
