import os
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
# edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')  # Correct the file extension here
edge_driver_path = ('C:\Program Files (x86)\selinium')
edge_service = Service(edge_driver_path)
edge_options = Options()
edge_options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Edge(service=edge_service, options=edge_options)
browser.get('https://www.example.com')

