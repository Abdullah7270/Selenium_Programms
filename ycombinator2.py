from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Initialize the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")

service = Service('chromedriver.exe')  # Adjust path as necessary
driver = webdriver.Chrome(service=service, options=chrome_options)

# Read the CSV file containing links
df = pd.read_csv('companies.csv')
links = df['Company_Link']

# Initialize a list to store extracted data
extracted_data = []

# Loop through each link and extract data
for i, link in enumerate(links):
    try:
        driver.get(link)
        time.sleep(2)  # Allow time for the page to load

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
            'Link': link
        })

        print(f"[{i + 1}/{len(links)}] Data extracted successfully for {link}")

    except Exception as e:
        print(f"Error processing link {link}: {e}")

# Save the extracted data to a new CSV file
output_df = pd.DataFrame(extracted_data)
output_df.to_csv('extracted_data.csv', index=False)

print("Data extraction completed. Results saved to 'extracted_data.csv'.")

# Close the browser
driver.quit()



