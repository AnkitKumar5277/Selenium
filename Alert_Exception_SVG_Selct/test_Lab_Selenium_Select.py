import allure
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("Select")
@allure.description("verify select")
def test_alerts_js_alert():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_html_tag = driver.find_element(By.ID, "dropdown")
    select = Select(select_html_tag)

    select.select_by_visible_text("Option 2")
    select.select_by_visible_text("Option 1")
    select.select_by_index(1)

    time.sleep(5)