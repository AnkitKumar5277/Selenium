# selenium 4 example
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")

time.sleep(2)

# Find Downloads link
download_link = driver.find_element(By.LINK_TEXT, "Downloads")

# Find link below Downloads
documentation_link = driver.find_element(
    locate_with(By.TAG_NAME, "a").below(download_link)
)

# Click the below element
documentation_link.click()

time.sleep(2)
driver.quit()




