from selenium import webdriver
import allure
import pytest

@allure.title("verify that tha title of vwo.com is exprected")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)

# pytest Folder_1/test05_Selenium_Commands.py --alluredir=./allure-results

