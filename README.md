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
| [system-design-101](https://github.com/ByteByteGoHq/system-design-101) | Explain complex systems using visuals and simple terms. Help you prepare for system design interviews. |
| [openpilot](https://github.com/commaai/openpilot) | openpilot is an open source driver assistance system. openpilot performs the functions of Automated Lane Centering and Adaptive Cruise Control for 250+ supported car makes and models. |
| [localsend](https://github.com/localsend/localsend) | An open source cross-platform alternative to AirDrop |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [deepsparse](https://github.com/neuralmagic/deepsparse) | Sparsity-aware deep learning inference runtime for CPUs |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) | OpenAI's Code Interpreter in your terminal, running locally |
| [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [gpt4free](https://github.com/xtekky/gpt4free) | The official gpt4free repository | various collection of powerful language models |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines. |
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
