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
| [microsoft/fluentui-system-icons](https://github.com/microsoft/fluentui-system-icons) | Fluent System Icons are a collection of familiar, friendly and modern icons from Microsoft. |
| [anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Anthropic's Interactive Prompt Engineering Tutorial |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [immich-app/immich](https://github.com/immich-app/immich) | High performance self-hosted photo and video management solution. |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning |
| [gtsteffaniak/filebrowser](https://github.com/gtsteffaniak/filebrowser) | 📂 Web File Browser |
| [zen-browser/desktop](https://github.com/zen-browser/desktop) | Welcome to a calmer internet |
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 一款提示词优化器，助力于编写高质量的提示词 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [jwohlwend/boltz](https://github.com/jwohlwend/boltz) | Official repository for the Boltz biomolecular interaction models |
| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | TensorZero is an open-source stack for industrial-grade LLM applications. It unifies an LLM gateway, observability, optimization, evaluation, and experimentation. |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 😎 Awesome lists about all kinds of interesting topics |
| [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | Offline speech recognition API for Android, iOS, Raspberry Pi and servers with Python, Java, C# and Node |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning |
| [datawhalechina/self-llm](https://github.com/datawhalechina/self-llm) | 《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [facebookresearch/vggt](https://github.com/facebookresearch/vggt) | [CVPR 2025 Best Paper Award] VGGT: Visual Geometry Grounded Transformer |
| [filamentphp/filament](https://github.com/filamentphp/filament) | A collection of beautiful full-stack components for Laravel. The perfect starting point for your next app. Using Livewire, Alpine.js and Tailwind CSS. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. 🔔 Official updates only via twitter @Martin993886460 (Beware of fake) |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped withhttps://github.com/microsoft/RD-Agentto automate R&D process. |
| [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) | AI's query engine - Platform for building AI that can answer questions over large scale federated data. - The only MCP Server you'll ever need |
| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 所有小初高、大学PDF教材。 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | This is a repo with links to everything you'd ever want to learn about data engineering |
| [anthropics/courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | TensorZero is an open-source stack for industrial-grade LLM applications. It unifies an LLM gateway, observability, optimization, evaluation, and experimentation. |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
<!-- END OF MONTHLY_TOP10_REPOS -->
