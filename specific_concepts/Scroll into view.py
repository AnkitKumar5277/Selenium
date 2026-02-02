
# ✅ Method 3: Scroll into view
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

button = driver.find_element(By.ID, "submitBtn")

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView();", button)
button.click()



