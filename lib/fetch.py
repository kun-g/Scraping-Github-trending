import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com/trending?since="
def fetch_repos(since="daily"):
    url = f"{BASE_URL}{since}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    repo_list = soup.find_all("article", class_="Box-row")

    trending_repos = []
    for repo in repo_list:
        title_tag = repo.h2.a
        repo_name = title_tag.get_text(strip=True).replace('\n', '').replace(' ', '')
        repo_url = f"https://github.com{title_tag['href']}"
        description_tag = repo.find("p", class_="col-9")
        description = description_tag.get_text(strip=True) if description_tag else ""
        language_tag = repo.find("span", itemprop="programmingLanguage")
        language = language_tag.get_text(strip=True) if language_tag else "N/A"
        stars_tag = repo.find("a", href=lambda x: x and x.endswith("/stargazers"))
        stars = stars_tag.get_text(strip=True) if stars_tag else "0"

        trending_repos.append({
            "name": repo_name,
            "url": repo_url,
            "description": description,
            "language": language,
            "stars": stars
        })

    return trending_repos