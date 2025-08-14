import allure
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_js_alert_normal():
    driver = webdriver.Edge()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Mobile Number']")))

    modal = driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    modal.send_keys("9876543210")

    continue_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
    continue_button.click()

    time.sleep(5)
    driver.quit()


def test_alerts_confirm():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You clicked: Cancel"

    time.sleep(5)
    driver.quit()


def test_alerts_prompt():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_prompt.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Pramod")
    alert.accept()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You entered: Pramod"

    time.sleep(5)
    driver.quit()

# pytest -s 05_Alerts/test_makemytrip.py --alluredir=./allure-results
