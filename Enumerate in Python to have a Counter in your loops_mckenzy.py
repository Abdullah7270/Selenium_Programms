from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

counter = 1

mckinsey_names = []
mckinsey_locations = []
mckinsey_job_titles = []
mckinsey_photos = []


url = 'https://www.mckinsey.com/about-us/overview/our-leadership/office-leadership#EEMA'
driver.get(url)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
	driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
	time.sleep(3)
	new_height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
	else:
		last_height = new_height

names = driver.find_elements(By.CSS_SELECTOR, 'h3.headline.-arrow')
for name in names:
	mckinsey_names.append(name.text)
# 	print(f'{counter}.{name.text}')
# 	counter +=1
# print('-------------------------------------------------------------------')

locations = driver.find_elements(By.CSS_SELECTOR, 'span.eyebrow')
for location in locations:
	mckinsey_locations.append(location.text)
# 	print(location.text)
# print('-------------------------------------------------------------------')

job_titles = driver.find_elements(By.CSS_SELECTOR, 'div.description')
for item in job_titles:
	mckinsey_job_titles.append(item.text)
# 	print(item.text)
# print('-------------------------------------------------------------------')

photos = driver.find_elements(By.CSS_SELECTOR, 'div.image a')
for photo in photos:
	mckinsey_photos.append(photo.get_attribute('href'))
# 	print(photo.get_attribute('href'))
#
# print('-----------------------End of page-----------------------')

data_dict = {
	'Name': mckinsey_names,
	'Location': mckinsey_locations,
	'Titles': mckinsey_job_titles,
	'Photo': mckinsey_photos
}

df = pd.DataFrame.from_dict(data_dict, orient='index')
df = df.transpose()
df.to_csv('Mckinsey_Staff_List.csv')
df.to_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\Mckinsey_Staff_List.csv')
df = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\Mckinsey_Staff_List.csv')
print(df)

driver.quit()



