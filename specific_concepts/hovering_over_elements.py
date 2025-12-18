from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# 1. Open Chrome browser
driver = webdriver.Chrome()

# 2. Go to the website
driver.get("https://www.example.com")  # replace with your URL
driver.maximize_window()

# 3. Locate the element to hover over
hover_element = driver.find_element(By.ID, "menu")  # replace with your element locator

# 4. Create ActionChains object
actions = ActionChains(driver)

# 5. Perform hover action
actions.move_to_element(hover_element).perform()

# 6. Wait to see the hover effect
time.sleep(3)

# 7. Close browser
driver.quit()
