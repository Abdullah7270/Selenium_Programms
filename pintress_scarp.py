from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time 
import os 

def get_images(var):
    try:
        os.chdir(os.path.join(os.getcwd(), 'images'))
    except:
        pass

    scrollnum = 4  # your choice
    sleeptimer = 1 # your choice


    url = f'https://www.pinterest.com/search/pins/?q={var}'

    # Set up Chrome options to exclude logging
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Initialize the Chrome driver with the specified service and options
    service = Service('C:\\Users\\aalhassan\\Documents\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    # Open the URL in the Chrome browser
    driver.get(url)

    for _ in range(1,scrollnum):
        driver.execute_script("window.scrollTo(1,100000)")
        print('scroll-down')
        time.sleep(sleeptimer)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for link in soup.find_all('img'):
        image_name =link.get('src').strip('https://i.pinimg.com/236x/75/1a/e5/.jpg')
        links = link.get('src')
        
        with open(image_name.replace('/',' ')+ '.png', 'wb') as file:
            im = requests.get(links)
            file.write(im.content)
    
    return
# write names of your choice in get_images("your choice term") 
get_images('wisdom')



