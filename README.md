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
| [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to build, manage & run useful autonomous agents quickly and reliably. |
| [gin](https://github.com/gin-gonic/gin) | Gin is a HTTP web framework written in Go (Golang). It features a Martini-like API with much better performance -- up to 40 times faster. If you need smashing performance, get yourself some Gin. |
| [roop](https://github.com/s0md3v/roop) | one-click deepfake (face swap) |
| [milvus](https://github.com/milvus-io/milvus) | A cloud-native vector database, storage for next generation AI applications |
| [Macaw-LLM](https://github.com/lyuchenyang/Macaw-LLM) | Macaw-LLM: Multi-Modal Language Modeling with Image, Video, Audio, and Text Integration |
| [Stable-Diffusion](https://github.com/FurkanGozukara/Stable-Diffusion) | Best Stable Diffusion and AI Tutorials, Guides, News, Tips and Tricks |
| [usehooks](https://github.com/uidotdev/usehooks) | A collection of modern, server-safe React hooks – from the ui.dev team |
| [spacedrive](https://github.com/spacedriveapp/spacedrive) | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. |
| [dm-ticket](https://github.com/ClassmateLin/dm-ticket) | 大麦网自动购票, 支持docker一键部署。Damai automatically purchases tickets, running in docker container. |
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
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag & drop UI to build your customized LLM flow using LangchainJS |
| [pandora](https://github.com/pengzhile/pandora) | 潘多拉，一个让你呼吸顺畅的ChatGPT。Pandora, a ChatGPT that helps you breathe smoothly. |
| [Ryujinx](https://github.com/Ryujinx/Ryujinx) | Experimental Nintendo Switch Emulator written in C# |
| [comprehensive-rust](https://github.com/google/comprehensive-rust) | This is the Rust course used by the Android team at Google. It provides you the material to quickly teach Rust to everyone. |
| [fairseq](https://github.com/facebookresearch/fairseq) | Facebook AI Research Sequence-to-Sequence Toolkit written in Python. |
| [mlc-llm](https://github.com/mlc-ai/mlc-llm) | Enable everyone to develop, optimize and deploy AI models natively on everyone's devices. |
| [tinygrad](https://github.com/geohot/tinygrad) | You like pytorch? You like micrograd? You love tinygrad! ❤️ |
| [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库, 唐宋两朝近一万四千古诗人, 接近5.5万首唐诗加26万宋诗. 两宋时期1564位词人，21050首词。 |
| [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | SoftVC VITS Singing Voice Conversion |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》是一本动画图解、能运行、可提问的数据结构与算法入门书，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Zig 等语言。 |
<!-- END OF MONTHLY_TOP10_REPOS -->
