from selenium import webdriver
import time
driver = webdriver.Edge()

driver.get('https://www.google.com')

result = driver.execute_script('return 500 + 700;')
print(result)

driver.quit()