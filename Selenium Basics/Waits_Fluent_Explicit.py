import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import *

@allure.title("app.vwo.com implicit wait")
@allure.description("verify that the app.vwo.com is loaded with waits")
def test_negative_app_vwo_com():
    # Create Edge options
    edge_options = Options()
    # edge_options.add_argument("--headless")  # Uncomment if you want headless mode
    driver = webdriver.Edge(options=edge_options)

    driver.get("https://app.vwo.com/#/login")

    # driver.implicitly_wait(5)  # -> 0.01 %

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@123")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description"))
    )

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    driver.quit()
