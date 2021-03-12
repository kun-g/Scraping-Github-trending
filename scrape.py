from gtrending import fetch_repos, fetch_developers
from datetime import datetime
import json, click

@click.command()
@click.option("--fetch", default='repos', help="repos or developers")
@click.option("--period", default='daily', help="daily, weekly or monthly")
@click.option("--lang", help="Programming language filter")
def scrape(fetch, period='daily', lang=None):
    if fetch == 'repos':
        func = fetch_repos
    else:
        func = fetch_developers
    time = datetime.now().strftime("%Y%m%d")
    if lang:
        filename = f'{fetch}/{period}/{lang}_{time}.json'
        data = func(since=period, language=lang)
    else:
        filename = f'{fetch}/{period}/{time}.json'
        data = func(since=period)

    with open(filename, 'w') as of:
        json.dump(data, of, indent=4, sort_keys=True)

    if fetch == 'repos':
        update_readme(period, data)

N = 10
def update_readme(period, repos):
    md = "\n| 名字 | 简介 |\n| :----: | :----: |\n"
    for e in repos[:N]:
        name = e.get('name')
        url = e.get('url')
        desc = e.get('description')
        md += f"| [{name}]({url}) | {desc} |\n"

    with open('README.md', 'r') as of:
        readme = of.read()

    marker = f'{period.upper()}_TOP10_REPOS'
    begin = readme.find(f'<!-- START OF {marker} -->')
    begin += len(f'<!-- START OF {marker} -->')
    end = readme.find(f'<!-- END OF {marker} -->')

    readme = readme[:begin] + md + readme[end:]

    with open('README.md', 'w') as of:
        of.write(readme)

if __name__ == '__main__':
    scrape()
