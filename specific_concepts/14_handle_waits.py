from selenium import webdriver

# open browser
driver = webdriver.Chrome()

# set implicit wait (applies to all elements)
driver.implicitly_wait(10)

driver.get("https://example.com")

# selenium will wait up to 10 seconds for element
element = driver.find_element("id", "myElement")

print("Element found:", element.text)

driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# explicit wait for specific element
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))

print("Element found:", element.text)

driver.quit()
