import allure
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@allure.title("Actions p1")
@allure.description("verify actions p1")
def test_verify_action_keyboard():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/practice.html")
    # //input[@name="firstname"]
    # input[name="firstname"]
    # By.Name -> firstNAME
    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")

    # keydown
    actions = ActionChains(driver=driver)
    (actions
     .key_down(Keys.SHIFT)
     .send_keys_to_element(first_name,"Ankit Kumar")
     .key_up(Keys.SHIFT).perform()
     )

    time.sleep(10)

    driver.quit()
