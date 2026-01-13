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
| [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | Fullstack app framework for web, desktop, and mobile. |
| [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 | 知乎问答文章｜评论爬虫 |
| [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | Autonomous AI development loop for Claude Code with intelligent exit detection |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | Collection of publicly available IPTV channels from all over the world |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |
| [obra/superpowers](https://github.com/obra/superpowers) | Claude Code superpowers: core skills library |
| [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks. |
| [home-assistant/home-assistant.io](https://github.com/home-assistant/home-assistant.io) | 📘 Home Assistant User documentation |
| [mpv-player/mpv](https://github.com/mpv-player/mpv) | 🎥 Command line media player |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | The open source coding agent. |
| [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | Autonomous AI development loop for Claude Code with intelligent exit detection |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |
| [obra/superpowers](https://github.com/obra/superpowers) | Claude Code superpowers: core skills library |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for coding agents |
| [steveyegge/beads](https://github.com/steveyegge/beads) | Beads - A memory upgrade for your coding agent |
| [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | Microsoft PowerToys is a collection of utilities that help you customize Windows and streamline everyday tasks |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Get 10X more out of Claude Code, Codex or any coding agent |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | The open source coding agent. |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Get 10X more out of Claude Code, Codex or any coding agent |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [exo-explore/exo](https://github.com/exo-explore/exo) | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | SoTA open-source TTS |
| [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | Personal AI Infrastructure for upgrading humans. |
| [steveyegge/beads](https://github.com/steveyegge/beads) | Beads - A memory upgrade for your coding agent |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | How can we build a true AI agent? Like Claude Code. |
<!-- END OF MONTHLY_TOP10_REPOS -->
