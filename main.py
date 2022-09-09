import requests
import lxml
from bs4 import BeautifulSoup


links = ("LP2075700", "LP2075804")

for link in links:

    url = f"https://litemf.com/ru/tracking?tracking_number={link}"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    article_title = soup.find_all("ul", class_="checkpoints")

    for article in article_title:

        last_status = soup.find("div", class_="description").text.strip()


        print(last_status)
