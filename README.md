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
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
| [xiangechen/chili3d](https://github.com/xiangechen/chili3d) | A web-based 3D CAD application for online model design and editing |
| [datawhalechina/self-llm](https://github.com/datawhalechina/self-llm) | 《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程 |
| [jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) | This is a python API which allows you to get the transcript/subtitles for a given YouTube video. It also works for automatically generated subtitles and it does not require an API key nor a headless browser, like other selenium based solutions do! |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 11 Lessons to Get Started Building AI Agents |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | The LLM Evaluation Framework |
| [YaLTeR/niri](https://github.com/YaLTeR/niri) | A scrollable-tiling Wayland compositor. |
| [FareedKhan-dev/all-rag-techniques](https://github.com/FareedKhan-dev/all-rag-techniques) | Implementation of all RAG techniques in a simpler way |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | TensorZero is an open-source stack for industrial-grade LLM applications. It unifies an LLM gateway, observability, optimization, evaluation, and experimentation. |
| [frdel/agent-zero](https://github.com/frdel/agent-zero) | Agent Zero AI framework |
| [netbirdio/netbird](https://github.com/netbirdio/netbird) | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. |
| [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | 🪐 Markdown with superpowers — from ideas to presentations, articles and books. |
| [XTLS/Xray-core](https://github.com/XTLS/Xray-core) | Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses. |
| [datawhalechina/self-llm](https://github.com/datawhalechina/self-llm) | 《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程 |
| [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | The Cursor for Designers • An Open-Source Visual Vibecoding Editor • Visually build, style, and edit your React App with AI |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 所有小初高、大学PDF教材。 |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. 🔔 Official updates only via twitter @Martin993886460. Any other account is fake. |
| [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | The Cursor for Designers • An Open-Source Visual Vibecoding Editor • Visually build, style, and edit your React App with AI |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped withhttps://github.com/microsoft/RD-Agentto automate R&D process. |
| [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) | AI's query engine - Platform for building AI that can answer questions over large scale federated data. - The only MCP Server you'll ever need |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory for AI Agents; Announcing OpenMemory MCP - local and secure memory management. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [anthropics/courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [xming521/WeClone](https://github.com/xming521/WeClone) | 🚀 One-stop solution for creating your digital avatar from chat history 💡 Fine-tune LLMs with your chat logs to capture your unique style, then bind to a chatbot to bring your digital self to life. 从聊天记录创造数字分身的一站式解决方案 |
<!-- END OF MONTHLY_TOP10_REPOS -->
