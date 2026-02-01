import allure
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("actions P3")
@allure.description("verify click and hold")
def test_verify_action_windows():
    edge_options = Options()
    edge_options.add_argument("--inprivate")  # Equivalent of incognito mode in Edge

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle
    print(parent_window)

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Test Case Passed")
            break

# 👉 Ye code verify karta hai ki "Click Here" link pe click karne se new window open hoti hai ya nahi, aur uspe switch karke content check karta hai.
