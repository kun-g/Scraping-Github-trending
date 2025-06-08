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
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | Memory for AI Agents in 5 lines of code |
| [netbirdio/netbird](https://github.com/netbirdio/netbird) | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |
| [codexu/note-gen](https://github.com/codexu/note-gen) | A cross-platform Markdown note-taking application dedicated to using AI to bridge recording and writing, organizing fragmented knowledge into a readable note. |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | Scrapy, a fast high-level web crawling & scraping framework for Python. |
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | An open source collection of animated, interactive & fully customizable React components for building stunning, memorable user interfaces. |
| [jwohlwend/boltz](https://github.com/jwohlwend/boltz) | Official repository for the Boltz biomolecular interaction models |
| [deepsense-ai/ragbits](https://github.com/deepsense-ai/ragbits) | Building blocks for rapid development of GenAI applications |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | DSPy: The framework for programming—not prompting—language models |
| [Daymychen/art-design-pro](https://github.com/Daymychen/art-design-pro) | A Vue 3 admin dashboard template using Vite + TypeScript + Element Plus | vue3 admin | vue-admin — focused on user experience and visual design. |
| [langgenius/dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [frdel/agent-zero](https://github.com/frdel/agent-zero) | Agent Zero AI framework |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [anthropics/courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | 📨 The ultimate social media scheduling tool, with a bunch of AI 🤖 |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. 🔔 Official updates only via twitter @Martin993886460. Any other account is fake. |
| [imputnet/cobalt](https://github.com/imputnet/cobalt) | best way to save what you love |
| [netbirdio/netbird](https://github.com/netbirdio/netbird) | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |
| [MervinPraison/PraisonAI](https://github.com/MervinPraison/PraisonAI) | PraisonAI is a production-ready Multi AI Agents framework, designed to create AI Agents to automate and solve problems ranging from simple tasks to complex challenges. It provides a low-code solution to streamline the building and management of multi-agent LLM systems, emphasising simplicity, customisation, and effective human-agent collaboration. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. 🔔 Official updates only via twitter @Martin993886460. Any other account is fake. |
| [xming521/WeClone](https://github.com/xming521/WeClone) | 🚀 One-stop solution for creating your digital avatar from chat history 💡 Fine-tune LLMs with your chat logs to capture your unique style, then bind to a chatbot to bring your digital self to life. 从聊天记录创造数字分身的一站式解决方案 |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | The Cursor for Designers • An Open-Source Visual Vibecoding Editor • Visually build, style, and edit your React App with AI |
| [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) | AI's query engine - Platform for building AI that can answer questions over large scale federated data. - The only MCP Server you'll ever need |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory for AI Agents; SOTA in AI Agent Memory; Announcing OpenMemory MCP - local and secure memory management. |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped withhttps://github.com/microsoft/RD-Agentto automate R&D process. |
| [bytedance/flowgram.ai](https://github.com/bytedance/flowgram.ai) | FlowGram is a node-based flow building engine that helps developers quickly create workflows in either fixed layout or free connection layout modes |
| [voideditor/void](https://github.com/voideditor/void) |  |
| [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
<!-- END OF MONTHLY_TOP10_REPOS -->
