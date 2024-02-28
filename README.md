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
| [public-apis](https://github.com/public-apis/public-apis) | A collective list of free APIs |
| [PyRIT](https://github.com/Azure/PyRIT) | The Python Risk Identification Tool for generative AI (PyRIT) is an open access automation framework to empower security professionals and machine learning engineers to proactively find risks in their generative AI systems. |
| [WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 该项目可以让你通过订阅的方式使用Cloudflare WARP+，自动获取流量。This project enables you to use Cloudflare WARP+ through subscription, automatically acquiring traffic. |
| [tigerbeetle](https://github.com/tigerbeetle/tigerbeetle) | The distributed financial transactions database designed for mission critical safety and performance. |
| [fuel-core](https://github.com/FuelLabs/fuel-core) | Rust full node implementation of the Fuel v2 protocol. |
| [sway](https://github.com/FuelLabs/sway) | 🌴 Empowering everyone to build reliable and efficient smart contracts. |
| [3x-ui](https://github.com/MHSanaei/3x-ui) | Xray panel supporting multi-protocol multi-user expire day & traffic & ip limit (Vmess & Vless & Trojan & ShadowSocks & Wireguard) |
| [gemma.cpp](https://github.com/google/gemma.cpp) | lightweight, standalone C++ inference engine for Google's Gemma models. |
| [AutoPrompt](https://github.com/Eladlev/AutoPrompt) | A framework for prompt tuning using Intent-based Prompt Calibration |
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
