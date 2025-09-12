from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Edge()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")

# Maximize window
driver.maximize_window()

# Wait for page to load
time.sleep(2)

# The page has an iframe, so first switch to it
driver.switch_to.frame("iframeResult")   # Switch using frame name/id

# Now inside iframe, locate element
text = driver.find_element(By.TAG_NAME, "h1").text
print("Text inside frame:", text)

# Come back to main page (default content)
driver.switch_to.default_content()

print("Back to main page")

# Close browser
time.sleep(2)
driver.quit()
