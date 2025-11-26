import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("EspoCRM Personal Demo")
@allure.description("tc6 positive case verify that personal demo button is working find")
@pytest.mark.positiveespopersonaldemo

def test_load_espo_crm_personal_demo():
    chrome_options = Options
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espcrm.com/")
    time.sleep(3)

    personal_demo_web_element = driver.find_element(By.PARTIAL_LINK_TEXT,"personal demo")
    personal_demo_web_element.click()

    time.sleep(3)
    expected_url = "https://www.espocrm.com/cloud-registration/?plan=demo"
    assert driver.current_url == expected_url

    time.sleep(3)
    driver.quit()
