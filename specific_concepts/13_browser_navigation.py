from selenium import webdriver
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Open Google
driver.get("https://www.google.com")
print("Opened Google")
time.sleep(2)

# Step 3: Navigate to YouTube
driver.get("https://www.youtube.com")
print("Opened YouTube")
time.sleep(2)

# Step 4: Go back to Google
driver.back()
print("Went back to Google")
time.sleep(2)

# Step 5: Go forward to YouTube again
driver.forward()
print("Went forward to YouTube")
time.sleep(2)

# Step 6: Refresh the page
driver.refresh()
print("Refreshed YouTube")
time.sleep(2)

# Step 7: Close the browser
driver.quit()
