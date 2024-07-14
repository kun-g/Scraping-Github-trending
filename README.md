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
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [tiptap](https://github.com/ueberdosis/tiptap) | The headless rich text editor framework for web artisans. |
| [tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [ragflow](https://github.com/infiniflow/ragflow) | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. |
| [grpc-go](https://github.com/grpc/grpc-go) | The Go language implementation of gRPC. HTTP/2 based RPC |
| [NewPipeExtractor](https://github.com/TeamNewPipe/NewPipeExtractor) | NewPipe's core library for extracting data from streaming sites |
| [SmartTube](https://github.com/yuliskov/SmartTube) | SmartTube - an advanced player for set-top boxes and tvs running Android OS |
| [optimism](https://github.com/ethereum-optimism/optimism) | Optimism is Ethereum, scaled. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Awesome multilingual OCR toolkits based on PaddlePaddle (practical ultra lightweight OCR system, support 80+ languages recognition, provide data annotation and synthesis tools, support training and deployment among server, mobile, embedded and IoT devices) |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [graphrag](https://github.com/microsoft/graphrag) | A modular graph-based Retrieval-Augmented Generation (RAG) system |
| [storm](https://github.com/stanford-oval/storm) | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
| [graphrag-accelerator](https://github.com/Azure-Samples/graphrag-accelerator) | One-click deploy of a Knowledge Graph powered RAG (GraphRAG) in Azure |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [litgpt](https://github.com/Lightning-AI/litgpt) | 20+ high-performance LLMs with recipes to pretrain, finetune and deploy at scale. |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Brand new TTS solution |
| [optimism](https://github.com/ethereum-optimism/optimism) | Optimism is Ethereum, scaled. |
| [puter](https://github.com/HeyPuter/puter) | 🌐 The Internet OS! Free, Open-Source, and Self-Hostable. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [ImHex](https://github.com/WerWolv/ImHex) | 🔍 A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM. |
| [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 30 days of Python programming challenge is a step-by-step guide to learn the Python programming language in 30 days. This challenge may take more than100 days, follow your own pace. These videos may help too: https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [HowToCook](https://github.com/Anduin2017/HowToCook) | 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only). |
| [mindsdb](https://github.com/mindsdb/mindsdb) | The platform for building AI from enterprise data |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | Open-Sora: Democratizing Efficient Video Production for All |
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [fish-speech](https://github.com/fishaudio/fish-speech) | Brand new TTS solution |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Master programming by recreating your favorite technologies from scratch. |
| [free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 📚 Freely available programming books |
<!-- END OF MONTHLY_TOP10_REPOS -->
