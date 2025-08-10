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