from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time

url = 'https://www.ycombinator.com/companies/airbnb'

# Initialize the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")


service = Service('chromedriver.exe')  # Adjust path as necessary
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

try:
    driver.get(url)
    extracted_data = []

    # Example: Extract specific elements (adjust selectors as needed)
    try:
        company_name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='font-extralight']"))
        ).text
    except NoSuchElementException:
        company_name = "N/A"

    try:
        location = driver.find_element(By.XPATH, "//div[@class='flex flex-row justify-between'][3]").text
    except NoSuchElementException:
        location = "N/A"

    try:
        website = driver.find_element(By.XPATH, "//div[@class='group flex flex-row items-center px-3 leading-none text-linkColor ']/a").get_attribute('href')
    except NoSuchElementException:
        website = "N/A"

    # Append the extracted data as a dictionary
    extracted_data.append({
        'Company_Name': company_name,
        'Location': location,
        'Website': website,
    })

    # Save the data into a pandas DataFrame
    df = pd.DataFrame(extracted_data)

    # Save the DataFrame to a CSV file
    df.to_csv('extracted_data.csv', index=False)

    print("Data saved to 'extracted_data.csv'.")
    print(df)

except Exception as e:
    print("Error occurred:", e)

# Close the browser
driver.quit()



