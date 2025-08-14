import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Alerts")
@allure.description("verify alerts")
def test_alerts_js_alert_normal():
    driver = webdriver.Edge()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModel__close']")))
    model = driver.find_element(By.XPATH, "//span[@class='commonModel__close']")
    model.click()
    time.sleep(5)


def test_alerts_confirm():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_confirm.click()  # Added missing click action
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You clicked: Cancel"
    time.sleep(5)


def test_alerts_prompt():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_prompt.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Ankit")
    alert.accept()

    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You entered: Ankit"  # Fixed assertion to match input
    time.sleep(5)


# pytest -s 05_Alerts/test_modal.py --alluredir=./allure-results

