import requests
from bs4 import BeautifulSoup
from time import sleep

import service

list_card_url = []

for page in range(1, 8):
    sleep(1)
    url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for d in data:
        # name = d.find('h4', class_='card-title').text.replace('\n', '')
        # price = d.find('h5').text
        # img = 'https://scrapingclub.com' + d.find('img', class_='card-img-top img-fluid').get('src')
        # print(name)
        # print(price)
        # print(img)
        card_url = 'https://scrapingclub.com' + d.find('a').get('href')
        list_card_url.append(card_url)

for card_url in list_card_url:
    response = requests.get(card_url)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find('div', class_='card mt-4 my-4')

    name = data.find('h3', class_='card-title').text
    price = data.find('h4').text
    text = data.find('p', class_='card-text').text
    url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
    print(name)
    print(price)
    print(text)
    print(url_img)


