from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import csv

articles = []
dates = []

s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get('https://www.swissinfo.ch/eng/latest-news#')

driver.maximize_window()

titles = driver.find_elements(By.CSS_SELECTOR, 'div.si-teaser__content>h3')
published_date = driver.find_elements(By.CSS_SELECTOR, 'span.show-for-sr')

for item_title in titles:
    articles.append(item_title.text)
for item_date in published_date:
    dates.append(item_date.text)

my_date = {'Article Title': articles, 'Date of Release': dates}
df = pd.DataFrame.from_dict(my_date, orient='index')
df = df.transpose()
df.to_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\swiss_output2.csv')
df = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\swiss_output2.csv', encoding='utf-8')
print(df)

driver.close()
