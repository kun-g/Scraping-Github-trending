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
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | 📄 A curated list of awesome .cursorrules files |
| [TypeScript](https://github.com/microsoft/TypeScript) | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [browser-use](https://github.com/browser-use/browser-use) | Make websites accessible for AI agents |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [OptiScaler](https://github.com/cdozdil/OptiScaler) | OptiScaler bridges upscaling/frame gen across GPUs. Supports DLSS2+/XeSS/FSR2+ inputs, replaces native upscalers, enables FSR3 FG on non-FG titles. Supports Nukem mod for DLSSG-to-FSR3 FG. |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [flux](https://github.com/bytedance/flux) | A fast communication-overlapping library for tensor/expert parallelism on GPUs. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [olmocr](https://github.com/allenai/olmocr) | Toolkit for linearizing PDFs for LLM datasets/training |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) |  |
| [hoppscotch](https://github.com/hoppscotch/hoppscotch) | Open source API development ecosystem - https://hoppscotch.io (open-source alternative to Postman, Insomnia) |
| [composio](https://github.com/ComposioHQ/composio) | Composio equip's your AI agents & LLMs with 100+ high-quality integrations via function calling |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | Enjoy the magic of Diffusion models! |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [OmniParser](https://github.com/microsoft/OmniParser) | A simple screen parsing tool towards pure vision based GUI agent |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [unsloth](https://github.com/unslothai/unsloth) | Finetune Llama 3.3, DeepSeek-R1 & Reasoning LLMs 2x faster with 70% less memory! 🦥 |
| [minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [ragflow](https://github.com/infiniflow/ragflow) | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. |
| [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Automate the process of making money online. |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [firecrawl](https://github.com/mendableai/firecrawl) | 🔥 Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl and extract with a single API. |
<!-- END OF MONTHLY_TOP10_REPOS -->
