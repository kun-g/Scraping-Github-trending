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
| [gpt-crawler](https://github.com/BuilderIO/gpt-crawler) | Crawl a site to generate knowledge files to create your own custom GPT from a URL |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating |
| [frigate](https://github.com/blakeblackshear/frigate) | NVR with realtime local object detection for IP cameras |
| [screenshot-to-code](https://github.com/abi/screenshot-to-code) | Drop in a screenshot and convert it to clean HTML/Tailwind/JS code |
| [PowerShell](https://github.com/PowerShell/PowerShell) | PowerShell for every system! |
| [spring-reading](https://github.com/xuchengsheng/spring-reading) | 涵盖了 Spring 框架的核心概念和关键功能，包括控制反转（IOC）容器的使用，面向切面编程（AOP）的原理与实践，事务管理的方式与实现，Spring MVC 的流程与控制器工作机制，以及 Spring 中数据访问、安全、Boot 自动配置等方面的深入研究。此外，它还包含了 Spring 事件机制的应用、高级主题如缓存抽象和响应式编程，以及对 Spring 源码的编程风格与设计模式的深入探讨。 |
| [uneebee](https://github.com/zoonk/uneebee) | Platform for creating interactive courses. |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | AppFlowy is an open-source alternative to Notion. You are in charge of your data and customizations. Built with Flutter and Rust. |
| [FriendsDontLetFriends](https://github.com/cxli233/FriendsDontLetFriends) | Friends don't let friends make certain types of data visualization - What are they and why are they bad. |
| [StyleTTS2](https://github.com/yl4579/StyleTTS2) | StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models |
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
