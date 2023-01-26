import requests
from bs4 import BeautifulSoup
from time import sleep


import service


headers = {}


for page in range(1, 8):
    sleep(3)
    url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for d in data:
        name = d.find('h4', class_='card-title').text.replace('\n', '')
        price = d.find('h5').text
        img = 'https://scrapingclub.com' + d.find('img', class_='card-img-top img-fluid').get('src')
        print(name)
        print(price)
        print(img)
