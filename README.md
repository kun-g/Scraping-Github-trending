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
| [clash-nyanpasu](https://github.com/keiko233/clash-nyanpasu) | Clash Nyanpasu! |
| [generative-models](https://github.com/Stability-AI/generative-models) | Generative Models by Stability AI |
| [leetcode](https://github.com/doocs/leetcode) | 🔥LeetCode solutions in any programming language | 多种编程语言实现 LeetCode、《剑指 Offer（第 2 版）》、《程序员面试金典（第 6 版）》题解 |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) | Python - 100天从新手到大师 |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 12 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [starrocks](https://github.com/StarRocks/starrocks) | StarRocks, a Linux Foundation project, is a next-generation sub-second MPP OLAP database for full analytics scenarios, including multi-dimensional analytics, real-time analytics, and ad-hoc queries. InfoWorld’s 2023 BOSSIE Award for best open source software. |
| [uptime-kuma](https://github.com/louislam/uptime-kuma) | A fancy self-hosted monitoring tool |
| [flowty-realtime-lcm-canvas](https://github.com/flowtyone/flowty-realtime-lcm-canvas) | A realtime sketch to image demo using LCM and the gradio library. |
| [GitHub-Chinese-Top-Charts](https://github.com/GrowingGit/GitHub-Chinese-Top-Charts) | 🇨🇳 GitHub中文排行榜，各语言分设「软件 | 资料」榜单，精准定位中文好项目。各取所需，高效学习。 |
| [live](https://github.com/fanmingming/live) | ✯ 一个国内可直连的直播源分享项目 ✯ 🔕 永久免费 直连访问 完整开源 不含广告 完善的台标 直播源支持IPv4/IPv6双栈访问 🔕 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [draw-a-ui](https://github.com/SawyerHood/draw-a-ui) | Draw a mockup and generate html for it |
| [ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
| [OpenAI_Agent_Swarm](https://github.com/daveshap/OpenAI_Agent_Swarm) | HAAS = Hierarchical Autonomous Agent Swarm - "Resistance is futile!" |
| [monaspace](https://github.com/githubnext/monaspace) | An innovative superfamily of fonts for code |
| [opengpts](https://github.com/langchain-ai/opengpts) |  |
| [vimGPT](https://github.com/ishan0102/vimGPT) | Browse the web with GPT-4V and Vimium |
| [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 12 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |
| [tldraw](https://github.com/tldraw/tldraw) | a very good whiteboard |
| [hello-algo](https://github.com/krahets/hello-algo) | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程，支持 Java, C++, Python, Go, JS, TS, C#, Swift, Rust, Dart, Zig 等语言。 |
| [latent-consistency-model](https://github.com/luosiallen/latent-consistency-model) | Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [system-design-101](https://github.com/ByteByteGoHq/system-design-101) | Explain complex systems using visuals and simple terms. Help you prepare for system design interviews. |
| [clash-verge](https://github.com/zzzgydi/clash-verge) | A Clash GUI based on tauri. Supports Windows, macOS and Linux. |
| [sing-box](https://github.com/SagerNet/sing-box) | The universal proxy platform |
| [ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and build TensorRT engines that contain state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that execute those TensorRT engines. |
| [v2rayN](https://github.com/2dust/v2rayN) | A GUI client for Windows, support Xray core and v2fly core and others |
| [tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 💯 Curated coding interview preparation materials for busy software engineers |
| [XAgent](https://github.com/OpenBMB/XAgent) | An Autonomous LLM Agent for Complex Task Solving |
| [MemGPT](https://github.com/cpacker/MemGPT) | Teaching LLMs memory management for unbounded context 📚🦙 |
| [Xray-core](https://github.com/XTLS/Xray-core) | Xray, Penetrates Everything. Also the best v2ray-core, with XTLS support. Fully compatible configuration. |
<!-- END OF MONTHLY_TOP10_REPOS -->
