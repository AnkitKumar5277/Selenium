from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

def test_katalon_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # 1- Find the element the anchor tag
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    driver.quit()

   # pytest -s Locators/test09_Selenium_locators.py --alluredir=./allure-results
