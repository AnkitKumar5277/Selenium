from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()
time.sleep(2)

source = driver.find_element(By.XPATH,"//a[text()='BANK']")
target = driver.find_element(By.ID,"bank")
actions = ActionChains(driver)

actions.drag_and_drop(source, target).perform()
time.sleep(5)
driver.quit()