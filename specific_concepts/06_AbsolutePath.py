from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open a demo website
driver.get("https://www.google.com")

# Example 1: Find element by absolute XPath (not recommended, too long)
search_box1 = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search_box1.send_keys("Selenium XPath Example")

time.sleep(2)

# Example 2: Find element by attribute (better way)
search_box2 = driver.find_element(By.XPATH, "//textarea[@name='q']")
search_box2.clear()
search_box2.send_keys("Learn XPath in Selenium")

time.sleep(2)

# Example 3: Find element using text()
search_button = driver.find_element(By.XPATH, "//input[@value='Google Search']")
search_button.click()

time.sleep(5)

driver.quit()
