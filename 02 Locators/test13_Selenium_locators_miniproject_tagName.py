from requests import options
from selenium import webdriver
import pytest
import allure
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@allure.title("vwo login negative testcase")
@allure.description("TC1 - negative TC - vwo login with invalid creds.")
@pytest.mark.negativevwologin

def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    # < a
    # href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class ="text-link Td(n)"
    # data-qa="bericafeqo" >
    # Start a free trial
    # < / a >
    all_links_page = driver.find_elements(By.TAG_NAME)
    print(len(all_links_page))
    for i in all_links_page:
        print(i.text)
        if "Start a free trial" in i.text:
            i.click()
    time.sleep(5)
    driver.quit()

