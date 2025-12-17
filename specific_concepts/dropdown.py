from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Edge()
driver.get("https://www.selenium.dev/selenium/web/formPage.html")
dropdown = driver.find_element("name","selectomatic")

select = Select(dropdown)
select.select_by_visible_text("One")
time.sleep(1)

select.select_by_index(2)
time.sleep(1)

select.select_by_value("fouth")
time.sleep(1)

driver.quit()

