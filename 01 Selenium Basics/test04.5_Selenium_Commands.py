from selenium import webdriver
import allure
import pytest

@allure.title("verify that the title of vwo.com is expected")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"

# pytest main --alluredir=reports
# allure serve reports
