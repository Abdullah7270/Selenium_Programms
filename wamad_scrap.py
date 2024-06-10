from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
import time

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

data = []

for page in range(1,15):
    url = f'https://www.wamda.com/media?page={page}'
    driver.get(url)
    time.sleep(3)


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    items = soup.find_all('div', class_='c-media__content')           

    for item in items:
        item_out = {}

        item_out['Title'] = item.find('h2', class_='c-media__title').text
        item_out['Location'] = item.find('span', class_='c-tag').text
        item_out['Description'] = item.find('p', class_='c-media__teaser').text
        item_out['Author'] = item.find('p', class_='c-media__footer').text
        data.append(item_out)

df = pd.DataFrame(data)
df.to_excel('articles_titles.xlsx', index=False)
