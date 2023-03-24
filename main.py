import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


url = 'https://www.pepper.ru/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


gradus = soup.findAll('span', class_='cept-vote-temp vote-temp vote-temp--hot')
gradus_list = []
names = soup.findAll('a', class_='cept-tt thread-link linkPlain thread-title--list js-thread-title')
names_list = []
links = (soup.findAll('a', class_='cept-tt thread-link linkPlain thread-title--list js-thread-title'))
links_list = []


def filter(otvet, spisok):
    for i in otvet:
        formatt = (i.text).replace('\n', '')
        formatt = formatt.strip()
        spisok.append(formatt)
        try:
            while True:
                spisok.remove("")
        except ValueError:
            pass


filter(gradus, gradus_list)
filter(names, names_list)
names_list = names_list[:5]

for i in links:
    links_list.append(i['href'])
    links_list = links_list[:5]

for i in range(0, len(names_list)):
    print(f'--------------------\nНазавание - {names_list[i]}\nГрадусы - {gradus_list[i]}\nСсылка на акцию - {links_list[i]}\n--------------------')
