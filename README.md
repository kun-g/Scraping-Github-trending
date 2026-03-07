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
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you-owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc. |
| [microsoft/hve-core](https://github.com/microsoft/hve-core) | A refined collection of Hypervelocity Engineering components (instructions, prompts, agents) to start your project off right, or upgrade your existing projects to get the most out of all Copilots |
| [Ed1s0nZ/CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities. |
| [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | Lightning-Fast RL for LLM Reasoning and Agents. Made Simple & Flexible. |
| [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | 基于 Claude Code 的长篇网文辅助创作系统，解决 AI 写作中的「遗忘」和「幻觉」问题，支持 200 万字量级 连载创作。 |
| [openai/skills](https://github.com/openai/skills) | Skills Catalog for Codex |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience. |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [aidenybai/react-grab](https://github.com/aidenybai/react-grab) | Select context for coding agents directly from your website |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | π RuView: WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video. |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you-owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training. |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours. |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration |
| [superset-sh/superset](https://github.com/superset-sh/superset) | IDE for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl! |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Bash is all you need - A nano Claude Code–like agent, built from 0 to 1 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | Shannon Lite is a fully autonomous AI pentester for web apps and APIs. 96.15% (100/104 exploits) on a hint-free, source-aware variant of the XBOW benchmark. |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | π RuView: WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video. |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 66 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer. |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [github/gh-aw](https://github.com/github/gh-aw) | GitHub Agentic Workflows |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 💖🧸 Self hosted, you-owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported. |
| [huggingface/skills](https://github.com/huggingface/skills) |  |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Fully automatic censorship removal for language models |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours. |
<!-- END OF MONTHLY_TOP10_REPOS -->
