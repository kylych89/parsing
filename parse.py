import requests
from bs4 import BeautifulSoup as bs
import service

# URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
# r = requests.get(URL_TEMPLATE)
#
# soup = bs(r.text, "html.parser")
# ht = int(soup.find('span', class_='text-default').text.split()[-1])
#
# tx = ''
# for page in range(1, 5):
#     r = requests.get(f'https://www.work.ua/ru/jobs-odesa/?page={page}')
#     soup = bs(r.text, "html.parser")
#     vacancies_names = soup.find_all('h2')
#
#     for name in vacancies_names:
#         tx += name.text
#
# service.save_data(tx)


TEMPLATE_URL = 'https://www.tazabek.kg/news:1855038/?from=tazabek&place=newsload'

req = requests.get(TEMPLATE_URL)

soup = bs(req.text, 'html.parser')
title1 = soup.find('h2')


body1 = soup.find('div', class_='text')


all_text = f'Тема: {title1.text}\n{body1.text}'

service.save_data(all_text)
