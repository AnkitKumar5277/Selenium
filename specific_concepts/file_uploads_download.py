from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
upload_input = driver.find_element("id", "file-upload")

upload_input.send_keys("C:\\Users\\YourName\\Desktop\\sample.txt")

driver.find_element("id", "file-submit").click()
time.sleep(3)
driver.quit()

