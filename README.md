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
| [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud) | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, K8s, AI inference, and IAM services. |
| [microsoft/poml](https://github.com/microsoft/poml) | Prompt Orchestration Markup Language |
| [denizsafak/abogen](https://github.com/denizsafak/abogen) | Generate audiobooks from EPUBs, PDFs and text with synchronized captions. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. |
| [umami-software/umami](https://github.com/umami-software/umami) | Umami is a modern, privacy-focused alternative to Google Analytics. |
| [unslothai/notebooks](https://github.com/unslothai/notebooks) | 100+ Fine-tuning LLM Notebooks on Google Colab, Kaggle, and more. |
| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
| [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) | OpenTelemetry Collector |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [apple/embedding-atlas](https://github.com/apple/embedding-atlas) | Embedding Atlas is a tool that provides interactive visualizations for large embeddings. It allows you to visualize, cross-filter, and search embeddings and metadata. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your terminal |
| [ollama/ollama](https://github.com/ollama/ollama) | Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Examples and guides for using the OpenAI API |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | The AI Browser Automation Framework |
| [lvgl/lvgl](https://github.com/lvgl/lvgl) | Embedded graphics library to create beautiful UIs for any MCU, MPU and display type. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [umami-software/umami](https://github.com/umami-software/umami) | Umami is a modern, privacy-focused alternative to Google Analytics. |
| [simstudioai/sim](https://github.com/simstudioai/sim) | Sim is an open-source AI agent workflow builder. Sim Studio's interface is a lightweight, intuitive way to quickly build and deploy LLMs that connect with your favorite tools. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Financial data aggregator for humans and AI agents. |
| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic. |
| [roboflow/supervision](https://github.com/roboflow/supervision) | We write your reusable computer vision tools. 💜 |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |  |
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | A curated list of awesome commands, files, and workflows for Claude Code |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtester |
| [frappe/hrms](https://github.com/frappe/hrms) | Open Source HR and Payroll Software |
<!-- END OF MONTHLY_TOP10_REPOS -->
