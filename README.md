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
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices. |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework & software development methodology that works. |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub:https://clianything.cc/ |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🧠 两小时从 0 训出你的 64M 大模型。Train your own 64M LLM from scratch in 2 hours. |
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor plugin specification and official plugins |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Knowledge infrastructure to make your agents smarter. Search, scrape and access 550+ data providers through one API. |
| [nginx/nginx](https://github.com/nginx/nginx) | The official NGINX Open Source repository. |
| [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) | OpenVINO™ is an open source toolkit for optimizing and deploying AI inference |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Qoder, and Pi. 45 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop. |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | The workspace to stay in the loop and on top of agents - shape, decide, plan, annotate, review code, share with team, and send all feedback to agents with one click. |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor. |
| [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | Keep your coding agent up to date with the latest web best practices |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for coding agents |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | Claude Code skills for equity investors and traders — market analysis, technical charting, economic calendars, screeners, and trading strategy development. |
| [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | AG-UI: the Agent-User Interaction Protocol. Bring Agents into Frontend Applications. |
| [meta/astryx](https://github.com/meta/astryx) | An open source design system that's fully customizable and agent ready |
| [pookjw/HermesEnabler](https://github.com/pookjw/HermesEnabler) | Enable Hermès Watch Faces on any Apple Watch devices |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Anti-AI-slop design skill for Claude Code, Cursor, and Codex. |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Open-source Grok Bot alternative with a virtual machine that bots can use |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | The best way to control Claude Code, Codex and more from any computer or phone |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More |
| [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) | Thirteen Claude skills that run an Instagram account: Reels off 26 scored hook formulas, a viral research skill, a caption linter, and a humanizer. Free, MIT. |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | The workspace to stay in the loop and on top of agents - shape, decide, plan, annotate, review code, share with team, and send all feedback to agents with one click. |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | DeepTutor: Lifelong Personalized Tutoring.https://deeptutor.info/. |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships. |
<!-- END OF MONTHLY_TOP10_REPOS -->
