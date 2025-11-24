import driver
from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options  # Changed for Edge
from dotenv import load_dotenv
import os

@allure.title("vwo login negative testcase")
@allure.description("tc1 - negative tc - vwo login with invalid creds")
@pytest.mark.negativevwologin
def test_app_vwo_login_edge():
    load_dotenv()
    edge_options = Options()
    edge_options.add_argument('--inprivate')  # Equivalent to --incognito in Edge

    driver = webdriver.Edge(options=edge_options)  # Changed to Edge
    driver.get(os.getenv("URL"))

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    # 2. Find the password and enter the wrong password
    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    # 3. Find the submit button and click
    submit_btn_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_element.click()

    time.sleep(3)

    # Check the error message
    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit()

# pytest -s Locators/test11_Selenium_locators_miniproject_Edge.py --alluredir=./allure-results

