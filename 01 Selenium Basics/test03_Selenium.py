import time
from selenium import webdriver
import allure
import pytest

@allure.title("open the app.vwo.com")
@pytest.mark.regression

def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.session_id)

# pytest Folder_1/test03_Selenium.py --alluredir=./allure-results