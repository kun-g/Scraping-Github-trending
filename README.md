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
| [gemma_pytorch](https://github.com/google/gemma_pytorch) | The official PyTorch implementation of Google's Gemma models |
| [gemma.cpp](https://github.com/google/gemma.cpp) | lightweight, standalone C++ inference engine for Google's Gemma models. |
| [SoraWebui](https://github.com/SoraWebui/SoraWebui) | SoraWebui is an open-source Sora web client, enabling users to easily create videos from text with OpenAI's Sora model. |
| [zed](https://github.com/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. |
| [react-strict-dom](https://github.com/facebook/react-strict-dom) | React Strict DOM (RSD) is a subset of React DOM, imperative DOM, and CSS that supports web and native targets |
| [sorafm](https://github.com/all-in-aigc/sorafm) | Sora AI Video Generator by Sora.FM |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) | Python - 100天从新手到大师 |
| [OOTDiffusion](https://github.com/levihsu/OOTDiffusion) | Official implementation of OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on |
| [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Automate the process of making money online. |
| [smart-resident-guard](https://github.com/mtkarimi/smart-resident-guard) |  |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [magika](https://github.com/google/magika) | Detect file content types with deep learning |
| [sherlock](https://github.com/sherlock-project/sherlock) | 🔎 Hunt down social media accounts by username across social networks |
| [uv](https://github.com/astral-sh/uv) | An extremely fast Python package installer and resolver, written in Rust. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design ChatGPT/LLMs UI/Framework. Supports speech-synthesis, multi-modal, and extensible plugin system. One-click FREE deployment of your private ChatGPT/Gemini/Ollama chat application. |
| [gptscript](https://github.com/gptscript-ai/gptscript) | Develop LLM Apps in Natural Language |
| [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM 等语言模型的本地知识库问答 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM) QA app with langchain |
| [gopeed](https://github.com/GopeedLab/gopeed) | A modern download manager that supports all platforms. Built with Golang and Flutter. |
| [provisions-data](https://github.com/starknet-io/provisions-data) | Lists of eligible identities for Starknet provisions. |
| [StableCascade](https://github.com/Stability-AI/StableCascade) | Official Code for Stable Cascade |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
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
