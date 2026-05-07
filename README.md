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
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Production-grade engineering skills for AI coding agents. |
| [PriorLabs/TabPFN](https://github.com/PriorLabs/TabPFN) | ⚡ TabPFN: Foundation Model for Tabular Data ⚡ |
| [docusealco/docuseal](https://github.com/docusealco/docuseal) | Open source DocuSign alternative. Create, fill, and sign digital documents ✍️ |
| [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search engines - arXiv, PubMed, your private documents. Everything Local & Encrypted. |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [InsForge/InsForge](https://github.com/InsForge/InsForge) | InsForge is a Postgres-based backend with auth, storage, compute, hosting, and AI gateway. Built for coding agents. |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) |  |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [warpdotdev/warp](https://github.com/warpdotdev/warp) | Warp is an agentic development environment, born out of the terminal. |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration |
| [soxoj/maigret](https://github.com/soxoj/maigret) | 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Coding Agent Harness |
| [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | 🚀 AI 全自动短视频引擎 | AI Fully Automated Short Video Engine |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research |
| [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | A curated list of practical Codex skills for automating workflows across the Codex CLI and API. |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl! |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you |
| [multica-ai/multica](https://github.com/multica-ai/multica) | The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported) |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets |
| [coleam00/Archon](https://github.com/coleam00/Archon) | The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Production-grade engineering skills for AI coding agents. |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | "DeepTutor: Agent-Native Personalized Learning Assistant" |
<!-- END OF MONTHLY_TOP10_REPOS -->
