from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl


# List of months to iterate through
months = ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# Initialize the Chrome driver (ensure the path to chromedriver is correct)
service = Service('chromedriver.exe')  # Adjust path as necessary
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# Initialize ExcelWriter with the desired Excel file name
with pd.ExcelWriter('conference_data.xlsx', engine='openpyxl') as writer:

    for month in months:
        url = f"https://allconferencealert.net/advanced-search.php?keyword=education&month={month}-2024"
        driver.get(url)
        
        time.sleep(5)  
        
        # Initialize lists to hold data for the current month  
        dates = []
        titles = []
        venues = []
        links = []

        # Scrape data for the current month
        date_elements = driver.find_elements(By.XPATH, ".//td[@class='date']")
        for i in date_elements:
            dates.append(i.text)

        title_elements = driver.find_elements(By.XPATH, ".//td[@class='name']")
        for t in title_elements:
            titles.append(t.text)

        venue_elements = driver.find_elements(By.XPATH, ".//td[@class='venue']")
        for v in venue_elements:
            venues.append(v.text)

        link_elements = driver.find_elements(By.XPATH, ".//td[@class='name']/a")
        for l in link_elements:
            links.append(l.get_attribute('href'))
        
        # Create a DataFrame from the lists
        df_month = pd.DataFrame({
            'Date': dates,
            'Title': titles,
            'Venue': venues,
            'Link': links
        })


 # Write the DataFrame to a sheet named after the current month
        df_month.to_excel(writer, sheet_name=month, index=False)

driver.quit()



