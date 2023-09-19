import time
from selenium import webdriver


driver = webdriver.Edge()  # Use a capitalized 'E' for Edge
time.sleep(5)
driver.get("https://www.google.com")

assert "google" in driver.title
breakpoint()
