from selenium import webdriver 
from selenium.webdriver.common.by import By

# creating webdriver object
driver = webdriver.Edge()

# get geeksforgeeks.org
driver.get('https://www.geeksforgeeks.org/')

# get element
element = driver.find_element(By.ID,'gsc-i-id1')
# breakpoint()

