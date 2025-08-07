import time
from selenium import webdriver
import allure
import pytest

@allure.title("open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https:/app.vwo.com")
    time.sleep(15)

    # pytest C:\Users\Ankit Kumar\PycharmProjects\Focus\Folder_1\test01_Selenium.py --alluredir=./allure-results

    # allure serve allure-results