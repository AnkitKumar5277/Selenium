from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)
driver.get("https://www.youtube.com")
print("Opened YouTube")

time.sleep(2)
driver.back()
print("Went back to Google")

time.sleep(2)
driver.forward()
print("Went forward to YouTube")
time.sleep(2)

driver.refresh()
print("Refreshed YouTube")
time.sleep(2)

driver.quit()

