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
| [OpenGFW](https://github.com/apernet/OpenGFW) | OpenGFW is a flexible, easy-to-use, open source implementation of GFW on Linux |
| [rustdesk](https://github.com/rustdesk/rustdesk) | An open-source remote desktop, and alternative to TeamViewer. |
| [spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source Spotify client that doesn't require Premium nor uses Electron! Available for both desktop & mobile! |
| [palworld-server-docker](https://github.com/thijsvanloef/palworld-server-docker) | A Docker Container to easily run a Palworld dedicated server. |
| [Reactive-Resume](https://github.com/AmruthPillai/Reactive-Resume) | A one-of-a-kind resume builder that keeps your privacy in mind. Completely secure, customizable, portable, open-source and free forever. Try it out today! |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
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
