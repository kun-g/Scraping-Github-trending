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
| [audiocraft](https://github.com/facebookresearch/audiocraft) | Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning. |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with large language models locally |
| [ToolBench](https://github.com/OpenBMB/ToolBench) | An open platform for training, serving, and evaluating large language model for tool learning. |
| [The-Art-of-Linear-Algebra](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra) | Graphic notes on Gilbert Strang's "Linear Algebra for Everyone" |
| [devops-exercises](https://github.com/bregman-arie/devops-exercises) | Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions |
| [gorilla](https://github.com/ShishirPatil/gorilla) | Gorilla: An API store for LLMs |
| [prompttools](https://github.com/hegelai/prompttools) | Open-source tools for prompt testing and experimentation, with support for both LLMs (e.g. OpenAI, LLaMA) and vector databases (e.g. Chroma, Weaviate). |
| [javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings |
| [OpenUSD](https://github.com/PixarAnimationStudios/OpenUSD) | Universal Scene Description |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [TypeChat](https://github.com/microsoft/TypeChat) | TypeChat is a library that makes it easy to build natural language interfaces using types. |
| [localGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |
| [ollama](https://github.com/jmorganca/ollama) | Get up and running with large language models locally |
| [llama](https://github.com/facebookresearch/llama) | Inference code for LLaMA models |
| [Llama2-Chinese](https://github.com/FlagAlpha/Llama2-Chinese) | Llama中文社区，最好的中文Llama大模型，完全开源可商用 |
| [ShortGPT](https://github.com/RayVentura/ShortGPT) | 🚀🎬 ShortGPT - Experimental AI framework for automated short/video content creation. |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [livewire](https://github.com/livewire/livewire) | A full-stack framework for Laravel that takes the pain out of building dynamic UIs. |
| [llama-recipes](https://github.com/facebookresearch/llama-recipes) | Examples and recipes for Llama 2 model |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Port of Facebook's LLaMA model in C/C++ |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [llama](https://github.com/facebookresearch/llama) | Inference code for LLaMA models |
| [aider](https://github.com/paul-gauthier/aider) | aider is GPT powered coding in your terminal |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | A powerful and modular stable diffusion GUI with a graph/nodes interface. |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [quivr](https://github.com/StanGirard/quivr) | 🧠 Dump all your files and chat with it using your Generative AI Second Brain using LLMs ( GPT 3.5/4, Private, Anthropic, VertexAI ) & Embeddings 🧠 |
| [freegpt-webui](https://github.com/ramonvc/freegpt-webui) | GPT 3.5/4 with a Chat Web UI. No API key required. |
| [h2ogpt](https://github.com/h2oai/h2ogpt) | Private Q&A and summarization of documents+images or chat with local GPT, 100% private, Apache 2.0. Supports LLaMa2, llama.cpp, and more. Demo: https://gpt.h2o.ai/ |
| [unilm](https://github.com/microsoft/unilm) | Large-scale Self-supervised Pre-training Across Tasks, Languages, and Modalities |
| [annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 🧑‍🏫 60 Implementations/tutorials of deep learning papers with side-by-side notes 📝; including transformers (original, xl, switch, feedback, vit, ...), optimizers (adam, adabelief, sophia, ...), gans(cyclegan, stylegan2, ...), 🎮 reinforcement learning (ppo, dqn), capsnet, distillation, ... 🧠 |
| [htmx](https://github.com/bigskysoftware/htmx) | </> htmx - high power tools for HTML |
<!-- END OF MONTHLY_TOP10_REPOS -->
