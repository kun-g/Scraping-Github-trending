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
| [black](https://github.com/psf/black) | The uncompromising Python code formatter |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [OpenAgents](https://github.com/xlang-ai/OpenAgents) | OpenAgents: An Open Platform for Language Agents in the Wild |
| [awesome-english-ebooks](https://github.com/hehonghui/awesome-english-ebooks) | 经济学人(含音频)、纽约客、卫报、连线、大西洋月刊等英语杂志免费下载,支持epub、mobi、pdf格式, 每周更新 |
| [react-agent](https://github.com/eylonmiz/react-agent) | The open-source React.js Autonomous LLM Agent |
| [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools) | Effortlessly discover API behaviour with a Chrome extension that automatically generates OpenAPI specifications in real time for any app or website |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [googletest](https://github.com/google/googletest) | GoogleTest - Google Testing and Mocking Framework |
| [3DGPT](https://github.com/Chuny1/3DGPT) |  |
| [jsoncrack.com](https://github.com/AykutSarac/jsoncrack.com) | ✨ Innovative and open-source visualization application that transforms various data formats, such as JSON, YAML, XML, CSV and more, into interactive graphs. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [system-design-101](https://github.com/ByteByteGoHq/system-design-101) | Explain complex systems using visuals and simple terms. Help you prepare for system design interviews. |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines. |
| [XAgent](https://github.com/OpenBMB/XAgent) | An Autonomous LLM Agent for Complex Task Solving |
| [MemGPT](https://github.com/cpacker/MemGPT) | Teaching LLMs memory management for unbounded context 📚🦙 |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [localsend](https://github.com/localsend/localsend) | An open source cross-platform alternative to AirDrop |
| [codeshell](https://github.com/WisdomShell/codeshell) | A series of code large language models developed by PKU-KCL |
| [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [incubator-answer](https://github.com/apache/incubator-answer) | A Q&A platform software for teams at any scales. Whether it's a community forum, help center, or knowledge management platform, you can always count on Answer. |
| [video-retalking](https://github.com/OpenTalker/video-retalking) | [SIGGRAPH Asia 2022] VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild |
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
