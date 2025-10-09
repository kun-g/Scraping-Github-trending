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
| [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | Stremio - Freedom to Stream |
| [Infisical/infisical](https://github.com/Infisical/infisical) | Infisical is the open-source platform for secrets management, PKI, and SSH access. |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | The AI Browser Automation Framework |
| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 所有小初高、大学PDF教材。 |
| [BeehiveInnovations/zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server) | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one. |
| [trycua/cua](https://github.com/trycua/cua) | Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that can control full desktops (macOS, Linux, Windows). |
| [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | Desktop App for downloading Videos and Audios from hundreds of sites |
| [openemr/openemr](https://github.com/openemr/openemr) | The most popular open source electronic health records and medical practice management solution. |
| [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | Open-source IoT Platform - Device management, data collection, processing and visualization. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [cjpais/Handy](https://github.com/cjpais/Handy) | A free, open source, and extensible speech-to-text application that works completely offline. |
| [microsoft/BitNet](https://github.com/microsoft/BitNet) | Official inference framework for 1-bit LLMs |
| [Infisical/infisical](https://github.com/Infisical/infisical) | Infisical is the open-source platform for secrets management, PKI, and SSH access. |
| [BeehiveInnovations/zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server) | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one. |
| [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | 基于多智能体LLM的中文金融交易框架 - TradingAgents中文增强版 |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) |  |
| [openemr/openemr](https://github.com/openemr/openemr) | The most popular open source electronic health records and medical practice management solution. |
| [YaLTeR/niri](https://github.com/YaLTeR/niri) | A scrollable-tiling Wayland compositor. |
| [nextcloud/server](https://github.com/nextcloud/server) | ☁️ Nextcloud server, a safe home for all your data |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | Tongyi Deep Research, the Leading Open-source Deep Research Agent |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |  |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | The best way to get AI coding agents to solve hard problems in complex codebases. |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | A community driven registry service for Model Context Protocol (MCP) servers. |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) | Clone a voice in 5 seconds to generate arbitrary speech in real-time |
| [coinbase/x402](https://github.com/coinbase/x402) | A payments protocol for the internet. Built on HTTP. |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) |  |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | Source code for the X Recommendation Algorithm |
<!-- END OF MONTHLY_TOP10_REPOS -->
