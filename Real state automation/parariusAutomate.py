from selenium import webdriver
# import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.pararius.com/apartments/amsterdam")
try:
    lists = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-list"))
    )
    contents= driver.find_elements(By.TAG_NAME,"section")
    for list in contents:
        title=list.find_element(By.CLASS_NAME,"listing-search-item__link--title").text
        subTitle=list.find_element(By.CLASS_NAME,"listing-search-item__sub-title").text
        price=list.find_element(By.CLASS_NAME,"listing-search-item__price").text
        area=list.find_element(By.CLASS_NAME,"listing-search-item__features").text
        print(title,subTitle,price,area)

finally:    
    driver.quit()
