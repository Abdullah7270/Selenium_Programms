from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

for page in range(1):
    url = f'https://www.goodreads.com/search?page={page}&q=python'

    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)

    # Initialize lists to store data    
    Book_Title= []
    Author_Name= []
    Rating= []
    Cover_Image_URL= []
    
    books = driver.find_elements(By.XPATH, "//a[@class='bookTitle']")
    for book in books:
        #print(book.text)
        Book_Title.append(book.text)
    
    # authors = driver.find_elements(By.XPATH, "//a[@class='authorName']")
    # for author in authors:
    #     #print(author.text)
    #     Author_Name.append(author.text)

    ratings = driver.find_elements(By.XPATH, "//span[@class='minirating']")
    for rating in ratings:
        #print(rating.text)
        Rating.append(rating.text)
    
    covers = driver.find_elements(By.XPATH, "//img[@class='bookCover']")
    for cover in covers:
        #print(cover.get_attribute('src'))
        Cover_Image_URL.append(cover.get_attribute('src'))
    
    # convert the data to Pandas Datafram
    df = pd.DataFrame({'Book':Book_Title, 'Ratings': Rating, 'Images': Cover_Image_URL})
    print(df)
    
    
    driver.quit()

    