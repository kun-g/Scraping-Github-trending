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
| [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | An AI Hedge Fund Team |
| [composio](https://github.com/ComposioHQ/composio) | Composio equip's your AI agents & LLMs with 100+ high-quality integrations via function calling |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 21 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source Spotify client that doesn't require Premium nor uses Electron! Available for both desktop & mobile! |
| [rayhunter](https://github.com/EFForg/rayhunter) | Rust tool to detect cell site simulators on an orbic mobile hotspot |
| [grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) | gRPC to JSON proxy generator following the gRPC HTTP spec |
| [union](https://github.com/unionlabs/union) | The trust-minimized, zero-knowledge bridging protocol, designed for censorship resistance, extremely high security, and usage in decentralized finance. |
| [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) |  |
| [SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | Multiplayer at the speed of light |
| [PowerToys](https://github.com/microsoft/PowerToys) | Windows system utilities to maximize productivity |
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
