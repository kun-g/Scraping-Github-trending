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
| [aipotheosis-labs/aci](https://github.com/aipotheosis-labs/aci) | ACI.dev is the open source platform that connects your AI agents to 600+ tool integrations with multi-tenant auth, granular permissions, and access through direct function calling or a unified MCP server. |
| [unionlabs/union](https://github.com/unionlabs/union) | The trust-minimized, zero-knowledge bridging protocol, designed for censorship resistance, extremely high security, and usage in decentralized finance. |
| [Atmosphere-NX/Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphère is a work-in-progress customized firmware for the Nintendo Switch. |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) |  |
| [aws/aws-sdk-java-v2](https://github.com/aws/aws-sdk-java-v2) | The official AWS SDK for Java - Version 2 |
| [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | Chris Titus Tech's Windows Utility - Install Programs, Tweaks, Fixes, and Updates |
| [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | Python - 100天从新手到大师 |
| [juanfont/headscale](https://github.com/juanfont/headscale) | An open source, self-hosted implementation of the Tailscale control server |
| [koreader/koreader](https://github.com/koreader/koreader) | An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats, running on Cervantes, Kindle, Kobo, PocketBook and Android devices |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Collection of leaked system prompts |
| [kortix-ai/suna](https://github.com/kortix-ai/suna) | Suna - Open Source Generalist AI Agent |
| [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | AI-powered multi-agent builder |
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Agent S: an open agentic framework that uses computers like a human |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 21 Lessons, Get Started Building with Generative AI 🔗https://microsoft.github.io/generative-ai-for-beginners/ |
| [lapce/lapce](https://github.com/lapce/lapce) | Lightning-fast and Powerful Code Editor written in Rust |
| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | Truly independent web browser |
| [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database diagram editor and SQL generator. |
| [fastrepl/hyprnote](https://github.com/fastrepl/hyprnote) | AI Notepad for back-to-back meetings. Local-first & Extensible. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.49.x]（Reset Cursor AI MachineID & Bypass Higher Token Limit） Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [CVEProject/cvelistV5](https://github.com/CVEProject/cvelistV5) | CVE cache of the official CVE List in CVE JSON 5 format |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Collection of leaked system prompts |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [jlowin/fastmcp](https://github.com/jlowin/fastmcp) | 🚀 The fast, Pythonic way to build MCP servers and clients |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Build Real-Time Knowledge Graphs for AI Agents |
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Agent S: an open agentic framework that uses computers like a human |
| [trycua/cua](https://github.com/trycua/cua) | c/ua is the Docker Container for Computer-Use AI Agents. |
<!-- END OF MONTHLY_TOP10_REPOS -->
