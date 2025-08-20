import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG")
@allure.description("Verify svg")
def test_alerts_js_alert():
    driver = webdriver.Edge()
    driver.get("https://www.flipkart.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("macmini")


    list_svg_elements = driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg_elements[0].click()



    time.sleep(5)
