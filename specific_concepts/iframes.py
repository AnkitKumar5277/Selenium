from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Edge()

# Open a page with iframe
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")

driver.maximize_window()
time.sleep(2)

# STEP 1: Switch to first iframe (main editor iframe)
driver.switch_to.frame("iframeResult")

# STEP 2: Switch to the nested iframe inside
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# STEP 3: Perform action inside iframe
heading = driver.find_element(By.TAG_NAME, "h1").text
print("Text inside iframe:", heading)

# STEP 4: Switch back to main page
driver.switch_to.default_content()

print("Back to main page")
time.sleep(2)

driver.quit()
