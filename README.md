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
| [kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [dokku](https://github.com/dokku/dokku) | A docker-powered PaaS that helps you build and manage the lifecycle of applications |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is an AI collaborative workspace where you achieve more without losing control of your data. The best open source alternative to Notion. |
| [LeetCode-Questions-CompanyWise](https://github.com/krishnadey30/LeetCode-Questions-CompanyWise) | Contains Company Wise Questions sorted based on Frequency and all time |
| [openobserve](https://github.com/openobserve/openobserve) | 🚀 10x easier, 🚀 140x lower storage cost, 🚀 high performance, 🚀 petabyte scale - Elasticsearch/Splunk/Datadog alternative for 🚀 (logs, metrics, traces, RUM, Error tracking, Session replay). |
| [firecrawl](https://github.com/mendableai/firecrawl) | 🔥 Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl and extract with a single API. |
| [coolify](https://github.com/coollabsio/coolify) | An open-source & self-hostable Heroku / Netlify / Vercel alternative. |
| [folly](https://github.com/facebook/folly) | An open-source C++ library developed and used at Facebook. |
| [hackingtool](https://github.com/Z4nzu/hackingtool) | ALL IN ONE Hacking Tool For Hackers |
<!-- END OF DAILY_TOP10_REPOS -->

## 本周TOP10
<!-- START OF WEEKLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [sherlock](https://github.com/sherlock-project/sherlock) | Hunt down social media accounts by username across social networks |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Bring projects, wikis, and teams together with AI. AppFlowy is an AI collaborative workspace where you achieve more without losing control of your data. The best open source alternative to Notion. |
| [nocodb](https://github.com/nocodb/nocodb) | 🔥 🔥 🔥 Open Source Airtable Alternative |
| [firecrawl](https://github.com/mendableai/firecrawl) | 🔥 Turn entire websites into LLM-ready markdown or structured data. Scrape, crawl and extract with a single API. |
| [roop](https://github.com/s0md3v/roop) | one-click face swap |
| [erpnext](https://github.com/frappe/erpnext) | Free and Open Source Enterprise Resource Planning (ERP) |
| [courses](https://github.com/anthropics/courses) | Anthropic's educational courses |
| [coolify](https://github.com/coollabsio/coolify) | An open-source & self-hostable Heroku / Netlify / Vercel alternative. |
| [spotify-downloader](https://github.com/spotDL/spotify-downloader) | Download your Spotify playlists and songs along with album art and metadata (from YouTube if a match is found). |
| [AFFiNE](https://github.com/toeverything/AFFiNE) | There can be more than Notion and Miro. AFFiNE(pronounced [ə‘fain]) is a next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, open-source, customizable and ready to use. |
<!-- END OF WEEKLY_TOP10_REPOS -->

## 本月TOP10
<!-- START OF MONTHLY_TOP10_REPOS -->
| 名字 | 简介 |
| :----: | :----: |
| [MinerU](https://github.com/opendatalab/MinerU) | A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。 |
| [drawdb](https://github.com/drawdb-io/drawdb) | Free, simple, and intuitive online database design tool and SQL generator. |
| [Docker-OSX](https://github.com/sickcodes/Docker-OSX) | Run macOS VM in a Docker! Run near native OSX-KVM in Docker! X11 Forwarding! CI/CD for OS X Security Research! Docker mac Containers. |
| [dice](https://github.com/DiceDB/dice) | A drop-in replacement of Redis with SQL-based realtime reactivity. |
| [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) |  |
| [teable](https://github.com/teableio/teable) | ✨ The Next Gen Airtable Alternative: No-Code Postgres |
| [metahuman-stream](https://github.com/lipku/metahuman-stream) | Real time interactive streaming digital human |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. |
| [authentik](https://github.com/goauthentik/authentik) | The authentication glue you need. |
| [midday](https://github.com/midday-ai/midday) | Run your business smarter 🪄 |
<!-- END OF MONTHLY_TOP10_REPOS -->
