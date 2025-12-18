from selenium import webdriver
import time
# Launch browser
driver = webdriver.Edge()
driver.get("https://www.w3schools.com/html/html_tooltip.asp")

# Locate element with tooltip
tooltip_element = driver.find_element("xpath", "//a[text()='W3Schools']")

tooltip_text = tooltip_element.get_attribute("title")

print("Tooltip is:", tooltip_text)

time.sleep(100)
driver.quit()
