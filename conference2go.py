from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

titles = []
dates = []
locations = []
links = []

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

for page in range(1,5):
    url = f"https://www.conference2go.com/education/page/{page}/?"
    driver.get(url)
    time.sleep(3)

    title_el = driver.find_elements(By.XPATH, "//a[@class='no-style-link']/h4")
    for i in title_el:
        titles.append(i.text)
        #print(i.text) 

    date_el = driver.find_elements(By.XPATH, "//i[@class='far fa-calendar-check']")
    for d in date_el:
        dates.append(d.text)
        #print(d.text)

    location_el = driver.find_elements(By.XPATH,"//div[@class='event-item-location']/a")
    for location in location_el:
        locations.append(location.text)
        #print(location.text)

    link_el = driver.find_elements(By.XPATH, "//div[@class='post-item-title event-item-title']/a")
    for link in link_el:
        links.append(link.get_attribute('href'))
        #print(link.get_attribute('href'))

driver.quit()

# Create DataFrame with lists    
data = {'Title': titles, 'Date': dates, 'Location': locations, 'Link': links}
df = pd.DataFrame(data)
print(df)