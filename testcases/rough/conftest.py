# Under the Tests directory we will create conftest.py – 
# for creating fixture (setup and tear down method) that will be used commonly for all test classes
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def setup():
    global driver 
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
   
    yield
    driver.close()

    