import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


@allure.title("Practicing Xpath")
@allure.description("TC1 - Exploring Xpath")
def test_xpath_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Make')]")
    make_app_btn.click()

    # text() -> exact match
    # partial text() - contains
    # //a[contains(text(),'Make Appointment')]
    # //a[contains(text(),'Appointment')]
    # //a[contains(text(),'Make')]
    # //a[contains(text(),'Ma')]
    # //a[contains(text(),'App')] - this may fail if there 1 or more a tag with app
    # <a rel="https:/google.com"/>
    # //a[starts-with(text(),'Make')]
    time.sleep(2)
    driver.quit()

    # pytest -s 03_Xpath/task02_edge.py --alluredir=./allure-results
    # allure serve allure-results