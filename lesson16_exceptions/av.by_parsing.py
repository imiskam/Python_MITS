from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

data = []

for pg in range(1, 4):
    url = f"https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=5965&page={pg}"
    response = requests.get(url, verify=False)
    sleep(3)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')

    cars = soup.findAll('div', class_="listing-item")

    for car in cars:
        link = "https://cars.av.by/bmw/x7" + car.find('a', class_="listing-item__link").get('href')
        name_car = car.find('a', class_="listing-item__link").text
        cost_rub = car.find('div', class_="listing-item__price").text
        cost_usd = car.find('div', class_="listing-item__priceusd").text

        data.append([link, name_car, cost_rub, cost_usd])
        print(len(data))

        head = ['link', 'name_car', 'costmost_rub', 'costmost_usd']
        df = pd.DataFrame(data, columns=head)
        df.to_csv('data.csv', sep=';', encoding='UTF-8')
