'''
https://demo.us.espocrm.com/

verify the title and current url

assert and create Allure HTML report also.
'''

from selenium import webdriver
import allure
import  pytest

@allure.title("Verify that the title and current url of espocrm.com is as expected.")
def test_espocrm_sample():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com")
    print(driver.title)
    print(driver.current_url)
    assert driver.title == "EspoCRM Demo"
    assert driver.current_url == "https://demo.us.espocrm.com/"


# pytest -s Jan/ex02_Selenium_Basics/task01_11012025.py --alluredir=./allure-results
# # allure serve allure-results
