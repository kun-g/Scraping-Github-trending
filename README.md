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
| [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | A text-to-speech (TTS), speech-to-text (STT) and speech-to-speech (STS) library built on Apple's MLX framework, providing efficient speech analysis on Apple Silicon. |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 🎥 Make videos programmatically with React |
| [qarmin/czkawka](https://github.com/qarmin/czkawka) | Multi functional app to find duplicates, empty folders, similar images etc. |
| [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | UltraRAG v3: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | Open-Source Frontier Voice AI |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | Memory engine and app that is extremely fast, scalable. The Memory API for the AI era. |
| [Psiphon-Inc/conduit](https://github.com/Psiphon-Inc/conduit) | Conduit React Native app |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 🎥 Make videos programmatically with React |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Free, local, open-source Cowork for Gemini CLI, Claude Code, Codex, Opencode, Qwen Code, Goose Cli, Auggie, and more | 🌟 Star if you like it! |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | UltraRAG v3: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | The open source coding agent. |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Get 10X more out of Claude Code, Codex or any coding agent |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |
| [usememos/memos](https://github.com/usememos/memos) | An open-source, self-hosted note-taking service. Your thoughts, your data, your control — no tracking, no ads, no subscription fees. |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Bash is all you need！write a claude code with only 16 line code |
| [steveyegge/beads](https://github.com/steveyegge/beads) | Beads - A memory upgrade for your coding agent |
| [Lissy93/web-check](https://github.com/Lissy93/web-check) | 🕵️‍♂️ All-in-one OSINT tool for analysing any website |
<!-- END OF MONTHLY_TOP10_REPOS -->
