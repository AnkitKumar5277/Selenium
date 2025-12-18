from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Edge()

# Open a sample website
driver.get("https://www.selenium.dev/")

# 1. Locate by ID
search_box = driver.find_element(By.ID, "gsc-i-id1")
search_box.send_keys("WebDriver")

# 2. Locate by Name
search_box_by_name = driver.find_element(By.NAME, "search")

# 3. Locate by Class Name
header = driver.find_element(By.CLASS_NAME, "navbar")

# 4. Locate by Tag Name
all_links = driver.find_elements(By.TAG_NAME, "a")
print("Total links:", len(all_links))

# 5. Locate by Link Text
downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
downloads_link.click()

# 6. Locate by Partial Link Text
projects_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Projec")
projects_link.click()

# 7. Locate by XPath
community_tab = driver.find_element(By.XPATH, '//*[@id="main_navbar"]/ul/li[4]/a')
community_tab.click()

# 8. Locate by CSS Selector
about_tab = driver.find_element(By.CSS_SELECTOR, "a[href='/about/']")
about_tab.click()

# Close browser
driver.quit()

