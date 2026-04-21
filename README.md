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
| [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment. |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | π RuView: WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video. |
| [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | AI You Control: Choose your models. Own your data. Eliminate vendor lock-in. |
| [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | A community-supported supercharged document management system: scan, index and archive all your documents |
| [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | Enterprise Architecture Governance & Vendor Procurement Toolkit |
| [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | A lightweight, powerful framework for multi-agent workflows |
| [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scaling |
| [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole) | A black hole for Internet advertisements |
| [XTLS/Xray-core](https://github.com/XTLS/Xray-core) | Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |
| [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption |
| [EvoMap/evolver](https://github.com/EvoMap/evolver) | The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai |
| [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | 《动手学大模型Dive into LLMs》系列编程实践教程 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [multica-ai/multica](https://github.com/multica-ai/multica) | The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills. |
| [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | The open-source voice synthesis studio |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [pascalorg/editor](https://github.com/pascalorg/editor) | Create and share 3D architectural projects. |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy. |
| [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio. |
| [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | A gallery that showcases on-device ML/GenAI use cases and allows people to try and use models locally. |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours. |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning |
<!-- END OF MONTHLY_TOP10_REPOS -->
