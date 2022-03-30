import json
from bs4 import BeautifulSoup as bs

with open("count_of_pages.txt", "r") as file:
    count_of_pages = int(file.read())

all_matches = []

for pages in range(1, count_of_pages + 1, 1):

    with open(f"C:/Users/875l/PycharmProjects/parsing/pages/page_{pages}.html", "r") as file:
        page_api = file.read()

    soup = bs(page_api, "lxml")

    all_matches_date = soup.find_all("div", class_="matche__date")
    all_matches_date = all_matches_date[1:]
    team_icons = soup.find_all("div", class_="icon--container icon--container-23")
    games_href = soup.find_all(class_="matches__link revers")

    teams_name = soup.find_all(class_="d--inline-block d--phone-none")


    for match_in_list in range(0, len(all_matches_date)):

        matches_href = []
        for item in games_href:
            item = str(item)[43:]
            counter = 0
            for letter in item:
                if letter == "\"":
                    item = item[:counter]
                    item = "https://www.cybersport.ru/base" + item
                    matches_href.append(item)
                    break
                counter += 1

        datetime = str(all_matches_date[match_in_list])[130:147]
        if datetime[len(datetime) - 1] == "<": datetime = datetime[:len(datetime) - 1]

        team_name_left = str(teams_name[match_in_list * 2])
        team_name_right = str(teams_name[match_in_list * 2 + 1])

        j = 44
        s = ""
        while team_name_left[j] != "<":
            s += team_name_left[j]
            j += 1
        team_name_left = s

        j = 44
        s = ""
        while team_name_right[j] != "<":
            s += team_name_right[j]
            j += 1
        team_name_right = s

        cur_match = {
            'match_href': matches_href[match_in_list],
            'datetime': datetime,
            'team_name_left': team_name_left,
            'team_name_right': team_name_right
        }

        all_matches.append(cur_match)

        with open("matches.json", "w") as file:
            json.dump(all_matches, file, indent=4, ensure_ascii=False)

        print(datetime, team_name_left, "*VS*", team_name_right)


import get_icons