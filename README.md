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
| [Vencord](https://github.com/Vendicated/Vencord) | The cutest Discord client mod |
| [Eureka](https://github.com/eureka-research/Eureka) | Official Repository for "Eureka: Human-Level Reward Design via Coding Large Language Models" |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
| [Startup-CTO-Handbook](https://github.com/ZachGoldberg/Startup-CTO-Handbook) | The Startup CTO's Handbook, a book covering leadership, management and technical topics for leaders of software engineering teams |
| [zero123plus](https://github.com/SUDO-AI-3D/zero123plus) | Code repository for Zero123++: a Single Image to Consistent Multi-view Diffusion Base Model. |
| [googletest](https://github.com/google/googletest) | GoogleTest - Google Testing and Mocking Framework |
| [BBLL](https://github.com/xiaye13579/BBLL) | 一个第三方哔哩哔哩客户端，A third-party bilibili client。 |
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
