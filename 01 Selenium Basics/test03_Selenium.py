from selenium import webdriver
import allure
import pytest
import time

def test_katalon_firefox():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    driver.quit()

# pytest main.py --alluredir=reports
# allure serve reports

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
    driver = webdriver.Edge()
    driver.get("https://demo.us.espocrm.com")
    print(driver.title)
    print(driver.current_url)
    assert driver.title == "EspoCRM Demo"
    assert driver.current_url == "https://demo.us.espocrm.com/"


# pytest -s main.py --alluredir=reports
# allure serve reports



