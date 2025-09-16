from selenium import webdriver
import time

# Open browser
driver = webdriver.Chrome()

# Open test page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click button to trigger alert
driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert text
print("Alert says:", alert.text)

# Accept the alert (click OK)
alert.accept()

time.sleep(2)

# Example for confirm alert
driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
print("Confirm says:", alert.text)

# Dismiss alert (click Cancel)
alert.dismiss()

time.sleep(2)

# Example for prompt alert
driver.find_element("xpath", "//button[text()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
print("Prompt says:", alert.text)

# Send text to prompt and accept
alert.send_keys("Hello Selenium")
alert.accept()

time.sleep(2)

# Close browser
driver.quit()
