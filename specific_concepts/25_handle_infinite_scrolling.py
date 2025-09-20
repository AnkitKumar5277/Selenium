from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open browser
driver = webdriver.Edge()

# Step 2: Open a website with infinite scroll
driver.get("https://infinite-scroll.com/demo/full-page/")

# Step 3: Maximize window
driver.maximize_window()

# Step 4: Scroll multiple times
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(5):  # 5 times scroll karega (you can increase)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for content to load

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:  # agar aur content load nahi ho raha
        break
    last_height = new_height

print("✅ Infinite scroll handled!")
driver.quit()
