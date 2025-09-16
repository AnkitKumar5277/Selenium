from selenium import webdriver

# Launch browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# -------------------------------
# 1. Get all cookies
cookies = driver.get_cookies()
print("All cookies:", cookies)

# 2. Add a new cookie
driver.add_cookie({"name": "test_cookie", "value": "hello123"})
print("Cookie added!")

# 3. Get a specific cookie by name
cookie = driver.get_cookie("test_cookie")
print("My Cookie:", cookie)

# 4. Delete a specific cookie
driver.delete_cookie("test_cookie")
print("Specific cookie deleted!")

# 5. Delete all cookies
driver.delete_all_cookies()
print("All cookies deleted!")

# Close browser
driver.quit()
