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
| [mattpocock/skills](https://github.com/mattpocock/skills) | Agent Skills for real engineers. Straight from my .claude directory. |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Use claude-code for free in the terminal, VSCode extension or via discord like openclaw |
| [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | ALL IN ONE Hacking Tool For Hackers |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration |
| [PostHog/posthog](https://github.com/PostHog/posthog) | 🦔 PostHog is an all-in-one developer platform for building successful products. We offer product analytics, web analytics, session replay, error tracking, feature flags, experimentation, surveys, data warehouse, a CDP, and an AI product assistant to help debug your code, ship features faster, and keep all your usage and customer data in one stack. |
| [microsoft/typescript-go](https://github.com/microsoft/typescript-go) | Staging repo for development of native port of TypeScript |
| [trycua/cua](https://github.com/trycua/cua) | Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that can control full desktops (macOS, Linux, Windows). |
| [gastownhall/beads](https://github.com/gastownhall/beads) | Beads - A memory upgrade for your coding agent |
| [curl/curl](https://github.com/curl/curl) | A command line tool and library for transferring data with URL syntax, supporting DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, MQTTS, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS. libcurl offers a myriad of powerful features |
| [home-assistant/core](https://github.com/home-assistant/core) | 🏡 Open source home automation that puts local control and privacy first. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Use claude-code for free in the terminal, VSCode extension or via discord like openclaw |
| [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment. |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | Code search MCP for Claude Code. Make entire codebase the context for any coding agent. |
| [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | AI You Control: Choose your models. Own your data. Eliminate vendor lock-in. |
| [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | ALL IN ONE Hacking Tool For Hackers |
| [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption |
| [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Claude Code skill to support Android app's reverse engineering |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Agent Skills for real engineers. Straight from my .claude directory. |
| [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | Build your own AI SRE agents. The open source toolkit for the AI era ✨ |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more. |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value. |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets |
| [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio. |
| [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment. |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | "DeepTutor: Agent-Native Personalized Learning Assistant" |
| [coleam00/Archon](https://github.com/coleam00/Archon) | The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable. |
| [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | A gallery that showcases on-device ML/GenAI use cases and allows people to try and use models locally. |
<!-- END OF MONTHLY_TOP10_REPOS -->
