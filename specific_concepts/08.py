from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://demoqa.com/automation-practice-form")
sports_checkbox = driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-1']")
if not sports_checkbox.is_selected():
    sports_checkbox.click()

male_radio = driver.find_element(By.XPATH,"//input[@id='gender-radio-1']")
if not male_radio.is_selected():
    male_radio.click()
time.sleep(100)
driver.quit()

