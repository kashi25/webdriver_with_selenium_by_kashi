from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium')
# search_box.send_keys(Keys.RETURN)

# Corrected XPath for the search button
search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[7]/center/input[1]')
search_button.click()


input("Press enter to exit")
driver.quite()  # Corrected the method name
