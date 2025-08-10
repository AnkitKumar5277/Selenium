from selenium import webdriver
import allure
import pytest

@allure.title("verify that tha title of vwo.com is exprected")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "PURA Healthcare Service" in driver.page_source:
        print("Text Found!, test case passed")
    else:
        print("text not found on the page")
        pytest.fail("text not found on the page")

# pytest Folder_1/test05_Selenium_Commands.py --alluredir=./allure-results
