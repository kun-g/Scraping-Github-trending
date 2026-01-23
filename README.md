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
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 🎥 Make videos programmatically with React |
| [block/goose](https://github.com/block/goose) | an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
| [xai-org/grok-1](https://github.com/xai-org/grok-1) | Grok open release |
| [deepseek-ai/FlashMLA](https://github.com/deepseek-ai/FlashMLA) | FlashMLA: Efficient Multi-head Latent Attention Kernels |
| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | The absolute trainer to light up AI agents. |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Free, local, open-source Cowork for Gemini CLI, Claude Code, Codex, Opencode, Qwen Code, Goose Cli, Auggie, and more | 🌟 Star if you like it! |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack. |
| [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | 10 Weeks, 20 Lessons, Data Science for All! |
| [nexmoe/VidBee](https://github.com/nexmoe/VidBee) | Download videos from almost any website worldwide |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | Eigent: The Open Source Cowork Desktop to Unlock Your Exceptional Productivity. |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Free, local, open-source Cowork for Gemini CLI, Claude Code, Codex, Opencode, Qwen Code, Goose Cli, Auggie, and more | 🌟 Star if you like it! |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | The open source coding agent. |
| [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | 程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享大模型选择指南（DeepSeek / GPT / Gemini / Claude）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（RAG / MCP / A2A）、AI 编程技巧、AI 工具用法（Cursor / Claude Code / TRAE / Lovable / Agent Skills）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档版本，已升级为鱼皮 AI 导航网站 |
| [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | Autonomous AI development loop for Claude Code with intelligent exit detection |
| [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) | bluetooth mesh chat, IRC vibes |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | A Collection of Skills for Claude Code and Claude AI for real-world Usage. Including Claude Code Subagents, Claude Code Commnads |
| [google/langextract](https://github.com/google/langextract) | A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | The open source coding agent. |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Get 10X more out of Claude Code, Codex or any coding agent |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [tw93/Mole](https://github.com/tw93/Mole) | 🐹 Deep clean and optimize your Mac. |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |
| [usememos/memos](https://github.com/usememos/memos) | An open-source, self-hosted note-taking service. Your thoughts, your data, your control — no tracking, no ads, no subscription fees. |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | How can we build a true AI agent? Like Claude Code. |
<!-- END OF MONTHLY_TOP10_REPOS -->
