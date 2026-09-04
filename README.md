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
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | A modern formatting library |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .agents directory. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | The agent that grows with you |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. |
| [anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman |
| [blader/humanizer](https://github.com/blader/humanizer) | Agent skill that removes signs of AI-generated writing from text |
| [google-research/timesfm](https://github.com/google-research/timesfm) | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
| [averygan/reclip](https://github.com/averygan/reclip) | Download videos from almost any website. Lightweight, self-hosted media downloader with a clean web UI. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export. |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click |
| [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | Help AI coding agents write modern Go |
| [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | runs anywhere. uses anything |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 190,000+ scientists worldwide. 165 ready-to-use validated skills plus 100+ scientific databases covering biology, chemistry, medicine, and drug discovery. Compatible with Cursor, Claude Code, Codex, Pi, Antigravity, and the open Agent Skills standard. |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🧠 Train a 64M-parameter LLM from scratch in just 2h! |
| [every-app/open-seo](https://github.com/every-app/open-seo) | Open source alternative to Semrush and Ahrefs |
| [omacom/omarchy](https://github.com/omacom/omarchy) | Beautiful, Modern & Opinionated Linux |
| [google-research/timesfm](https://github.com/google-research/timesfm) | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [omacom/omarchy](https://github.com/omacom/omarchy) | Beautiful, Modern & Opinionated Linux |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Graph-Native Infrastructure for Context and Accountable AI Systems |
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor plugin specification and official plugins |
| [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | Agent workspace built on Cloudflare Workers for creating documents, building apps, and running agents with your company’s context and systems. |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export. |
| [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | Community plugin marketplace for Claude Cowork and Claude Code. Read-only mirror — submit plugins at clau.de/plugin-directory-submission. |
| [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | ⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry. |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills. |
| [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | Prompt as Code | GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 |
| [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag) | The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs |
<!-- END OF MONTHLY_TOP10_REPOS -->
