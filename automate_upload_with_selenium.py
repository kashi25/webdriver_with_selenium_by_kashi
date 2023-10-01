import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("E:/selinium/env/upload.html")
time.sleep(3)

file_input = driver.find_element(By.XPATH,"//*[@id='file]")
file_path = "/selinium/env/upload.html"

file_input.send_keys(file_path)

time.sleep(5)

submit_button = driver.find_element(By.XPATH, "/html/body/form/input[2]")
submit_button.click()

breakpoint()

# input("please press enter to quite")
# driver.quit()



