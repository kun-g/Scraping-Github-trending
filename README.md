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
| [ragflow](https://github.com/infiniflow/ragflow) | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. |
| [terminal](https://github.com/microsoft/terminal) | The new Windows Terminal and the original Windows console host, all in the same place! |
| [chatbox](https://github.com/Bin-Huang/chatbox) | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...) |
| [unsloth](https://github.com/unslothai/unsloth) | Finetune Llama 3.3, DeepSeek-R1 & Reasoning LLMs 2x faster with 70% less memory |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | 🤯 Lobe Chat - an open-source, modern-design AI chat framework. Supports Multi AI Providers( OpenAI / Claude 3 / Gemini / Ollama / Qwen / DeepSeek), Knowledge Base (file upload / knowledge management / RAG ), Multi-Modals (Vision/TTS/Plugins/Artifacts). One-click FREE deployment of your private ChatGPT/ Claude application. |
| [minimind](https://github.com/jingyaogong/minimind) | 🚀🚀 「大模型」50分钟完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 50 min! |
| [sglang](https://github.com/sgl-project/sglang) | SGLang is a fast serving framework for large language models and vision language models. |
| [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | Speech-to-text, text-to-speech, speaker diarization, and VAD using next-gen Kaldi with onnxruntime without Internet connection. Support embedded systems, Android, iOS, HarmonyOS, Raspberry Pi, RISC-V, x86_64 servers, websocket server/client, C/C++, Python, Kotlin, C#, Go, NodeJS, Java, Swift, Dart, JavaScript, Flutter, Object Pascal, Lazarus, Rust |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [oumi](https://github.com/oumi-ai/oumi) | Everything you need to build state-of-the-art foundation models, end-to-end. |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 2, and other large language models. |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [verl](https://github.com/volcengine/verl) | veRL: Volcano Engine Reinforcement Learning for LLM |
| [chatbox](https://github.com/Bin-Huang/chatbox) | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...) |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more. |
| [VideoLingo](https://github.com/Huanshere/VideoLingo) | Netflix-level subtitle cutting, translation, alignment, and even dubbing - one-click fully automated AI video subtitle team | Netflix级字幕切割、翻译、对齐、甚至加上配音，一键全自动视频搬运AI字幕组 |
| [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | LLM based autonomous agent that conducts deep local and web research on any topic and generates a long report with citations. |
| [page-assist](https://github.com/n4ze3m/page-assist) | Use your locally running AI models to assist you in your web browsing |
| [register](https://github.com/is-a-dev/register) | Grab your own sweet-looking '.is-a.dev' subdomain. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | DeepSeek Coder: Let the Code Write Itself |
| [ollama](https://github.com/ollama/ollama) | Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 2, and other large language models. |
| [maybe](https://github.com/maybe-finance/maybe) | The OS for your personal finances |
| [browser-use](https://github.com/browser-use/browser-use) | Make websites accessible for AI agents |
| [open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |
| [tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant |
| [llm-course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. |
| [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) | A robust, efficient, low-latency speech-to-text library with advanced voice activity detection, wake word activation and instant transcription. |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | LLM inference in C/C++ |
| [onlook](https://github.com/onlook-dev/onlook) | The open source Cursor for Designers. Design directly in your live React app and publish your changes to code. |
<!-- END OF MONTHLY_TOP10_REPOS -->
