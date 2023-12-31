from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class GoogleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
        time.sleep(5)
    
    def test_google_images(self):
        image_link = self.driver.find_element(By.LINK_TEXT, 'Images')
        image_link.click()
        assert 'Google Images' in self.driver.title
        time.sleep(5)
    
    def test_google_search(self):
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys('Selenium with python')
        search_box.submit()
        time.sleep(5)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    

        