from selenium import webdriver
from selenium.webdriver.common.by import By
# Step 1: Launch browser
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")

# Step 2: Locate the table
table = driver.find_element(By.ID, "customers")

# Step 3: Get all rows
rows = table.find_elements(By.TAG_NAME, "tr")

print("Total rows:", len(rows))

# Step 4: Loop through each row and get columns
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    for col in cols:
        print(col.text, end=" | ")  # print each cell
    print()  # new line after each row

driver.quit()

