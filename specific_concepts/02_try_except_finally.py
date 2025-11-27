from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to ChromeDriver (replace with your actual ChromeDriver path)
driver_path = "path/to/chromedriver"  # Example: "C:/chromedriver/chromedriver.exe"

# Initialize Selenium WebDriver (Chrome)
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # Open a website (example: a simple login page)
    driver.get("https://www.saucedemo.com")
    print("Opened SauceDemo website")

    # Find username field by ID and enter username
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    print("Entered username")

    # Find password field by ID and enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    print("Entered password")

    # Find login button by ID and click it
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("Clicked login button")

    # Wait for page to load
    time.sleep(2)

    # Verify successful login by checking page title or element
    page_title = driver.title
    print("Page title after login:", page_title)

    # Check if inventory page is displayed (by finding an element)
    inventory = driver.find_element(By.CLASS_NAME, "inventory_list")
    if inventory:
        print("Login successful! Inventory page displayed.")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
    print("Browser closed")
