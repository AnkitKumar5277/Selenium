from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")  # Example site with AJAX/dynamic elements

# Wait for element (AJAX content) to appear
try:
    # Explicit wait for max 10 seconds
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    print("Element is visible after AJAX call!")
    element.click()
except:
    print("Element not found after waiting!")

driver.quit()

