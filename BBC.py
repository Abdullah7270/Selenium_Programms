from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


s= Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

titles = []
urls = []

for page in range(1, 30):
    driver.get('https://www.bbc.co.uk/search?q=learn+english&d=news_gnl&page='+str(page))

    title = driver.find_elements(By.CSS_SELECTOR, 'div.ssrcss-1f3bvyz-Stack.e1y4nx260 > a > span > p > span')
    url = driver.find_elements(By.CSS_SELECTOR, 'a.ssrcss-1ynlzyd-PromoLink.e1f5wbog0[href]')

    for item_title in title:
        titles.append(item_title.text)
        print(item_title.get_attribute('textContent'))
    for item_url in url:
        urls.append(item_url.get_attribute('href'))
        print(item_url.get_attribute('href'))


my_data = {'Title': titles, 'Links': urls}
df = pd.DataFrame.from_dict(my_data, orient='index')
df= df.transpose()
df.to_csv('bbc_data.csv')
df.to_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\bbc_output2.csv')
df = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\bbc_output2.csv', encoding='utf-8')
print(df)

driver.close()