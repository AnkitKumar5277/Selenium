import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

@allure.title("stale_element")
@allure.description("stale_element")
def test_stale_element_exp_demo():
    # Use the EdgeService to manage the msedgedriver executable
    edge_service = EdgeService()

    # Initialize the Edge WebDriver with the service
    driver = webdriver.Edge(service=edge_service)
    driver.get("https://google.com")

    try:
        # Find the search text area by its name attribute
        textarea = driver.find_element(By.NAME, "q")

        # Refresh the page, which invalidates the 'textarea' element
        driver.refresh()

        # This will raise a StaleElementReferenceException
        textarea.send_keys("The Testing Academy")

    except StaleElementReferenceException as see:
        # Catch the exception and print a descriptive message
        print(f"Stale element reference caught: {see}")

    finally:
        # It's a good practice to close the driver in a finally block
        # to ensure it always runs, even if an exception occurs
        driver.quit()

# To run the script, you would typically call the function directly
# or use a test runner like pytest.

# test_stale_element_exp_demo()
