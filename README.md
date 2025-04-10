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
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) | Connect Supabase to your AI assistants |
| [datawhalechina/llm-cookbook](https://github.com/datawhalechina/llm-cookbook) | 面向开发者的 LLM 入门教程，吴恩达大模型系列课程中文版 |
| [swiftlang/swift](https://github.com/swiftlang/swift) | The Swift Programming Language |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | "LightRAG: Simple and Fast Retrieval-Augmented Generation" |
| [jiji262/douyin-downloader](https://github.com/jiji262/douyin-downloader) | 抖音批量下载工具，去水印，支持视频、图集、合集、音乐(原声)。免费！免费！免费！ |
| [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf) | Protocol Buffers - Google's data interchange format |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | AI agents & MCPs & workflow automation • (280+ MCP servers for AI agents) • AI automation with MCPs • No-code AI agents with MCPs • AI workflows |
| [girafe-ai/ml-course](https://github.com/girafe-ai/ml-course) | Open Machine Learning course |
| [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) | 提取微信聊天记录，将其导出成HTML、Word、Excel文档永久保存，对聊天记录进行分析生成年度聊天报告，用聊天数据训练专属于个人的AI聊天助手 |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools. |
| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |
| [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) | Free, simple, fast interactive diagrams for any GitHub repository |
| [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | Examples and guides for using the Gemini API |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Build Real-Time Knowledge Graphs for AI Agents |
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Agent S: an open agentic framework that uses computers like a human |
| [Flowseal/zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) |  |
| [koreader/koreader](https://github.com/koreader/koreader) | An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats, running on Cervantes, Kindle, Kobo, PocketBook and Android devices |
| [th-ch/youtube-music](https://github.com/th-ch/youtube-music) | YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader) |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | A collection of MCP servers. |
| [microsoft/typescript-go](https://github.com/microsoft/typescript-go) | Staging repo for development of native port of TypeScript |
| [GuijiAI/HeyGem.ai](https://github.com/GuijiAI/HeyGem.ai) |  |
| [glanceapp/glance](https://github.com/glanceapp/glance) | A self-hosted dashboard that puts all your feeds in one place |
| [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram) | Free, simple, fast interactive diagrams for any GitHub repository |
| [th-ch/youtube-music](https://github.com/th-ch/youtube-music) | YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader) |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | Build effective agents using Model Context Protocol and simple workflow patterns |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |
<!-- END OF MONTHLY_TOP10_REPOS -->
