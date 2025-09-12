from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click on the button that triggers alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

time.sleep(2)  # wait for alert to appear

# Switch to alert
alert = driver.switch_to.alert

# Get alert text
print("Alert says:", alert.text)

# Accept the alert (Click OK)
alert.accept()
print("Alert accepted!")

time.sleep(2)

# Example: Handling Confirm Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Confirm says:", alert.text)

# Dismiss the alert (Click Cancel)
alert.dismiss()
print("Alert dismissed!")

time.sleep(2)

# Example: Handling Prompt Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Prompt says:", alert.text)

# Send text to prompt and accept
alert.send_keys("Hello Selenium!")
alert.accept()
print("Prompt accepted with input.")

time.sleep(2)
driver.quit()
