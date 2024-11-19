from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import pandas as pd 
import time 

chrome_options = Options()
chrome_options.add_argument("--disable-logging")  # Disables most logging
chrome_options.add_argument("--log-level=3")      # Reduces logging verbosity


url = 'https://www.ycombinator.com/companies'

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

try:
    driver.get(url)
    time.sleep(5)

    # Scroll to the bottom of the page to load all content
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new content to load
        time.sleep(3)  # Adjust the sleep time as needed

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    links = []
    try:

        company_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@class='_company_86jzd_338']")))
        for link in company_links:
            
            links.append(link.get_attribute('href'))
    except NoSuchElementException:
        print("No elements found. Please check the XPath or website structure.")

    df = pd.DataFrame(links, columns=['Company_Link'])
    df.to_csv('companies.csv', index=False)

finally:
    driver.quit()

