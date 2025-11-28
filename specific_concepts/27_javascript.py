# ✅ Method 1: Use WebDriverWait (Best way)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Wait until button is clickable, then click
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submitBtn"))
)
button.click()

# ✅ Method 2: Use JavaScript click
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

button = driver.find_element(By.ID, "submitBtn")

# Click using JavaScript
driver.execute_script("arguments[0].click();", button)

# ✅ Method 3: Scroll into view
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

button = driver.find_element(By.ID, "submitBtn")

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView();", button)
button.click()


