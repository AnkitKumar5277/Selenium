from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

@allure.title("vwo login negative testcase")
@allure.description("TC1 - negative TC - vwo login with invalid creds")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    """<a href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage" 
    class="text-link Td(n)" 
    data-qa="bericafeqo">
    Start a free trial
    </a>"""

    # linktext
    # anchor_tag_element=driver.find_element(By.LINK_TEXT,"Start a free trial")
    # anchor_tag_element.click()

# partial text
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(5)
    driver.quit()
