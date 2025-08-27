import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Action P3")
@allure.description("verify click and hold")
def test_verify_actoin_keyboard():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #draggable
    element_to_hold = driver.find_element(By.ID,"draggable")

    # click - normal driver, will find the element and click on it. realease it.realease
    # click and hold - actions chains - click and hold (dont relealse)

    time.sleep(2)

    # keydown
    actions = ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()
    time.sleep(10)
    driver.quit()

# pytest Selenium_Acion_Class/test_Lab_Selenium_Actions_P3.py --alluredir=allure_results
#  allure serve allure_results