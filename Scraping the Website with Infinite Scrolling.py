import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep

s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver')
driver = webdriver.Chrome(service=s)

countries = []
flags = []

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
	driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
	time.sleep(3)
	new_height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
	else:
		last_height = new_height

country = driver.find_elements(By.CSS_SELECTOR, 'tbody tr td:nth-child(2)')
flag = driver.find_elements(By.XPATH, '//img')
for item_country in country:
	#print(item_country.text)
	countries.append(item_country.text)
for item_flag in flag:
	#print(item_flag.get_attribute('src'))
	flags.append(item_flag.get_attribute('src'))


my_data = {'Country': countries, 'Flag': flags}
df = pd.DataFrame.from_dict(my_data, orient='index')
df= df.transpose()
df.to_csv('country_list.csv')
df.to_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\country_list.csv')
df = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\country_list.csv', encoding='utf-8')
print(df)

driver.close()

