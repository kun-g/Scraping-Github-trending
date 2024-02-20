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
| [minbpe](https://github.com/karpathy/minbpe) | Minimal, clean, code for the Byte Pair Encoding (BPE) algorithm commonly used in LLM tokenization. |
| [LWM](https://github.com/LargeWorldModel/LWM) |  |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning) |
| [DiT](https://github.com/facebookresearch/DiT) | Official PyTorch Implementation of "Scalable Diffusion Models with Transformers" |
| [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) | A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。 |
| [zksync-era](https://github.com/matter-labs/zksync-era) | zkSync era |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Python, C++, Java, C#, Go, Swift, JS, TS, Dart, Rust, C, Zig 等语言。English edition ongoing |
| [magika](https://github.com/google/magika) | Detect file content types with deep learning |
| [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Stable Diffusion web UI |
| [the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | Master the command line, in one page |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [llrt](https://github.com/awslabs/llrt) | LLRT (Low Latency Runtime) is an experimental, lightweight JavaScript runtime designed to address the growing demand for fast and efficient Serverless applications. |
| [MoneyPrinter](https://github.com/FujiwaraChoki/MoneyPrinter) | Automate Creation of YouTube Shorts using MoviePy. |
| [metavoice-src](https://github.com/metavoiceio/metavoice-src) | Foundational model for human-like, expressive TTS |
| [phidata](https://github.com/phidatahq/phidata) | Build AI Assistants using function calling |
| [pkl](https://github.com/apple/pkl) | A configuration as code language with rich validation and tooling. |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
| [ml-mgie](https://github.com/apple/ml-mgie) |  |
| [rinha-de-backend-2024-q1](https://github.com/zanfranceschi/rinha-de-backend-2024-q1) | Repositório da 2ª edição da Rinha de Backend |
| [conductor](https://github.com/conductor-oss/conductor) | Conductor is a microservices orchestration engine. |
| [Badget](https://github.com/projectx-codehagen/Badget) | Badget aims to simplify financial management with a user-friendly interface and robust backend |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning) |
| [maybe](https://github.com/maybe-finance/maybe) | The OS for your personal finances |
| [spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source Spotify client that doesn't require Premium nor uses Electron! Available for both desktop & mobile! |
| [dspy](https://github.com/stanfordnlp/dspy) | DSPy: The framework for programming—not prompting—foundation models |
| [QAnything](https://github.com/netease-youdao/QAnything) | Question and Answer based on Anything. |
| [alphageometry](https://github.com/google-deepmind/alphageometry) |  |
| [black](https://github.com/psf/black) | The uncompromising Python code formatter |
| [codellama](https://github.com/facebookresearch/codellama) | Inference code for CodeLlama models |
| [memos](https://github.com/usememos/memos) | An open source, lightweight note-taking service. Easily capture and share your great thoughts. |
| [serenity](https://github.com/SerenityOS/serenity) | The Serenity Operating System 🐞 |
<!-- END OF MONTHLY_TOP10_REPOS -->
