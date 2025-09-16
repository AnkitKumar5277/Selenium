from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Open Chrome
driver = webdriver.Chrome()

try:
    # Open a website
    driver.get("https://www.google.com")

    # Try to find an element which does not exist
    element = driver.find_element("id", "fakeElement")  # wrong locator

    # If element is found, do something
    element.click()

# Handle specific exception: element not found
except NoSuchElementException:
    print("❌ Element not found on the page.")

# Handle timeout error
except TimeoutException:
    print("⏳ The page took too long to load.")

# Handle any other exception
except Exception as e:
    print("⚠️ Some other error occurred:", e)

finally:
    # Close the browser after 3 seconds
    time.sleep(3)
    driver.quit()
