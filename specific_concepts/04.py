from selenium import webdriver

# Set path to your chromedriver
driver = webdriver.Chrome(executable_path="C:/drivers/chromedriver.exe")

# Open a website
driver.get("https://www.google.com")

# Print the title of the page
print("Page Title is:", driver.title)

# Close the browser
driver.quit()
