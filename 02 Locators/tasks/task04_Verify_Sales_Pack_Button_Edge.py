import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


@allure.title("EspoCRM Sales Pack.")
@allure.description("TC04-Positive Case-Verify that sales pack button is working fine.")
@pytest.mark.positiveesposalespack
def test_load_espo_crm_sales_pack():
    edge_options = Options()
    edge_options.add_argument("--inprivate")  # Edge's equivalent to incognito
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)

    sale_pack_web_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Sales")
    sale_pack_web_element.click()

    time.sleep(3)

    main_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(3)
    expected_url = "https://www.espocrm.com/extensions/sales-pack/"
    assert driver.current_url == expected_url

    time.sleep(5)
    driver.quit()

    # pytest -s Locators/task04_Verify_Sales_Pack_Button_Edge.py --alluredir=./allure-results
    # allure serve allure-results