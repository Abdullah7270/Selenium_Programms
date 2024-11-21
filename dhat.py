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


url = 'https://dhat.com/gastroenterologist-near-me?lat=&lng='

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

    # Lists to store scraped data
    business_names = []
    contact_numbers = []
    locations = []

    try:

        all_names = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card__title']/h2")))
        for name in all_names:
            business_names.append(name.text)
        
        all_phones = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card__phone']/a")))
        for phone in all_phones:
            contact_numbers.append(phone.text)

        # Extract locations
        all_locations = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='text card__city-st-zip']"))
        )
        for loc_div in all_locations:
            spans = loc_div.find_elements(By.XPATH, "./span")  # Find all child <span> elements
            full_location = " ".join([span.text.strip() for span in spans])  # Concatenate their text
            locations.append(full_location)


    except NoSuchElementException:
        print("No elements found. Please check the XPath or website structure.")

    # Check if the lengths of the lists match
    if len(business_names) == len(contact_numbers) == len(locations):
        # Create a DataFrame with the structured data
        df = pd.DataFrame({
            'Business Name': business_names,
            'Contact Number': contact_numbers,
            'Location': locations
        })
    df.to_csv('DHAT.csv', index=False)

finally:
    driver.quit()