import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions


@allure.title("Espo CRM Logging In.")
@allure.description("TC02-Positive Case-Verify able to login successfully.")
@pytest.mark.positiveespologin
def test_load_espo_crm_login():
    edge_options = EdgeOptions()
    edge_options.add_argument("--inprivate")
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)

    login_web_element = driver.find_element(By.ID, "btn-login")
    login_web_element.click()
    time.sleep(3)
    assert driver.current_url == "https://demo.us.espocrm.com/?l=en_US"

    time.sleep(5)
    driver.quit()

# pytest -s Locators/task02_Verify_Login_Edge.py --alluredir=./allure-results
# allure serve allure-results

