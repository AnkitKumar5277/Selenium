from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()
driver.get("https://example.com/login")  # Replace with your site

# Example: ID keeps changing like "username_123", "username_456"
# Instead of driver.find_element(By.ID, "username_123")

# ✅ Use contains in XPath
username = driver.find_element(By.XPATH, "//input[contains(@id,'username')]")
username.send_keys("my_username")

# ✅ Or use starts-with in XPath
password = driver.find_element(By.XPATH, "//input[starts-with(@id,'pass')]")
password.send_keys("my_password")

# ✅ Or use CSS selector (if class/name is stable)
login_btn = driver.find_element(By.CSS_SELECTOR, "button.login-btn")
login_btn.click()

time.sleep(3)
driver.quit()
