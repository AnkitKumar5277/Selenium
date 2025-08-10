# import allure
# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# @allure.title("Espo CRM Login Page.")
# @allure.description("TC01-Positive Case-Verify that title and URL is appearing correctly.")
# @pytest.mark.positiveespologinpage
#
# def test_load_espo_crm():
#     chrome_options = Options()
#     chrome_options.add_argument("--incognito")
#     chrome_options.add_argument("--start-maximized")
#
#     driver = webdriver.Chrome(chrome_options)
#     driver.get("https://demo.us.espocrm.com/")
#     print(driver.title)
#
#     assert driver.title == "EspoCRM Demo"
#     assert driver.current_url == ("https://demo.us.espocrm.com/")
#
#     time.sleep(5)
#     driver.quit()


import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options  # Edge ke liye change


@allure.title("Espo CRM Login Page.")
@allure.description("TC01-Positive Case-Verify that title and URL is appearing correctly.")
@pytest.mark.positiveespologinpage
def test_load_espo_crm():
    edge_options = Options()  # Chrome ki jagah Edge Options
    edge_options.add_argument("--inprivate")  # Incognito ke liye Edge mein --inprivate
    edge_options.add_argument("--start-maximized")  # Full-screen browser

    driver = webdriver.Edge(options=edge_options)  # Chrome ki jagah Edge
    driver.get("https://demo.us.espocrm.com/")
    print(driver.title)

    assert driver.title == "EspoCRM Demo"
    assert driver.current_url == "https://demo.us.espocrm.com/"

    time.sleep(5)
    driver.quit()