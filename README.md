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
| [awslabs/amazon-bedrock-agentcore-samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples) | Amazon Bedrock Agentcore accelerates AI agents into production with the scale, reliability, and security, critical to real-world deployment. |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Get 10X more out of Claude Code, Codex or any coding agent |
| [usememos/memos](https://github.com/usememos/memos) | An open-source, self-hosted note-taking service. Your thoughts, your data, your control — no tracking, no ads, no subscription fees. |
| [organicmaps/organicmaps](https://github.com/organicmaps/organicmaps) | 🍃 Organic Maps is a free Android & iOS offline maps app for travelers, tourists, hikers, and cyclists. It uses crowd-sourced OpenStreetMap data and is developed with love by the community. No ads, no tracking, no data collection, no crapware. Please donate to support the development! |
| [afkarxyz/SpotiFLAC](https://github.com/afkarxyz/SpotiFLAC) | Get Spotify tracks in true FLAC from Tidal, Qobuz & Amazon Music — no account required. |
| [HQarroum/docker-android](https://github.com/HQarroum/docker-android) | 🤖 A minimal and customizable Docker image running the Android emulator as a service. |
| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | Introduction to Machine Learning Systems |
| [Polymarket/agents](https://github.com/Polymarket/agents) | Trade autonomously on Polymarket using AI Agents |
| [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | Official code repo for the O'Reilly Book - "Hands-On Large Language Models" |
| [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application on your personal device. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Get 10X more out of Claude Code, Codex or any coding agent |
| [antvis/Infographic](https://github.com/antvis/Infographic) | 🦋 An Infographic Generation and Rendering Framework, bring words to life with AI! |
| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | Introduction to Machine Learning Systems |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | SoTA open-source TTS |
| [rendercv/rendercv](https://github.com/rendercv/rendercv) | CV/resume generator for academics and engineers, YAML to PDF |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [alexta69/metube](https://github.com/alexta69/metube) | Self-hosted YouTube downloader (web UI for youtube-dl / yt-dlp) |
| [Flowseal/zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) |  |
| [antiwork/gumroad](https://github.com/antiwork/gumroad) | Sell stuff and see what sticks |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | Collection of publicly available IPTV channels from all over the world |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization. |
| [basecamp/fizzy](https://github.com/basecamp/fizzy) | Kanban as it should be. Not as it has been. |
| [exo-explore/exo](https://github.com/exo-explore/exo) | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Open-source platform to build and deploy AI agent workflows. |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | SoTA open-source TTS |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 |
| [sst/opencode](https://github.com/sst/opencode) | The open source coding agent. |
| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | AGENTS.md — a simple, open format for guiding coding agents |
<!-- END OF MONTHLY_TOP10_REPOS -->
