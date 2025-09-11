from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to ChromeDriver (replace with your ChromeDriver path)
driver_path = "path/to/chromedriver"  # Example: "C:/chromedriver/chromedriver.exe"

# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # Open a website
    driver.get("https://www.google.com")
    print("Opened Google website")

    # Find the search box by name attribute
    search_box = driver.findElement(By.NAME, "q")

    # Type a search query
    search_box.send_keys("Selenium Python Tutorial")

    # Press Enter to search
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(2)

    # Print the page title
    print("Page title:", driver.title)

finally:
    # Close the browser
    driver.quit()
    print("Browser closed")