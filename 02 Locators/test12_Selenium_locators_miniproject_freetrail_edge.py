from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from dotenv import load_dotenv
import os

@allure.title("VWO Login Negative Testcase - Edge")
@allure.description("TC1 - negative TC - VWO login with invalid creds on Edge browser")
@pytest.mark.negativevwologin
def test_app_vwo_login_edge():
    load_dotenv()
    edge_options = Options()
    edge_options.add_argument("--inprivate")
    driver = webdriver.Edge(options=edge_options)
    driver.get(os.getenv("URL"))

    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(5)
    driver.quit()

# pytest -s Locators/test12_Selenium_locators_miniproject_freetrail_edge.py --alluredir=./allure-results
