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
| [oumi](https://github.com/oumi-ai/oumi) | Everything you need to build state-of-the-art foundation models, end-to-end. |
| [Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL) | Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. |
| [goose](https://github.com/block/goose) | an open-source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM |
| [docs](https://github.com/github/docs) | The open-source repo for docs.github.com |
| [penpot](https://github.com/penpot/penpot) | Penpot: The open-source design tool for design and code collaboration |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
| [meridian](https://github.com/google/meridian) | Meridian is an MMM framework that enables advertisers to set up and run their own in-house models. |
| [Qwen2.5](https://github.com/QwenLM/Qwen2.5) | Qwen2.5 is the large language model series developed by Qwen team, Alibaba Cloud. |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [Qwen](https://github.com/QwenLM/Qwen) | The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | DeepSeek Coder: Let the Code Write Itself |
| [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) |  |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 2, and other large language models. |
| [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) | DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [onlook](https://github.com/onlook-dev/onlook) | The open source Cursor for Designers. Design directly in your live React app and publish your changes to code. |
| [browser-use](https://github.com/browser-use/browser-use) | Make websites accessible for AI agents |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | LLM inference in C/C++ |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 21 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [browser](https://github.com/lightpanda-io/browser) | Lightpanda: the headless browser designed for AI and automation |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | DeepSeek Coder: Let the Code Write Itself |
| [browser-use](https://github.com/browser-use/browser-use) | Make websites accessible for AI agents |
| [crawl4ai](https://github.com/unclecode/crawl4ai) | 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper |
| [MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | MiniCPM-o 2.6: A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming on Your Phone |
| [khoj](https://github.com/khoj-ai/khoj) | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free. |
| [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | Build your own AI friend |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [maybe](https://github.com/maybe-finance/maybe) | The OS for your personal finances |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」3小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 3 hours! |
<!-- END OF MONTHLY_TOP10_REPOS -->
