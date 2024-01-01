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
| [movie-web](https://github.com/movie-web/movie-web) | A small web app for watching movies and shows easily |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source Spotify client that doesn't require Premium nor uses Electron! Available for both desktop & mobile! |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating |
| [rinha-de-algoritmos](https://github.com/Universidade-Livre/rinha-de-algoritmos) | Na Rinha de Algoritmos você deve utilizar suas habilidades para a criação de algoritmos eficientes para resolver problemas! |
| [llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [promptoftheyear](https://github.com/successfulstudy/promptoftheyear) | In the evolving world of Large Language Models (LLMs), crafting effective prompts has become an essential skill. That's why I've created this collection, showcasing the most impactful prompts of the year across various intriguing domains. 🌐 |
| [flowpilot](https://github.com/flowdriveai/flowpilot) | flow-pilot is an openpilot based driver assistance system that runs on linux, windows and android powered machines. |
| [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | A community-supported supercharged version of paperless: scan, index and archive all your physical documents |
| [Perfect-Roadmap-To-Learn-Data-Science-In-2024](https://github.com/krishnaik06/Perfect-Roadmap-To-Learn-Data-Science-In-2024) |  |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | locally hosted web application that allows you to perform various operations on PDF files |
| [StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion) | StreamDiffusion: A Pipeline-Level Solution for Real-Time Interactive Generation |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [Rope](https://github.com/Hillobar/Rope) | GUI-focused roop |
| [clone-voice](https://github.com/jianchang512/clone-voice) | A sound cloning tool with a web interface, using your voice or any sound to record audio / 一个带web界面的声音克隆工具，使用你的音色或任意声音来录制音频 |
| [ui](https://github.com/shadcn-ui/ui) | Beautifully designed components that you can copy and paste into your apps. Accessible. Customizable. Open Source. |
| [imessage](https://github.com/beeper/imessage) | A Matrix-iMessage puppeting bridge. |
| [crewAI](https://github.com/joaomdmoura/crewAI) |  |
| [spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source Spotify client that doesn't require Premium nor uses Electron! Available for both desktop & mobile! |
| [Reactive-Resume](https://github.com/AmruthPillai/Reactive-Resume) | A one-of-a-kind resume builder that keeps your privacy in mind. Completely secure, customizable, portable, open-source and free forever. Try it out today! |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [WeChatMsg](https://github.com/LC044/WeChatMsg) | 提取微信聊天记录，将其导出成HTML、Word、CSV文档永久保存，对聊天记录进行分析生成年度聊天报告 |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤖 Lobe Chat - an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application. |
| [project-based-learning](https://github.com/practical-tutorials/project-based-learning) | Curated list of project-based tutorials |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | locally hosted web application that allows you to perform various operations on PDF files |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Open-source ChatGPT experience for both open and closed source LLMs, embedders, and vector databases. Unlimited documents, messages, and concurrent users with permission management in one app. |
| [deploy](https://github.com/pandora-next/deploy) | Pandora Cloud + Pandora Server + Shared Chat + BackendAPI Proxy + Chat2API + Signup Free = PandoraNext. New GPTs(Gizmo) UI, All in one! |
| [GPTs](https://github.com/linexjlin/GPTs) | leaked prompts of GPTs |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with Llama 2 and other large language models locally |
| [seamless_communication](https://github.com/facebookresearch/seamless_communication) | Foundational Models for State-of-the-Art Speech and Text Translation |
<!-- END OF MONTHLY_TOP10_REPOS -->
