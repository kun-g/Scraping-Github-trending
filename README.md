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
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor plugin specification and official plugins |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub:https://clianything.cc/ |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary |
| [getarcaneapp/arcane](https://github.com/getarcaneapp/arcane) | Modern Docker Management, Designed for Everyone |
| [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) | Multi-tier framework for evaluating AI agent skills and plugins with quality gates, security scanning, harness compatibility checks, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior. Ships reusable CI templates that bring every check to any repository. |
| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions. |
| [astral-sh/uv](https://github.com/astral-sh/uv) | An extremely fast Python package and project manager, written in Rust. |
| [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) | PaperOrchestra is a multi-agent framework for automated AI research paper writing. |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor. |
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | web development for the rest of us |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | Keep your coding agent up to date with the latest web best practices |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | The workspace to stay in the loop and on top of agents - shape, decide, plan, annotate, review code, share with team, and send all feedback to agents with one click. |
| [meta/astryx](https://github.com/meta/astryx) | An open source design system that's fully customizable and agent ready |
| [we-promise/sure](https://github.com/we-promise/sure) | The personal finance app for everyone (by everyone) |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor. |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | Claude Code skills for equity investors and traders — market analysis, technical charting, economic calendars, screeners, and trading strategy development. |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for coding agents |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Anti-AI-slop design skill for Claude Code, Cursor, and Codex. |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | The best way to control Claude Code, Codex and more from any computer or phone |
| [php/php-src](https://github.com/php/php-src) | The PHP Interpreter |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Open-source Grok Bot alternative with a virtual machine that bots can use |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships. |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | The workspace to stay in the loop and on top of agents - shape, decide, plan, annotate, review code, share with team, and send all feedback to agents with one click. |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | DeepTutor: Lifelong Personalized Tutoring.https://deeptutor.info/. |
<!-- END OF MONTHLY_TOP10_REPOS -->
