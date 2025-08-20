import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

@allure.title("Timeout")
@allure.description("Timeout")
def test_stale_element_exp_demo():
    driver = webdriver.Edge()
    driver.get("https://google.com")

    driver.get("https://google.com")
    try:
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.ID, "submit")))
        print("End of the program")
    except TimeoutException as see:
        # stale element reference
        print(see)
        print("TimeoutException occured!! , 10 Seconds Passed")
    finally:
        driver.quit()