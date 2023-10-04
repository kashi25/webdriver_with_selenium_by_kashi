import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Edge()

driver.get("https://www.google.com/")

try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selinium Exception handling")
    time.sleep(3)
    
    search_box.submit()
    search_result = driver.find_element(By.CSS_SELECTOR, 'g')
    time.sleep(3)
    
    for result in search_result:
        title = result.find_element(By.CSS_SELECTOR, ".LC20lb").text
        print(title)

except NoSuchElementException:
    print("element not found on the page")

finally:
    driver.quit()
    
        
        
        