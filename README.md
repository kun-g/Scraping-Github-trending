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
| [yolov9](https://github.com/WongKinYiu/yolov9) | Implementation of paper - YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information |
| [I-S00N](https://github.com/mttaggart/I-S00N) | Anxun Shanghai (I-SOON) Data Dump Translations (PII Redacted) |
| [gemma_pytorch](https://github.com/google/gemma_pytorch) | The official PyTorch implementation of Google's Gemma models |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) | Python - 100天从新手到大师 |
| [OOTDiffusion](https://github.com/levihsu/OOTDiffusion) | Official implementation of OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on |
| [gemma](https://github.com/google-deepmind/gemma) | Open weights LLM from Google DeepMind. |
| [gemma.cpp](https://github.com/google/gemma.cpp) | lightweight, standalone C++ inference engine for Google's Gemma models. |
| [hiddify-next](https://github.com/hiddify/hiddify-next) | Multi-platform auto-proxy client, supporting Sing-box, X-ray, TUIC, Hysteria, Reality, Trojan, SSH etc. It’s an open-source, secure and ad-free. |
| [SoraWebui](https://github.com/SoraWebui/SoraWebui) | SoraWebui is an open-source Sora web client, enabling users to easily create videos from text with OpenAI's Sora model. |
| [NoteWallet](https://github.com/NoteProtocol/NoteWallet) | A Command Line Wallet to Send/Receive BTC and NOTE Tokens |
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
| [zed](https://github.com/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. |
| [maybe](https://github.com/maybe-finance/maybe) | The OS for your personal finances |
| [codellama](https://github.com/facebookresearch/codellama) | Inference code for CodeLlama models |
| [moondream](https://github.com/vikhyat/moondream) | tiny vision language model |
| [palworld-server-docker](https://github.com/thijsvanloef/palworld-server-docker) | A Docker Container to easily run a Palworld dedicated server. |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning) |
| [dspy](https://github.com/stanfordnlp/dspy) | DSPy: The framework for programming—not prompting—foundation models |
| [google-indexing-script](https://github.com/goenning/google-indexing-script) | Script to get your site indexed on Google in less than 48 hours |
| [langgraph](https://github.com/langchain-ai/langgraph) |  |
| [black](https://github.com/psf/black) | The uncompromising Python code formatter |
<!-- END OF MONTHLY_TOP10_REPOS -->
