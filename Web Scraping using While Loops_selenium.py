from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

authors = []
tags = []
quotes = []

s= Service ('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('https://quotes.toscrape.com/page/1/')
driver.maximize_window()

while True:
    author = driver.find_elements(By.CSS_SELECTOR, 'div.quote small.author')
    tag = driver.find_elements(By.CSS_SELECTOR, 'div.tags')
    quote = driver.find_elements(By.CSS_SELECTOR, 'div.quote span')
    for item_author in author:
        authors.append(item_author.text)
    for item_tag in tag:
        tags.append(item_tag.text)
    for item_quote in quote:
        quotes.append(item_quote.text)

# Use 'Try' to find if there is CSS Selector for "Next Button"
    # click Next Button
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next > a'))).click()
# If there is no more "Next Button" break condition using "Expect"
    except:
        break
my_data = {'Author': authors, 'Tag': tags, 'Quotes': quotes}
df = pd.DataFrame.from_dict(my_data, orient='index')
df = df.transpose()
#df.to_csv('quotes.csv')
df.to_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\quotes.csv')
df = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\quotes.csv', encoding='utf-8')
print(df)

driver.close()





driver.close()