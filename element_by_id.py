from selenium import webdriver

# driver = webdriver.Edge('C:\Program Files (x86)\selinium')
driver = webdriver.Edge()
driver.get('https://wwww.python.org')

search_bar = driver.find_element_by_id('id-search-field')
# locating element using id, name, class and tag
# first_search_bar = driver.find_element_by_class_name('id-class-name')

breakpoint()