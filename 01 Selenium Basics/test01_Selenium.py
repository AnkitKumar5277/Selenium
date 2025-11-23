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

    # pytest main --alluredir=reports
    # allure serve reports
