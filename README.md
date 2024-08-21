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
| [authentik](https://github.com/goauthentik/authentik) | The authentication glue you need. |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [es-toolkit](https://github.com/toss/es-toolkit) | A modern JavaScript utility library that's 2-3 times faster and up to 97% smaller—a major upgrade to lodash. |
| [graphrag](https://github.com/microsoft/graphrag) | A modular graph-based Retrieval-Augmented Generation (RAG) system |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design LLMs/AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Bedrock / Azure / Mistral / Perplexity ), Multi-Modals (Vision/TTS) and plugin system. One-click FREE deployment of your private ChatGPT chat application. |
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | Investment Research for Everyone, Everywhere. |
| [tinygrad](https://github.com/tinygrad/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [MinerU](https://github.com/opendatalab/MinerU) | A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。 |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing |
| [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) | Free and Open Source Machine Translation API. Self-hosted, offline capable and easy to setup. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. |
| [MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-V 2.6: A GPT-4V Level MLLM for Single Image, Multi Image and Video on Your Phone |
| [bootstrap](https://github.com/twbs/bootstrap) | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| [EasySpider](https://github.com/NaiboWang/EasySpider) | A visual no-code/code-free web crawler/spider易采集：一个可视化浏览器自动化测试/数据采集/爬虫软件，可以无代码图形化的设计和执行爬虫任务。别名：ServiceWrapper面向Web应用的智能化服务封装系统。 |
| [FlClash](https://github.com/chen08209/FlClash) | A multi-platform proxy client based on ClashMeta,simple and easy to use, open-source and ad-free. |
| [teable](https://github.com/teableio/teable) | ✨ The Next Gen Airtable Alternative: No-Code Postgres |
| [puter](https://github.com/HeyPuter/puter) | 🌐 The Internet OS! Free, Open-Source, and Self-Hostable. |
| [bark](https://github.com/suno-ai/bark) | 🔊 Text-Prompted Generative Audio Model |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [mem0](https://github.com/mem0ai/mem0) | The memory layer for Personalized AI |
| [MinerU](https://github.com/opendatalab/MinerU) | A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。 |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [FlClash](https://github.com/chen08209/FlClash) | A multi-platform proxy client based on ClashMeta,simple and easy to use, open-source and ad-free. |
| [metahuman-stream](https://github.com/lipku/metahuman-stream) | Real time interactive streaming digital human |
| [teable](https://github.com/teableio/teable) | ✨ The Next Gen Airtable Alternative: No-Code Postgres |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. |
| [composio](https://github.com/ComposioHQ/composio) | Composio equips agents with well-crafted tools empowering them to tackle complex tasks |
<!-- END OF MONTHLY_TOP10_REPOS -->
