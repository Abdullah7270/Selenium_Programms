
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
import time

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()



url = 'https://www.fintastico.com/es/fintech-uk/'

driver.get(url)

for _ in range(5):
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

data = []
soup = BeautifulSoup(driver.page_source, 'html.parser')

# titles = soup.find_all('h4')
# for title in titles:
#     print(title.text.strip())

items = soup.find_all('a', class_='card medium')
for item in items:
    item_out = {}

    item_out['Title'] = item.find('h4').text
    item_out['Link'] = 'https://www.fintastico.com/'+ item.attrs['href']
    item_out['Description'] = item.find('p').text

    data.append(item_out)

df = pd.DataFrame(data)
df.to_excel('file.xlsx', index=False)

driver.quit()

    