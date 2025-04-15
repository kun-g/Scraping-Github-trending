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
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.48.x]（Reset Cursor AI MachineID & Auto Sign Up / In & Bypass Higher Token Limit）自动注册 Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [krillinai/KrillinAI](https://github.com/krillinai/KrillinAI) | A video translation and dubbing tool powered by LLMs, offering professional-grade translations and one-click full-process deployment. It can generate content optimized for platforms like YouTube，TikTok, and Shorts. 基于AI大模型的视频翻译和配音工具，专业级翻译，一键部署全流程，可以生成适配抖音，小红书，哔哩哔哩，视频号，TikTok，Youtube Shorts等形态的内容 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [funstory-ai/BabelDOC](https://github.com/funstory-ai/BabelDOC) | Yet Another Document Translator |
| [BasedHardware/omi](https://github.com/BasedHardware/omi) | AI wearables. Put it on, speak, transcribe, automatically |
| [GuijiAI/HeyGem.ai](https://github.com/GuijiAI/HeyGem.ai) |  |
| [Zackriya-Solutions/meeting-minutes](https://github.com/Zackriya-Solutions/meeting-minutes) | A free and open source, self hosted Ai based live meeting note taker and minutes summary generator that can completely run in your Local device (Mac OS and windows OS Support added. Working on adding linux support soon) |
| [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec) | The Network Execution Tool |
| [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) | Quickstart configs for Nvim LSP |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 10 Lessons to Get Started Building AI Agents |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.48.x]（Reset Cursor AI MachineID & Auto Sign Up / In & Bypass Higher Token Limit）自动注册 Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [juliangarnier/anime](https://github.com/juliangarnier/anime) | JavaScript animation engine |
| [datawhalechina/llm-cookbook](https://github.com/datawhalechina/llm-cookbook) | 面向开发者的 LLM 入门教程，吴恩达大模型系列课程中文版 |
| [jiji262/douyin-downloader](https://github.com/jiji262/douyin-downloader) | 抖音批量下载工具，去水印，支持视频、图集、合集、音乐(原声)。免费！免费！免费！ |
| [meta-llama/llama-models](https://github.com/meta-llama/llama-models) | Utilities intended for use with Llama models. |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 10 Lessons to Get Started Building AI Agents |
| [funstory-ai/BabelDOC](https://github.com/funstory-ai/BabelDOC) | Yet Another Document Translator |
| [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | Multiplayer at the speed of light |
| [vercel/ai-chatbot](https://github.com/vercel/ai-chatbot) | A full-featured, hackable Next.js AI chatbot built by Vercel |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | A collection of MCP servers. |
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.48.x]（Reset Cursor AI MachineID & Auto Sign Up / In & Bypass Higher Token Limit）自动注册 Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) | Free, simple, fast interactive diagrams for any GitHub repository |
| [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。 |
| [th-ch/youtube-music](https://github.com/th-ch/youtube-music) | YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader) |
| [ourongxing/newsnow](https://github.com/ourongxing/newsnow) | Elegant reading of real-time and hottest news |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 10 Lessons to Get Started Building AI Agents |
| [GuijiAI/HeyGem.ai](https://github.com/GuijiAI/HeyGem.ai) |  |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [glanceapp/glance](https://github.com/glanceapp/glance) | A self-hosted dashboard that puts all your feeds in one place |
<!-- END OF MONTHLY_TOP10_REPOS -->
