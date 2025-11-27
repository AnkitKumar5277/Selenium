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

@allure.title("Actions P3")
@allure.description("verify click and hold")
def test_verify_action_makemytrip():
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--incognito")

    driver=webdriver.Edge(edge_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=5).until(
        EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']"))
    )
    driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()
    time.sleep(2)

    fromCity=driver.find_element(By.ID,"fromCity")
    actions=ActionChains(driver)
    (actions
     .move_to_element(fromCity)
     .click().send_keys("del")
     .perform())

    time.sleep(2)

    actions.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    time.sleep(10)
    driver.quit()
