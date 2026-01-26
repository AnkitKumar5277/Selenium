import driver
from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

@allure.title("vwo login negative testcase")
@allure.description("tc1 - negative tc - vwo login with invalid creds")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

email_web_element = driver.find_element(By.ID,"login-username")
email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

password_web_element = driver.find_element(By.NAME, "password")
password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

submit_btn_element = driver.find_element(By.ID, "js-login-btn")
submit_btn_element.click()

time.sleep(3)

error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
print(error_message_web_element.text)
assert error_message_web_element.text == os.getenv("error_message_expected")
time.sleep(5)
driver.quit()




