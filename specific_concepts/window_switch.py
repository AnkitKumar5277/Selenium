from selenium import webdriver
import time

# Launch browser
driver = webdriver.Edge()
driver.get("https://www.selenium.dev/")   # Open main site
driver.maximize_window()

print("Current Window Title: ", driver.title)

# Click link that opens new window
driver.find_element("xpath", "//a[text()='Watch the Videos']").click()
time.sleep(2)  # wait for new window

# Get all window handles
handles = driver.window_handles
print("All window handles: ", handles)

# Switch to the second window (index 1)
driver.switch_to.window(handles[1])
print("Now switched to: ", driver.title)

# Perform action on new window
time.sleep(2)

# Switch back to first window (index 0)
driver.switch_to.window(handles[0])
print("Back to first window: ", driver.title)

# Close browser
driver.quit()
