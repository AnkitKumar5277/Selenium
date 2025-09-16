from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open Chrome
driver = webdriver.Chrome()

# Step 2: Open website
driver.get("https://example.com")

# Example: Suppose the element ID keeps changing like 'login_123', 'login_456' etc.
# Instead of fixed ID, we use "contains" in XPath

try:
    # Step 3: Wait until element is visible (max 10 sec)
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'login')]"))
    )

    # Step 4: Click the button
    login_button.click()

    print("Dynamic element handled successfully!")

except:
    print("Element not found!")

# Step 5: Close browser
driver.quit()
