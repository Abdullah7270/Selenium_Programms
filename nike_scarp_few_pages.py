from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

url = 'https://www.nike.sa/en/mens/shoes'

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get(url)

# Number of pages to scrape
num_pages = 3

for page in range(num_pages):
    print(f"Scraping page {page+1}...")
    
    # Simulate scrolling down
    for _ in range(5):  # Scroll down 5 times, adjust as needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)  # Wait for content to load after scrolling

    soup = BeautifulSoup(driver.page_source, 'html.parser')  # Use driver.page_source to get the HTML content
    products = soup.find_all('div', class_='b-product-tile__body')

    for product in products:
        try:
            name = product.find('a', class_='b-product-tile__name-link js-product-link').text.strip()  # Added strip() to remove leading/trailing whitespace
            desc = product.find('a', class_='b-product-tile__specifications-link js-product-link js-product-tile__subcategory').text.strip()  # Added strip() to remove leading/trailing whitespace
            color = product.find('p', class_='b-product-tile__color').text.strip()  # Added strip() to remove leading/trailing whitespace
            print(f"Name: {name}, Description: {desc}, Color: {color}")
        except Exception as e:
            print(e)

driver.quit()  # Close the WebDriver session
