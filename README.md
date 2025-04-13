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
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.48.x]（Reset Cursor AI MachineID & Auto Sign Up / In & Bypass Higher Token Limit）自动注册 Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 10 Lessons to Get Started Building AI Agents |
| [GuijiAI/HeyGem.ai](https://github.com/GuijiAI/HeyGem.ai) |  |
| [colinhacks/zod](https://github.com/colinhacks/zod) | TypeScript-first schema validation with static type inference |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [crestalnetwork/intentkit](https://github.com/crestalnetwork/intentkit) | An open and fair framework for everyone to build AI agents equipped with powerful skills. Launch your agent, improve the world, your wallet, or both! |
| [funstory-ai/BabelDOC](https://github.com/funstory-ai/BabelDOC) | Yet Another Document Translator |
| [krillinai/KrillinAI](https://github.com/krillinai/KrillinAI) | A video translation and dubbing tool powered by LLMs, offering professional-grade translations and one-click full-process deployment. It can generate content optimized for platforms like YouTube，TikTok, and Shorts. 基于AI大模型的视频翻译和配音工具，专业级翻译，一键部署全流程，可以生成适配抖音，小红书，哔哩哔哩，视频号，TikTok，Youtube Shorts等形态的内容 |
| [minio/minio](https://github.com/minio/minio) | MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.48.x]（Reset Cursor AI MachineID & Auto Sign Up / In & Bypass Higher Token Limit）自动注册 Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [datawhalechina/llm-cookbook](https://github.com/datawhalechina/llm-cookbook) | 面向开发者的 LLM 入门教程，吴恩达大模型系列课程中文版 |
| [jiji262/douyin-downloader](https://github.com/jiji262/douyin-downloader) | 抖音批量下载工具，去水印，支持视频、图集、合集、音乐(原声)。免费！免费！免费！ |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 10 Lessons to Get Started Building AI Agents |
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools. |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [koreader/koreader](https://github.com/koreader/koreader) | An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats, running on Cervantes, Kindle, Kobo, PocketBook and Android devices |
| [elie222/inbox-zero](https://github.com/elie222/inbox-zero) | AI personal assistant for email. Open source app to help you reach inbox zero fast. |
| [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) | The best and simplest free open source web page change detection, website watcher, restock monitor and notification service. Restock Monitor, change detection. Designed for simplicity - Simply monitor which websites had a text change for free. Free Open source web page change detection, Website defacement monitoring, Price change notification |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | A collection of MCP servers. |
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.48.x]（Reset Cursor AI MachineID & Auto Sign Up / In & Bypass Higher Token Limit）自动注册 Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [glanceapp/glance](https://github.com/glanceapp/glance) | A self-hosted dashboard that puts all your feeds in one place |
| [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) | Free, simple, fast interactive diagrams for any GitHub repository |
| [GuijiAI/HeyGem.ai](https://github.com/GuijiAI/HeyGem.ai) |  |
| [th-ch/youtube-music](https://github.com/th-ch/youtube-music) | YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader) |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [ourongxing/newsnow](https://github.com/ourongxing/newsnow) | Elegant reading of real-time and hottest news |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 10 Lessons to Get Started Building AI Agents |
| [DiceDB/dice](https://github.com/DiceDB/dice) | DiceDB is an open-source, fast, reactive, in-memory database optimized for modern hardware. |
<!-- END OF MONTHLY_TOP10_REPOS -->
