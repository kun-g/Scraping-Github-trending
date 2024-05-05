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
| [fastfetch](https://github.com/fastfetch-cli/fastfetch) | Like neofetch, but much faster because written mostly in C. |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. |
| [neofetch](https://github.com/dylanaraps/neofetch) | 🖼️ A command-line system information tool written in bash 3.2+ |
| [coolify](https://github.com/coollabsio/coolify) | An open-source & self-hostable Heroku / Netlify / Vercel alternative. |
| [react-spectrum](https://github.com/adobe/react-spectrum) | A collection of libraries and tools that help you build adaptive, accessible, and robust user experiences. |
| [GlaDOS](https://github.com/dnhkng/GlaDOS) | This is the Personality Core for GLaDOS, the first steps towards a real-life implementation of the AI from the Portal series by Valve. |
| [banking](https://github.com/adrianhajdin/banking) | Horizon is a modern banking platform for everyone. |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files |
| [CCTV](https://github.com/IvanGlinkin/CCTV) | Close-Circuit Telegram Vision revolutionizes location tracking with its open-source design and Telegram API integration. Offering precise tracking within 50-100 meters, users can monitor others in real-time for logistics or safety, redefining how we navigate our surroundings |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MS-DOS](https://github.com/microsoft/MS-DOS) | The original sources of MS-DOS 1.25, 2.0, and 4.0 for reference purposes |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning by MyShell. |
| [tiny-gpu](https://github.com/adam-maj/tiny-gpu) | A minimal GPU design in Verilog to learn how GPUs work from the ground up |
| [corenet](https://github.com/apple/corenet) | CoreNet: A library for training deep neural networks |
| [douyin](https://github.com/zyronon/douyin) | Vue3 + Pinia + Vite5 仿抖音，Vue 在移动端的最佳实践 . Imitate TikTok ，Vue Best practices on Mobile |
| [IDM-VTON](https://github.com/yisol/IDM-VTON) | IDM-VTON : Improving Diffusion Models for Authentic Virtual Try-on in the Wild |
| [TagStudio](https://github.com/TagStudioDev/TagStudio) | A file and photo management application and system. |
| [tracecat](https://github.com/TracecatHQ/tracecat) | 😼 The open source alternative to Tines / Splunk SOAR. Build AI-assisted workflows, orchestrate alerts, and close cases fast. |
| [lapce](https://github.com/lapce/lapce) | Lightning-fast and Powerful Code Editor written in Rust |
| [cohere-toolkit](https://github.com/cohere-ai/cohere-toolkit) | Toolkit is a collection of prebuilt components enabling users to quickly build and deploy RAG applications. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [plandex](https://github.com/plandex-ai/plandex) | An AI coding engine for building complex, real-world software with LLMs |
| [coding-interview-university](https://github.com/jwasham/coding-interview-university) | A complete computer science study plan to become a software engineer. |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | Instant voice cloning by MyShell. |
| [ragflow](https://github.com/infiniflow/ragflow) | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding. |
| [dify](https://github.com/langgenius/dify) | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |
| [douyin](https://github.com/zyronon/douyin) | Vue3 + Pinia + Vite5 仿抖音，Vue 在移动端的最佳实践 . Imitate TikTok ，Vue Best practices on Mobile |
| [ore-cli](https://github.com/HardhatChad/ore-cli) |  |
| [Llama-Chinese](https://github.com/LlamaFamily/Llama-Chinese) | Llama中文社区，Llama3在线体验和微调模型已开放，实时汇总最新Llama3学习资料，已将所有代码更新适配Llama3，构建最好的中文Llama大模型，完全开源可商用 |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | Unify Efficient Fine-Tuning of 100+ LLMs |
| [coolify](https://github.com/coollabsio/coolify) | An open-source & self-hostable Heroku / Netlify / Vercel alternative. |
<!-- END OF MONTHLY_TOP10_REPOS -->
