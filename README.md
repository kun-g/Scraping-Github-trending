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
| [modular/modular](https://github.com/modular/modular) | The Modular Platform (includes MAX & Mojo) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .agents directory. |
| [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | ⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry. |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor plugin specification and official plugins |
| [santifer/career-ops](https://github.com/santifer/career-ops) | Open-source AI job search: scan job portals, evaluate listings with a structured A-F rubric into a 1.0-5.0 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…) |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Solution for long term memory for agent coding CLIs and to facilitate handoff between different agent vendors |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. |
| [agent-substrate/substrate](https://github.com/agent-substrate/substrate) | Agent Substrate: the core system |
| [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | local multi-agent harness |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No shadows. No Mermaid slop. |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills. |
| [basecamp/omarchy](https://github.com/basecamp/omarchy) | Beautiful, Modern & Opinionated Linux |
| [cactus-compute/needle](https://github.com/cactus-compute/needle) | 14MB foundation model for tiny devices; phones, wearables, smart home, and robots. |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Graph-Native Infrastructure for Context and Accountable AI Systems |
| [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | Switchyard lets LLM applications route traffic across models and providers while preserving native OpenAI and Anthropic API compatibility - enabling flexible model selection, benchmarking, and cost/performance optimization. |
| [modular/modular](https://github.com/modular/modular) | The Modular Platform (includes MAX & Mojo) |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [megadose/holehe](https://github.com/megadose/holehe) | holehe allows you to check if the mail is used on different sites like twitter, instagram and will retrieve information on sites with the forgotten password function. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [block/buzz](https://github.com/block/buzz) | A hive mind communication platform |
| [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) | bluetooth mesh chat, IRC vibes |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |
| [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you. Zero cost, zero config. |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks. |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Never stop coding. Free MIT AI gateway: one endpoint, 340 providers (90+ free), 1200+ models — Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 450+ contributors |
| [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 | 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端 |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) |  |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 12 Weeks, 24 Lessons, AI for All! |
<!-- END OF MONTHLY_TOP10_REPOS -->
