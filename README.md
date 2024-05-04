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
| [pykan](https://github.com/KindXiaoming/pykan) | Kolmogorov Arnold Networks |
| [PPPwn](https://github.com/TheOfficialFloW/PPPwn) | PPPwn - PlayStation 4 PPPoE RCE |
| [fastfetch](https://github.com/fastfetch-cli/fastfetch) | Like neofetch, but much faster because written mostly in C. |
| [GlaDOS](https://github.com/dnhkng/GlaDOS) | This is the Personality Core for GLaDOS, the first steps towards a real-life implementation of the AI from the Portal series by Valve. |
| [espeak-ng](https://github.com/espeak-ng/espeak-ng) | eSpeak NG is an open source speech synthesizer that supports more than hundred languages and accents. |
| [swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) | A library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. |
| [hydra](https://github.com/hydralauncher/hydra) | Hydra is a game launcher with its own embedded bittorrent client and a self-managed repack scraper. |
| [neofetch](https://github.com/dylanaraps/neofetch) | 🖼️ A command-line system information tool written in bash 3.2+ |
| [FourierKAN](https://github.com/GistNoesis/FourierKAN) |  |
| [MemGPT](https://github.com/cpacker/MemGPT) | Create LLM agents with long-term memory and custom tools 📚🦙 |
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
| [openui](https://github.com/wandb/openui) | OpenUI let's you describe UI using your imagination, then see it rendered live. |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning by MyShell. |
| [heyform](https://github.com/heyform/heyform) | HeyForm is an open-source form builder that allows anyone to create engaging conversational forms for surveys, questionnaires, quizzes, and polls. No coding skills required. |
| [OpenDevin](https://github.com/OpenDevin/OpenDevin) | 🐚 OpenDevin: Code Less, Make More |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | Unify Efficient Fine-Tuning of 100+ LLMs |
| [Llama-Chinese](https://github.com/LlamaFamily/Llama-Chinese) | Llama中文社区，Llama3在线体验和微调模型已开放，实时汇总最新Llama3学习资料，已将所有代码更新适配Llama3，构建最好的中文Llama大模型，完全开源可商用 |
| [valkey](https://github.com/valkey-io/valkey) | A new project to resume development on the formerly open-source Redis project. We're calling it Valkey, since it's a twist on the key-value datastore. |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | Distribute and run LLMs with a single file. |
<!-- END OF MONTHLY_TOP10_REPOS -->
