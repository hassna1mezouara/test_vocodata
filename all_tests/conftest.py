import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # <-- ajout
import os




@pytest.fixture(scope="session")
def setup():
    chromedriver_path = r"C:\Users\pc\AppData\Roaming\Microsoft\Windows\Network Shortcuts\test_automatisation2\drivers\chromedriver.exe"
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(180)
    yield driver
    driver.quit()


