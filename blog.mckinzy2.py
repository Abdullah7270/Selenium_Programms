from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

articles = []
dates = []
descriptions = []
links = []

s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('https://www.mckinsey.com/about-us/new-at-mckinsey-blog')
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

	article_title = driver.find_elements(By.CSS_SELECTOR,'h3.headline')
	for item in article_title:
		articles.append(item.text)
		# print(item.text)
	article_date = driver.find_elements(By.CSS_SELECTOR, 'div.description > time')
	for item in article_date:
		# print(item.text)
		dates.append(item.text)
	description = driver.find_elements(By.CSS_SELECTOR, 'div.description > p')
	for item in description:
		# print(item.text)
		descriptions.append(item.text)
	article_link = driver.find_elements(By.CSS_SELECTOR, 'div.text-wrapper > a')
	for item in article_link:
		print(item.get_attribute('href'))

blog_data = {
	'Title': articles,
	'Date': dates,
	'Description': descriptions,
	'Link': links
}

df = pd.DataFrame.from_dict(blog_data, orient='index')
df = df.transpose()
df.to_csv('blogs_list.csv')
df.to_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\blogs_list.csv')
df = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\blogs_list.csv', encoding='utf-8')
print(df)

driver.close()




















