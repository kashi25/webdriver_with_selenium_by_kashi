# pip install pytest-xdist

from selenium import webdriver

def test_google():
    driver = webdriver.Edge()
    driver.get("https://www.google.com")
    assert"Google" in driver.title
    driver.quite()

def test_amazone():
    driver = webdriver.Edge()
    driver.get("https://www.amazone.com")
    assert"Amazon" in driver.title
    driver.quit()
    
# pytest -n 2 -> to run tests with two parallel workers