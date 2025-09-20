from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open a site with a date picker (demo site)
driver.get("https://demoqa.com/date-picker")

# Maximize window
driver.maximize_window()

# Wait a bit
time.sleep(2)

# 1. Click on the date input box to open calendar
date_input = driver.find_element(By.ID, "datePickerMonthYearInput")
date_input.click()

# 2. Select month (Dropdown for month)
month_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
month_dropdown.send_keys("September")

# 3. Select year (Dropdown for year)
year_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
year_dropdown.send_keys("2025")

# 4. Select date (15th)
driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015']").click()

time.sleep(3)
driver.quit()
