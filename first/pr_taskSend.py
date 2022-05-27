import sqlite3 as sq
import undetected_chromedriver
from bs4 import BeautifulSoup
import time as tiime


def get_Y_time_km(url):
    print('function')
    # if __name__ == '__main__':
    driver = undetected_chromedriver.Chrome()

    # url="https://yandex.ru/maps/213/moscow/?mode=routes&rtext=55.82834407%2C37.770358~55.82247453%2C37.75472859&rtt=auto"
    # # url="https://yandex.ru/maps/213/moscow/?mode=routes&rtext=55.9177074613704%2C38.017335110962~55.75924759999999%2C37.6125459&rtt=auto"
    # url="https://yandex.ru/maps/213/moscow/?mode=routes&rtext=55.91746761%2C38.02953783~55.91746761%2C38.01953783&rtt=auto"

    driver.get(url)
    tiime.sleep(2)
    with open("index.selenium.html", "w") as file:
        file.write(driver.page_source)
    tiime.sleep(2)
    with open('index.selenium.html', 'r') as f:
        contents = f.read()
        # soup = BeautifulSoup(contents, 'lxml')
        html = BeautifulSoup(contents, 'html.parser')

        convert = html.find_all('div', class_='auto-route-snippet-view__route-title-primary')
        find_time = str(convert[0].contents[0])
        c = find_time.split(' ')
        if len(c) == 1:
            if "мин" in c[0]:
                hrs = 0
                mins = int(c[0].replace("мин", ""))
            else:
                mins = 0
                hrs = int(c[0].replace("ч", ""))
        elif len(c) == 2:
            hrs = int(c[0].replace("ч", ""))
            mins = int(c[1].replace("мин", ""))

        convert = html.find_all('div', class_='auto-route-snippet-view__route-subtitle')
        find_km = str(convert[0].contents[0])
        try:
            find_km.index('км')
        except ValueError:
            km = float(find_km.split('м')[0]) / 1000
        else:
            # print(find_km.split('км')[0])
            km = float(find_km.split('км')[0].replace(",", "."))
        min_km = [hrs * 60 + mins, km]
        print(f'otvet:{min_km}')
        return min_km
#
# print('start')
#
# url="https://yandex.ru/maps/213/moscow/?mode=routes&rtext=55.9177074613704%2C38.017335110962~55.75924759999999%2C37.6125459&rtt=auto"
# get_Y_time_km(url)
#
# # url="https://yandex.ru/maps/213/moscow/?mode=routes&rtext=55.917236%2C38.02824~55.75924759999999%2C37.6125459&rtt=auto"
# url="https://yandex.ru/maps/213/moscow/?mode=routes&rtext=55.82834407%2C37.770358~55.82247453%2C37.75472859&rtt=auto"
# get_Y_time_km(url)
#
#
# length = 82
# base = sq.connect('log.db')
# cur = base.cursor()
#
# cur.execute("SELECT lat FROM Coordinates")
# lat = cur.fetchall()
#
# cur.execute("SELECT lng FROM Coordinates")
# lng = cur.fetchall()
#
# cur.execute("SELECT y_url FROM Coordinates")
# y_url = cur.fetchall()
#
# # print(lat)
# # print(lng)
#
# # target = (56.36264842, 38.17546011)
# target = (55.75924759999999, 37.6125459)
# # Y_url_List = [''] * length
# Y_url_List = y_url
#
# # i=0
# # Y_url_List = f'https://yandex.ru/maps/213/moscow/?mode=routes&rtext={lat[i][0]}%2C{lng[i][0]}~{target[0]}%2C{target[1]}&rtt=auto'
# # # print(Y_url_List)
# # print(get_Y_time_km(Y_url_List))
#
# #
# # for i in range(0, 82):
# #     print(i)
# #     if i == 2:
# #         print(i)
#         # Y_url_List[i] = f'https://yandex.ru/maps/213/moscow/?mode=routes&rtext={lat[i][0]}%2C{lng[i][0]}~{target[0]}%2C{target[1]}&rtt=auto'
#         # print(Y_url_List[i])
#         # print(get_Y_time_km(Y_url_List[i]))
#     # elif i == 5:
#     #     Y_url_List[i] = f'https://yandex.ru/maps/213/moscow/?mode=routes&rtext={lat[i][0]}%2C{lng[i][0]}~{target[0]}%2C{target[1]}&rtt=auto'
#     #     print(Y_url_List[i])
#     #     print(get_Y_time_km(Y_url_List[i]))
#     # elif i == 10:
#     #     Y_url_List[i] = f'https://yandex.ru/maps/213/moscow/?mode=routes&rtext={lat[i][0]}%2C{lng[i][0]}~{target[0]}%2C{target[1]}&rtt=auto'
#     #     print(Y_url_List[i])
#     #     print(get_Y_time_km(Y_url_List[i]))
