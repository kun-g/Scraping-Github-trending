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
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Create Customized Software with Natural Language Ideas |
| [DevToys](https://github.com/veler/DevToys) | A Swiss Army knife for developers. |
| [PowerToys](https://github.com/microsoft/PowerToys) | Windows system utilities to maximize productivity |
| [HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. |
| [BatteryML](https://github.com/microsoft/BatteryML) |  |
| [ntfy](https://github.com/binwiederhier/ntfy) | Send push notifications to your phone or desktop using PUT/POST |
| [astro](https://github.com/withastro/astro) | The all-in-one web framework designed for speed. ⭐️ Star to support our work! |
| [1Panel](https://github.com/1Panel-dev/1Panel) | 🔥 🔥 🔥 现代化、开源的 Linux 服务器运维管理面板。 |
| [webstudio](https://github.com/webstudio-is/webstudio) | 🖌 Webstudio Visual Builder |
| [tango](https://github.com/NetEase/tango) | A source code based low-code builder without private schema. Integrate low-code into your local development workflow seamlessly. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [codellama](https://github.com/facebookresearch/codellama) | Inference code for CodeLlama models |
| [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | PoC for a scalable dev tool that writes entire apps from scratch while the developer oversees the implementation |
| [awesome-english-ebooks](https://github.com/hehonghui/awesome-english-ebooks) | 经济学人(含音频)、纽约客、卫报、连线、大西洋月刊等英语杂志免费下载,支持epub、mobi、pdf格式, 每周更新 |
| [embedchain](https://github.com/embedchain/embedchain) | Framework to easily create LLM powered bots over any dataset. |
| [facefusion](https://github.com/facefusion/facefusion) | Next generation face swapper and enhancer |
| [WizardLM](https://github.com/nlpxucan/WizardLM) | Family of instruction-following LLMs powered by Evol-Instruct: WizardLM, WizardCoder and WizardMath |
| [ntfy](https://github.com/binwiederhier/ntfy) | Send push notifications to your phone or desktop using PUT/POST |
| [OpenCopilot](https://github.com/openchatai/OpenCopilot) | 🤖 🔥 AI Copilot for your own SaaS product. Open source AI sidekick for everyone. |
| [Qwen-VL](https://github.com/QwenLM/Qwen-VL) | The official repo of Qwen-VL (通义千问-VL) chat & pretrained large vision language model proposed by Alibaba Cloud. |
| [graph-of-thoughts](https://github.com/spcl/graph-of-thoughts) | Official Implementation of "Graph of Thoughts: Solving Elaborate Problems with Large Language Models" |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo |
| [awesome-english-ebooks](https://github.com/hehonghui/awesome-english-ebooks) | 经济学人(含音频)、纽约客、卫报、连线、大西洋月刊等英语杂志免费下载,支持epub、mobi、pdf格式, 每周更新 |
| [ToolBench](https://github.com/OpenBMB/ToolBench) | An open platform for training, serving, and evaluating large language model for tool learning. |
| [nextui](https://github.com/nextui-org/nextui) | 🚀 Beautiful, fast and modern React UI library. |
| [Qwen-7B](https://github.com/QwenLM/Qwen-7B) | The official repo of Qwen-7B (通义千问-7B) chat & pretrained large language model proposed by Alibaba Cloud. |
| [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering" |
| [one-api](https://github.com/songquanpeng/one-api) | OpenAI 接口管理 & 分发系统，支持 Azure、Anthropic Claude、Google PaLM 2、智谱 ChatGLM、百度文心一言、讯飞星火认知、阿里通义千问以及 360 智脑，可用于二次分发管理 key，仅单可执行文件，已打包好 Docker 镜像，一键部署，开箱即用. OpenAI key management & redistribution system, using a single API for all LLMs, and features an English UI. |
| [sweep](https://github.com/sweepai/sweep) | Sweep: AI-powered Junior Developer for small features and bug fixes. |
| [Python](https://github.com/TheAlgorithms/Python) | All Algorithms implemented in Python |
| [FastGPT](https://github.com/labring/FastGPT) | FastGPT is a knowledge-based question answering system built on the LLM. It offers out-of-the-box data processing and model invocation capabilities. Moreover, it allows for workflow orchestration through Flow visualization, thereby enabling complex question and answer scenarios! |
<!-- END OF MONTHLY_TOP10_REPOS -->
