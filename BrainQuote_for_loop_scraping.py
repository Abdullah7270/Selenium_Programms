from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep

quotes = []
authors = []

s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver')
driver = webdriver.Chrome(service=s)

driver.maximize_window()

for page in range(1,17):
    driver.get('https://www.brainyquote.com/topics/chance-quotes_'+str(page))

    quote = driver.find_elements(By.CSS_SELECTOR, 'div.grid-item.qb.clearfix.bqQt div')
    author = driver.find_elements(By.CSS_SELECTOR, '.oncl_a')
    for item_quote in quote:
        #print(item_quote.text)
        quotes.append(item_quote.text)
    for item_author in author:
        authors.append(item_author.text)
        #print(item_author.text)

my_data = {'Quotes': quotes, 'Author': authors}
df = pd.DataFrame.from_dict(my_data, orient='index')
df= df.transpose()
df.to_csv('bbc_data.csv')
df.to_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\Brainquotes.csv')
df = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\Brainquotes.csv', encoding='utf-8')
print(df)

driver.close()