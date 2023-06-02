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
| [dm-ticket](https://github.com/ClassmateLin/dm-ticket) | 大麦网自动购票, 支持docker一键部署。Damai automatically purchases tickets, running in docker container. |
| [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [roop](https://github.com/s0md3v/roop) | one-click deepfake (face swap) |
| [CPM-Bee](https://github.com/OpenBMB/CPM-Bee) | 百亿参数的中英文双语基座大模型 |
| [AdGuardian-Term](https://github.com/Lissy93/AdGuardian-Term) | 🛡️ Terminal-based, real-time traffic monitoring and statistics for your AdGuard Home instance |
| [ecoute](https://github.com/SevaSk/ecoute) | Ecoute is a live transcription tool that provides real-time transcripts for both the user's microphone input (You) and the user's speakers output (Speaker) in a textbox. It also generates a suggested response using OpenAI's GPT-3.5 for the user to say based on the live transcription of the conversation. |
| [semantic-search-nextjs-pinecone-langchain-chatgpt](https://github.com/dabit3/semantic-search-nextjs-pinecone-langchain-chatgpt) | Embeds text files into vectors, stores them on Pinecone, and enables semantic search using GPT3 and Langchain in a Next.js UI |
| [plane](https://github.com/makeplane/plane) | 🔥 🔥 🔥 Open Source JIRA, Linear and Height Alternative. Plane helps you track your issues, epics, and product roadmaps in the simplest way possible. |
| [ML-Papers-of-the-Week](https://github.com/dair-ai/ML-Papers-of-the-Week) | 🔥Highlighting the top ML papers every week. |
| [MallChatWeb](https://github.com/Evansy/MallChatWeb) | mallchat的前端项目，是一个既能购物又能聊天的电商系统。以互联网企业级开发规范的要求来实现它，电商该有的购物车，订单，支付，推荐，搜索，拉新，促活，推送，物流，客服，它都必须有。持续更新ing |
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
