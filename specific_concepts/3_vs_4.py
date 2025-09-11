# # selenium 3 example
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Edge()
# driver.get("https://wwww.google.com")
#
# search_box = driver.find_element(driver.find_elements(By.XPATH,"//textarea[@title='Search']"))
# search_box.send_keys("Selenium 3 example")
# search_box.submit()
# driver.quit()

# selenium 4 example
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time
# Selenium 4 ke locate_with feature se aap elements ko
# dusre elements ke relative position (jaise near, above, below) se locate kar sakte hain.

driver = webdriver.Edge()
driver.get("https://www.selenium.dev/")

time.sleep(2)
download_link = driver.find_element(By.LINK_TEXT, "Downloads")
documentation_link = driver.find_element(
    locate_with(By.TAG_NAME,"a").below(download_link)
)

print("Found link: ",documentation_link.text)

driver.switch_to.new_window("tab")
driver.get("https://www.google.com")
driver.quit()


