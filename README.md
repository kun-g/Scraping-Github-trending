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
| [qlora](https://github.com/artidoro/qlora) | QLoRA: Efficient Finetuning of Quantized LLMs |
| [gptlink](https://github.com/gptlink/gptlink) | 10分钟搭建自己可免费商用的ChatGPT环境，搭建简单，包含用户，订单，任务，付费等功能 |
| [ts-rust-zig-deez](https://github.com/ThePrimeagen/ts-rust-zig-deez) |  |
| [tinygrad](https://github.com/geohot/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | A GPT-4 AI Tutor Prompt for customizable personalized learning experiences. |
| [devicescript](https://github.com/microsoft/devicescript) | TypeScript for Tiny IoT Devices |
| [sectorc](https://github.com/xorvoid/sectorc) | A C Compiler that fits in the 512 byte boot sector of an x86 machine |
| [InternGPT](https://github.com/OpenGVLab/InternGPT) | InternGPT (iGPT) is an open source demo platform where you can easily showcase your AI models. Now it supports DragGAN, ChatGPT, ImageBind, multimodal chat like GPT-4, SAM, interactive image editing, etc. Try it at igpt.opengvlab.com (支持DragGAN、ChatGPT、ImageBind、SAM的在线Demo系统) |
| [PowerToys](https://github.com/microsoft/PowerToys) | Windows system utilities to maximize productivity |
| [DragGAN](https://github.com/Zeqiang-Lai/DragGAN) | Online Demo and Implementation of DragGAN - "Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold" （DragGAN 全功能实现，在线Demo，本地部署试用，代码、模型已全部开源，支持Windows, macOS, Linux） |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [LaWGPT](https://github.com/pengxiao-song/LaWGPT) | 🎉 Repo for LaWGPT, Chinese-Llama tuned with Chinese Legal knowledge. 基于中文法律知识的大语言模型 |
| [fairseq](https://github.com/facebookresearch/fairseq) | Facebook AI Research Sequence-to-Sequence Toolkit written in Python. |
| [quivr](https://github.com/StanGirard/quivr) | Dump all your files and thoughts into your GenerativeAI Second Brain and chat with it |
| [StableStudio](https://github.com/Stability-AI/StableStudio) | Community interface for generative AI |
| [tinygrad](https://github.com/geohot/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [voice-changer](https://github.com/w-okada/voice-changer) | リアルタイムボイスチェンジャー Realtime Voice Changer |
| [privateGPT](https://github.com/imartinez/privateGPT) | Interact privately with your documents using the power of GPT, 100% privately, no data leaks |
| [VisualGLM-6B](https://github.com/THUDM/VisualGLM-6B) | Chinese and English multimodal conversational language model | 多模态中英双语对话语言模型 |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag & drop UI to build your customized LLM flow using LangchainJS |
| [nlw-12-spacetime-ignite](https://github.com/rocketseat-education/nlw-12-spacetime-ignite) | Aplicação de recordação de memórias desenvolvida no NLW 12 |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [gpt4free](https://github.com/xtekky/gpt4free) | decentralising the Ai Industry, just some language model api's... |
| [AudioGPT](https://github.com/AIGC-Audio/AudioGPT) | AudioGPT: Understanding and Generating Speech, Music, Sound, and Talking Head |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag & drop UI to build your customized LLM flow using LangchainJS |
| [pandora](https://github.com/pengzhile/pandora) | 潘多拉，一个让你呼吸顺畅的ChatGPT。Pandora, a ChatGPT that helps you breathe smoothly. |
| [IF](https://github.com/deep-floyd/IF) |  |
| [fairseq](https://github.com/facebookresearch/fairseq) | Facebook AI Research Sequence-to-Sequence Toolkit written in Python. |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | A GPT-empowered penetration testing tool |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | SoftVC VITS Singing Voice Conversion |
| [yuzu](https://github.com/yuzu-emu/yuzu) | Nintendo Switch Emulator |
<!-- END OF MONTHLY_TOP10_REPOS -->
