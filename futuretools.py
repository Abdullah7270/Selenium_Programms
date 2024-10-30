import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url = "https://www.futuretools.io/"

driver.get(url)

# Scroll to the bottom of the page to load all content
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for new content to load
    time.sleep(2)  # Adjust the sleep time as needed

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

tools = []

all_items = soup.find_all('div', class_='tool w-dyn-item w-col w-col-6')

for item in all_items:
    row = {}

    row['Tool Name'] = item.find('a', class_='tool-item-link---new').text
    row['Description'] = item.find('div', class_='tool-item-description-box---new').text

    tools.append(row)

df = pd.DataFrame(tools)
df.to_csv('ai_tools.csv', index=False)

print("Data scraping completed and saved to 'ai_tools.csv'.")