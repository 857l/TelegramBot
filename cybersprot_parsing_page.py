import requests
from bs4 import BeautifulSoup as bs
import time

general_url = "https://www.cybersport.ru/base/match?disciplines=21&status=future&page=1"
general_api = requests.get(general_url).text
soup = bs(general_api, "lxml")

Pagination = soup.find(class_="page__pagination margin-bottom--20").find_all("a")
count_of_pages = len(Pagination)
if len(Pagination) == 0: count_of_pages = 1

with open("count_of_pages.txt", "w") as file:
    file.write(str(count_of_pages))

for i in range(1, count_of_pages + 1, 1):
    print(i)
    page_url = f"https://www.cybersport.ru/base/match?disciplines=21&status=future&page={i}"
    page_api = requests.get(page_url).text

    with open(f"C:/Users/875l/PycharmProjects/parsing/pages/page_{i}.html", "w") as file:
        file.write(page_api)

import get_info