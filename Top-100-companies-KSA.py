import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import pandas as pd

s = Service('C:\\Users\\DELL\\PycharmProjects\\MyTests2022\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

url = 'https://www.forbesmiddleeast.com/list/top-100-companies-in-the-ksa'
driver.get(url)

load_more = True
while load_more:
	try:
		driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div[2]/div[4]/div[2]/button').click()
		time.sleep(3)
	except (ElementNotInteractableException, NoSuchElementException):
		load_more = False

xlwriter = pd.ExcelWriter('test_company.xlsx')
table = pd.read_html(driver.page_source)[0]
table.to_excel(xlwriter, engine='xlsxwriter', index=False)

xlwriter.save()

driver.close()



