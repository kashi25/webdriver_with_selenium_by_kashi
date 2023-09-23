# first create html file on name of drop_down.html
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("E:/selinium/env/drop_down.html")

time.sleep(5)

dropdown = driver.find_element(By.ID, "dropdown")

select = Select(dropdown)
select.select_by_value("option2")

time.sleep(5)