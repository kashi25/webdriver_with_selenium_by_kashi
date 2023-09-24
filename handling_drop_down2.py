import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get('E:/selinium/env/handeling_drop_down2.html')
wait = WebDriverWait(driver, 15)
menu = wait.until(EC.presence_of_element_located((By.NAME, "menu")))
time.sleep(3)

option = menu.find_element(By.XPATH, "/html/body/form/label[1]/input")
option.click()
time.sleep(3)

option = menu.find_element(By.XPATH, "/html/body/form/label[2]/input")
option.click()
time.sleep(3)


option = menu.find_element(By.XPATH, "/html/body/form/label[3]/input")
option.click()
time.sleep(3)

submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit.click()