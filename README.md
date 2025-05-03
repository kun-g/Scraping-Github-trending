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
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [aipotheosis-labs/aci](https://github.com/aipotheosis-labs/aci) | ACI.dev is the open source platform that connects your AI agents to 600+ tool integrations with multi-tenant auth, granular permissions, and access through direct function calling or a unified MCP server. |
| [MODSetter/SurfSense](https://github.com/MODSetter/SurfSense) | Open Source Alternative to NotebookLM / Perplexity / Glean, connected to external sources such as search engines (Tavily, Linkup), Slack, Linear, Notion, YouTube, GitHub and more. |
| [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) |  |
| [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | An open source payments switch written in Rust to make payments fast, reliable and affordable |
| [Atmosphere-NX/Atmosphere](https://github.com/Atmosphere-NX/Atmosphere) | Atmosphère is a work-in-progress customized firmware for the Nintendo Switch. |
| [unionlabs/union](https://github.com/unionlabs/union) | The trust-minimized, zero-knowledge bridging protocol, designed for censorship resistance, extremely high security, and usage in decentralized finance. |
| [cloudflare/agents](https://github.com/cloudflare/agents) | Build and deploy AI Agents on Cloudflare |
| [DiceDB/dice](https://github.com/DiceDB/dice) | DiceDB is an open-source, fast, reactive, in-memory database optimized for modern hardware. |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [kortix-ai/suna](https://github.com/kortix-ai/suna) | Suna - Open Source Generalist AI Agent |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Collection of leaked system prompts |
| [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | AI-powered multi-agent builder |
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Agent S: an open agentic framework that uses computers like a human |
| [fastrepl/hyprnote](https://github.com/fastrepl/hyprnote) | AI Notepad for back-to-back meetings. Local-first & Extensible. |
| [lapce/lapce](https://github.com/lapce/lapce) | Lightning-fast and Powerful Code Editor written in Rust |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 21 Lessons, Get Started Building with Generative AI 🔗https://microsoft.github.io/generative-ai-for-beginners/ |
| [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database diagram editor and SQL generator. |
| [bregman-arie/devops-exercises](https://github.com/bregman-arie/devops-exercises) | Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | [Support 0.49.x]（Reset Cursor AI MachineID & Bypass Higher Token Limit） Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | Collection of leaked system prompts |
| [CVEProject/cvelistV5](https://github.com/CVEProject/cvelistV5) | CVE cache of the official CVE List in CVE JSON 5 format |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Build Real-Time Knowledge Graphs for AI Agents |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. |
| [jlowin/fastmcp](https://github.com/jlowin/fastmcp) | 🚀 The fast, Pythonic way to build MCP servers and clients |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. |
| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | real time face swap and one-click video deepfake with only a single image |
| [elie222/inbox-zero](https://github.com/elie222/inbox-zero) | AI personal assistant for email. Open source app to help you reach inbox zero fast. |
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Agent S: an open agentic framework that uses computers like a human |
<!-- END OF MONTHLY_TOP10_REPOS -->
