from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    """the base page class hold the common 
    functionality across the website.Also provide a nice
    wrapper when dealing with selenium function that may
    not be easy to understand"""
    
    def __init__(self, driver):
        """this function is called every time a new object
        of the base class is created"""
        self.driver = driver
        
    def clck(self, by_locator):
        """performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator).click())
    
    def enter_text(self, by_locator, text):
        """performs the text entry of the passed in text, in web
        element whose locator is passed to it"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator).send_keys(text))
    
    def get_title(self,title)->str:
        """return the title of the page"""
        
        WebDriverWait(self.driver, 10).until(EC.title)
        return self.driver.title