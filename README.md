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
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. |
| [groupultra/telegram-search](https://github.com/groupultra/telegram-search) | 🔍 一个功能强大的 Telegram 聊天记录搜索客户端，支持聊天记录备份和向量搜索。 |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented quantitative investment platform that aims to realize the potential, empower research, and create value using AI technologies in quantitative investment, from exploring ideas to implementing productions. Qlib supports diverse machine learning modeling paradigms. including supervised learning, market dynamics modeling, and RL. |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | The Free Software Media System - Server Backend & API |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | Collection of publicly available IPTV channels from all over the world |
| [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 4 / Gemini / Ollama / DeepSeek / Qwen), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Plugins/Artifacts) and Thinking. One-click FREE deployment of your private ChatGPT/ Claude / DeepSeek application. |
| [XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) | A cross-platform fluent-design AI-boost multi-threaded downloader built with Python. |
| [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) | AI's query engine - Platform for building AI that can answer questions over large scale federated data. - The only MCP Server you'll ever need |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 所有小初高、大学PDF教材。 |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🙌 OpenHands: Code Less, Make More |
| [appwrite/appwrite](https://github.com/appwrite/appwrite) | Build like a team of hundreds_ |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | React UI + elegant infrastructure for AI Copilots, AI chatbots, and in-app AI agents. The Agentic last-mile 🪁 |
| [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | Windows system utilities to maximize productivity |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. |
| [tinygrad/tinygrad](https://github.com/tinygrad/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [xming521/WeClone](https://github.com/xming521/WeClone) | 🚀 One-stop solution for creating your digital avatar from chat logs 💡 Fine-tune LLMs with your chat logs to capture your unique style, then bind to a chatbot to bring your digital self to life. 从聊天记录创造数字分身的一站式解决方案 |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [voideditor/void](https://github.com/voideditor/void) |  |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Collection of leaked system prompts |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. |
| [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) | Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. |
| [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) | Official repository for LTX-Video |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory for AI Agents; SOTA in AI Agent Memory; Announcing OpenMemory MCP - local and secure memory management. |
| [kortix-ai/suna](https://github.com/kortix-ai/suna) | Suna - Open Source Generalist AI Agent |
<!-- END OF MONTHLY_TOP10_REPOS -->
