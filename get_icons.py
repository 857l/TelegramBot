import requests
import json
from bs4 import BeautifulSoup as bs

with open("count_of_pages.txt", "r") as file:
    count_of_pages = int(file.read())

with open("matches.json", "r") as file:
    all_matches = json.load(file)

icons = []

c = 0
for pages in range(1, count_of_pages, 1):

    with open(f"C:/Users/875l/PycharmProjects/parsing/pages/page_{pages}.html", "r") as file:
        page_api = file.read()

    soup = bs(page_api, "lxml")

    team_icons = soup.find_all("div", class_="icon--container icon--container-23")

    for photo in team_icons:

        team_name_left = all_matches[c // 2]['team_name_left']
        team_name_right = all_matches[c // 2]['team_name_right']

        photo = str(photo)

        if len(photo) == 303:
            print(photo[176:291])
            icons.append(photo[176:291])

            img = requests.get(photo[176:291])

            if c % 2 == 0:
                img_option = open("C:/Users/875l/PycharmProjects/parsing/icons/" + team_name_left + '.jpg', "wb")
                print(team_name_left)
            else:
                img_option = open("C:/Users/875l/PycharmProjects/parsing/icons/" + team_name_right + '.jpg', "wb")
                print(team_name_right)

            img_option.write(img.content)
            img_option.close()
            c += 1

        elif len(photo) == 301:
            print(photo[174:288])
            icons.append(photo[174:288])

            img = requests.get(photo[174:288])

            if c % 2 == 0:
                img_option = open("C:/Users/875l/PycharmProjects/parsing/icons/" + team_name_left + '.jpg', "wb")
                print(team_name_left)
            else:
                img_option = open("C:/Users/875l/PycharmProjects/parsing/icons/" + team_name_right + '.jpg', "wb")
                print(team_name_right)

            img_option.write(img.content)
            img_option.close()
            c += 1

        else:
            img = "https://falcon-esports.ru/img/disciplines/dota2.png"
            img = requests.get(img)

            if c % 2 == 0:
                img_option = open("C:/Users/875l/PycharmProjects/parsing/icons/" + team_name_left + '.jpg', "wb")
                print("##No Photo##")
                print(team_name_left)
            else:
                img_option = open("C:/Users/875l/PycharmProjects/parsing/icons/" + team_name_right + '.jpg', "wb")
                print("##No Photo##")
                print(team_name_right)

            img_option.write(img.content)
            img_option.close()
            c += 1


with open("icons.json", "w") as file:
    json.dump(icons, file, indent=4, ensure_ascii=False)
