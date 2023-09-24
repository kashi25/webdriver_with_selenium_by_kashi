from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://www.google.com')

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('KASHI BHATTARAI')

input("press enter to exit")
driver.quite()
