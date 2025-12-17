from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter username
driver.find_element(By.ID, "username").send_keys("student")

# Enter password
driver.find_element(By.ID, "password").send_keys("Password123")

# Click login button
driver.find_element(By.ID, "submit").click()

# Wait to see result
time.sleep(3)

# Verify login success
if "Logged In Successfully" in driver.page_source:
    print("✅ Login Successful")
else:
    print("❌ Login Failed")

driver.quit()
