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
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines. |
| [localsend](https://github.com/localsend/localsend) | An open source cross-platform alternative to AirDrop |
| [XAgent](https://github.com/OpenBMB/XAgent) | An Autonomous LLM Agent for Complex Task Solving |
| [codeshell](https://github.com/WisdomShell/codeshell) | A series of code large language models developed by PKU-KCL |
| [codeshell-vscode](https://github.com/WisdomShell/codeshell-vscode) | An intelligent coding assistant plugin for Visual Studio Code, developed based on CodeShell |
| [deepsparse](https://github.com/neuralmagic/deepsparse) | Sparsity-aware deep learning inference runtime for CPUs |
| [autotab-starter](https://github.com/Planetary-Computers/autotab-starter) | Build browser agents for real world tasks |
| [system-design-101](https://github.com/ByteByteGoHq/system-design-101) | Explain complex systems using visuals and simple terms. Help you prepare for system design interviews. |
| [Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | A curated list of free courses & certifications. |
| [Cybersecurity101](https://github.com/danieldonda/Cybersecurity101) | Um guia abrangente para iniciantes na área de cibersegurança. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [LazyVim](https://github.com/LazyVim/LazyVim) | Neovim config for the lazy |
| [omnivore](https://github.com/omnivore-app/omnivore) | Omnivore is a complete, open source read-it-later solution for people who like reading. |
| [autogen](https://github.com/microsoft/autogen) | Enable Next-Gen Large Language Model Applications. Join our Discord: https://discord.gg/pAbnFJrkgZ |
| [formbricks](https://github.com/formbricks/formbricks) | Open Source Surveys & Experience Management Solution |
| [CogVLM](https://github.com/THUDM/CogVLM) | a state-of-the-art-level open visual language model |
| [video-retalking](https://github.com/OpenTalker/video-retalking) | [SIGGRAPH Asia 2022] VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild |
| [pi-hole](https://github.com/pi-hole/pi-hole) | A black hole for Internet advertisements |
| [swift-syntax](https://github.com/apple/swift-syntax) | A set of Swift libraries for parsing, inspecting, generating, and transforming Swift source code. |
| [localsend](https://github.com/localsend/localsend) | An open source cross-platform alternative to AirDrop |
| [coolify](https://github.com/coollabsio/coolify) | An open-source & self-hostable Heroku / Netlify alternative. Cloud version available here -> https://app.coolify.io |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Create Customized Software using Natural Language Idea (through LLM-powered Multi-Agent Collaboration) |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [LLaVA](https://github.com/haotian-liu/LLaVA) | [NeurIPS 2023 Oral] Visual Instruction Tuning: LLaVA (Large Language-and-Vision Assistant) built towards GPT-4V level capabilities. |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
| [appwrite](https://github.com/appwrite/appwrite) | Build like a team of hundreds_ |
| [novu](https://github.com/novuhq/novu) | 🔥 The open-source notification infrastructure with fully functional embedded notification center 🚀🚀🚀 |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [pandora](https://github.com/zhile-io/pandora) | 潘多拉，一个让你呼吸顺畅的ChatGPT。Pandora, a ChatGPT client that lets you breathe freely. |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [openv0](https://github.com/raidendotai/openv0) | AI generated UI components |
<!-- END OF MONTHLY_TOP10_REPOS -->
