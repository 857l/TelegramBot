import json
from bs4 import BeautifulSoup as bs

with open("count_of_pages.txt", "r") as file:
    count_of_pages = int(file.read())

all_matches = []

for i in range(1, count_of_pages + 1, 1):

    with open(f"page_{i}.html", "r") as file:
        page_api = file.read()

    soup = bs(page_api, "lxml")

    games_href = soup.find_all(class_="matches__link revers")

    for j in games_href:
        j = str(j)[43:]
        counter = 0
        for t in j:
            if t == "\"":
                j = j[:counter]
                print(j)
                break
            counter += 1