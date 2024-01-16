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
| [maybe](https://github.com/maybe-finance/maybe) | Personal finance and wealth management app |
| [tachiyomi](https://github.com/tachiyomiorg/tachiyomi) | Free and open source manga reader for Android. |
| [tachiyomi-extensions-revived](https://github.com/ThePBone/tachiyomi-extensions-revived) | Revival of removed source extensions for the Tachiyomi app. |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [everyone-can-use-english](https://github.com/xiaolai/everyone-can-use-english) | 人人都能用英语 |
| [extensions](https://github.com/tachiyomiorg/extensions) | Source extensions for the Tachiyomi app. |
| [extensions](https://github.com/keiyoushi/extensions) | Source extensions for the Tachiyomi app. |
| [autogen](https://github.com/microsoft/autogen) | Enable Next-Gen Large Language Model Applications. Join our Discord: https://discord.gg/pAbnFJrkgZ |
| [GPTs](https://github.com/linexjlin/GPTs) | leaked prompts of GPTs |
| [open-interpreter](https://github.com/KillianLucas/open-interpreter) | A natural language interface for computers |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [crewAI](https://github.com/joaomdmoura/crewAI) | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. |
| [act-plus-plus](https://github.com/MarkFzp/act-plus-plus) | Imitation learning algorithms with Co-training for Mobile ALOHA: ACT, Diffusion Policy, VINN |
| [mobile-aloha](https://github.com/MarkFzp/mobile-aloha) | Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation |
| [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) | The open-source AI chat app for everyone. |
| [audio2photoreal](https://github.com/facebookresearch/audio2photoreal) | Code and dataset for photorealistic Codec Avatars driven from audio |
| [tachiyomi](https://github.com/tachiyomiorg/tachiyomi) | Free and open source manga reader for Android. |
| [1brc](https://github.com/gunnarmorling/1brc) | 1️⃣🐝🏎️ The One Billion Row Challenge -- A fun exploration of how quickly 1B rows from a text file can be aggregated with Java |
| [TinyLlama](https://github.com/jzhang38/TinyLlama) | The TinyLlama project is an open endeavor to pretrain a 1.1B Llama model on 3 trillion tokens. |
| [jan](https://github.com/janhq/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |
| [embedchain](https://github.com/embedchain/embedchain) | The Open Source RAG framework |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | locally hosted web application that allows you to perform various operations on PDF files |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | Dev tool that writes scalable apps from scratch while the developer oversees the implementation |
| [spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source Spotify client that doesn't require Premium nor uses Electron! Available for both desktop & mobile! |
| [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) | The open-source AI chat app for everyone. |
| [TinyLlama](https://github.com/jzhang38/TinyLlama) | The TinyLlama project is an open endeavor to pretrain a 1.1B Llama model on 3 trillion tokens. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤖 Lobe Chat - an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application. |
| [Rope](https://github.com/Hillobar/Rope) | GUI-focused roop |
| [clone-voice](https://github.com/jianchang512/clone-voice) | A sound cloning tool with a web interface, using your voice or any sound to record audio / 一个带web界面的声音克隆工具，使用你的音色或任意声音来录制音频 |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with Llama 2, Mistral, and other large language models locally. |
| [ui](https://github.com/shadcn-ui/ui) | Beautifully designed components that you can copy and paste into your apps. Accessible. Customizable. Open Source. |
<!-- END OF MONTHLY_TOP10_REPOS -->
