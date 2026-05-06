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
| [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | Coding agent for DeepSeek models that runs in your terminal |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research |
| [docusealco/docuseal](https://github.com/docusealco/docuseal) | Open source DocuSign alternative. Create, fill, and sign digital documents ✍️ |
| [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | VSCode theme based off the easemate IDE and Jetbrains islands theme |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 14 platforms |
| [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | Incremental engine for long horizon agents 🌟 Star if you like it! |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |
| [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | A collection of projects showcasing RAG, agents, workflows, and other AI use cases |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [warpdotdev/warp](https://github.com/warpdotdev/warp) | Warp is an agentic development environment, born out of the terminal. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework |
| [soxoj/maigret](https://github.com/soxoj/maigret) | 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration |
| [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack) | Useful tool to track location or mobile number |
| [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | A curated list of practical Codex skills for automating workflows across the Codex CLI and API. |
| [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | 🚀 AI 全自动短视频引擎 | AI Fully Automated Short Video Engine |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported) |
| [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | 🪐 Markdown with superpowers: from ideas to papers, presentations, websites, books, and knowledge bases. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you |
| [multica-ai/multica](https://github.com/multica-ai/multica) | The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment. |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported) |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Production-grade engineering skills for AI coding agents. |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets |
| [coleam00/Archon](https://github.com/coleam00/Archon) | The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable. |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | "DeepTutor: Agent-Native Personalized Learning Assistant" |
<!-- END OF MONTHLY_TOP10_REPOS -->
