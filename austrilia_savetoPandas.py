import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
service = Service('chromedriver.exe')  # Adjust path if necessary
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# URL to scrape
url = "https://www8.austlii.edu.au/cgi-bin/viewtoc/au/legis/wa/consol_act/toc-C.html"
driver.get(url)

# List of tabs to iterate over
tabs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

# Dictionary to store data for each tab
tab_data = {}

try:
    for tab in tabs:
        try:
            # Locate and click on the tab using dynamic XPath
            xpath = f"//a[text()='{tab}']"
            print(f"Processing Tab {tab} with XPath: {xpath}")
            tab_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))

            # Scroll into view (in case the tab is not visible)
            driver.execute_script("arguments[0].scrollIntoView();", tab_element)
            tab_element.click()

            # Wait for the content to load
            WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="page-main"]/div/div/ul/li')))

            # Extract text from all list items within the current tab
            text_elements = driver.find_elements(By.XPATH, '//*[@id="page-main"]/div/div/ul/li')
            extracted_text = [element.text for element in text_elements]
            tab_data[tab] = extracted_text

            print(f"Successfully processed Tab {tab}")

        except Exception as e:
            print(f"Skipping Tab {tab} due to error: {e}")
            continue


finally:
    # Close the browser
    driver.quit()

# Convert the tab data dictionary to a pandas DataFrame
df = pd.DataFrame(dict([(tab, pd.Series(data)) for tab, data in tab_data.items()]))

# Save the DataFrame to an Excel file
output_file = "tab_data.csv"
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")
