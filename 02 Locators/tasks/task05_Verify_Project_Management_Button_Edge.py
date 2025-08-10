import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import allure
import pytest


@allure.title("EspoCRM project management")
@allure.description("tc 5 positive case verify that project management button is working fine.")
@pytest.mark.positiveEspoProjectManagement
def test_load_espo_crm_project_management():
    edge_options = Options()
    edge_options.add_argument("--inprivate")
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(2)

    project_management_web_element = driver.find_elements(By.TAG_NAME, "a")

    for i in range(len(project_management_web_element)):
        element = driver.find_elements(By.TAG_NAME, "a")[i]
        print(element.text)
        if "Project Management" in element.text:
            element.click()
            break

    time.sleep(3)

    main_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(3)
    expected_url = "https://www.espocrm.com/extensions/project-management/"
    assert driver.current_url == expected_url

    time.sleep(5)
    driver.quit()

# pytest -s Locators/task05_Verify_Project_Management_Button_Edge.py --alluredir=./allure-results
# allure serve allure-results