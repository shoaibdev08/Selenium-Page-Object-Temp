from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest

@pytest.fixture(scope="class")
def SetUp():
    driver=webdriver.Chrome()
    wait= WebDriverWait(driver,10)
    driver.get("https://www.youtube.com/") #Any Web that you want to Open
    driver.maximize_window()
