from requests import options
from selenium import webdriver
import pytest
import allure
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

@allure.title("VWO Login Negative Testcase - Edge")
@allure.description("TC1 - Negative TC - VWO login with invalid credentials using Edge browser.")
@pytest.mark.negativevwologin

def test_app_vwo_login_edge():
    load_dotenv()
    edge_options = Options()
    edge_options.add_argument("--inprivate")
    driver = webdriver.Edge(options=edge_options)
    driver.get(os.getenv("URL"))

    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for link in all_links_page:
        print(link.text)
        if "Start a free trial" in link.text:
            link.click()
            break
    time.sleep(5)
    driver.quit()

# pytest -s Locators/test13_Selenium_locators_miniproject_tagName_edge.py --alluredir=./allure-results
