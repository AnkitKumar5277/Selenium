from selenium import webdriver
import time

# Open browser
driver = webdriver.Chrome()

# Open a demo file upload page
driver.get("https://the-internet.herokuapp.com/upload")

# Locate the file input element
upload_input = driver.find_element("id", "file-upload")

# Provide full path of file to upload
upload_input.send_keys("C:\\Users\\YourName\\Desktop\\sample.txt")

# Click on Upload button
driver.find_element("id", "file-submit").click()

# Wait for a few seconds to see result
time.sleep(3)

# Close browser
driver.quit()
