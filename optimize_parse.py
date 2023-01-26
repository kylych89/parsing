import requests
from bs4 import BeautifulSoup
from time import sleep

import service


def get_url():
    for page in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

        for d in data:
            card_url = 'https://scrapingclub.com' + d.find('a').get('href')
            yield card_url


for card_url in get_url():
    response = requests.get(card_url)
    sleep(3)
    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find('div', class_='card mt-4 my-4')

    name = data.find('h3', class_='card-title').text
    price = data.find('h4').text
    text = data.find('p', class_='card-text').text
    url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
    service.save_data(name)
    print(name)
    print(price)
    print(text)
    print(url_img)
