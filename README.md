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
| [douyin](https://github.com/zyronon/douyin) | Vue3 + Pinia + Vite5 仿抖音，Vue 在移动端的最佳实践 . Imitate TikTok ，Vue Best practices on Mobile |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning by MyShell. |
| [MS-DOS](https://github.com/microsoft/MS-DOS) | The original sources of MS-DOS 1.25, 2.0, and 4.0 for reference purposes |
| [ServiceLogos](https://github.com/SAWARATSUKI/ServiceLogos) | ロゴを可愛く作ろう　節度を持って利用してくださいね🫠 |
| [corenet](https://github.com/apple/corenet) | CoreNet: A library for training deep neural networks |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [IDM-VTON](https://github.com/yisol/IDM-VTON) | IDM-VTON : Improving Diffusion Models for Authentic Virtual Try-on in the Wild |
| [tiny-gpu](https://github.com/adam-maj/tiny-gpu) | A minimal GPU design in Verilog to learn how GPUs work from the ground up |
| [netprobe_lite](https://github.com/plaintextpackets/netprobe_lite) | Simple internet performance tester written in Python |
| [xelis-blockchain](https://github.com/xelis-project/xelis-blockchain) | A private blockDAG using Homomorphic Encryption with Smart Contract support |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [llama3](https://github.com/meta-llama/llama3) | The official Meta Llama 3 GitHub site |
| [chess](https://github.com/code100x/chess) | A multiplayer chess platform |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 3, Mistral, Gemma, and other large language models. |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly WebUI for LLMs (Formerly Ollama WebUI) |
| [unsloth](https://github.com/unslothai/unsloth) | Finetune Llama 3, Mistral & Gemma LLMs 2-5x faster with 80% less memory |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | Unify Efficient Fine-Tuning of 100+ LLMs |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning by MyShell. |
| [codellama](https://github.com/meta-llama/codellama) | Inference code for CodeLlama models |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [llama-recipes](https://github.com/meta-llama/llama-recipes) | Scripts for fine-tuning Meta Llama3 with composable FSDP & PEFT methods to cover single/multi-node GPUs. Supports default & custom datasets for applications such as summarization and Q&A. Supporting a number of candid inference solutions such as HF TGI, VLLM for local or cloud deployment. Demo apps to showcase Meta Llama3 for WhatsApp & Messenger. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [OpenDevin](https://github.com/OpenDevin/OpenDevin) | 🐚 OpenDevin: Code Less, Make More |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [valkey](https://github.com/valkey-io/valkey) | A new project to resume development on the formerly open-source Redis project. We're calling it Valkey, since it's a twist on the key-value datastore. |
| [VoiceCraft](https://github.com/jasonppy/VoiceCraft) | Zero-Shot Speech Editing and Text-to-Speech in the Wild |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 18 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [llm-answer-engine](https://github.com/developersdigest/llm-answer-engine) | Build a Perplexity-Inspired Answer Engine Using Next.js, Groq, Mixtral, Langchain, OpenAI, Brave & Serper |
| [AniPortrait](https://github.com/Zejun-Yang/AniPortrait) | AniPortrait: Audio-Driven Synthesis of Photorealistic Portrait Animation |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
<!-- END OF MONTHLY_TOP10_REPOS -->
