import allure
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions P2")
@allure.description("verify MouseBack")

def test_verify_action_keyboard():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(2)

    # keydown
    action_builders = ActionBuilder(driver=driver)
    action_builders.pointer_action.pointer_up(MouseButton.BACK)
    action_builders.perform()

    time.sleep(10)
    driver.quit()

# pytest Selenium_Acion_Class/test_Lab_Selenium_Actions_P2.py --alluredir=allure_result
# allure serve allure-results