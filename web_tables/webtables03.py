from pycparser.ply.ctokens import t_DIVIDE
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtables():
    driver = webdriver.Edge()  # Changed from webdriver.firefox() to webdriver.Edge()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()

    # row
    # //table[contains(@id,"cust")]/tbody/tr
#     row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
#     row = len(row_elements)
#     print(row)
#
#     # col
#     # //table[contains(@id,"cust")]/tbody/tr[2]/td -> first column ka first row
#     col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
#     col = len(col_elements)
#     print(col)
#
#     # //table[contains(@id,'cust')]/tbody/tr[2]/td[3]
#
#     # FP - //table[contains(@id,"cust")]/tbody/tr
#     # 7 - i (2,7)
#     # SP - j/td1
#     # 3 - j (1,3)
#     # TP - j
#
# # //table[contains(@id,"cust")]/tbody/tr[5]/td[2]/following-sibling::td
# # right wala element dega jo pass me h
#     first_part = "//table[contains(@id,'cust')]/tbody/tr["
#     second_part = "]/td["
#     third_part = "]"
#
#     for i in range(2, row+1):  # range(1, 10) -> 1, 9+1)
#         for j in range(1, col+1):
#             dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
#             data = driver.find_element(By.XPATH, dynamic_path).text
#             if "Helen Bennett" in data:
#                 country_path = f"{dynamic_path}//following-sibling::td"
#                 country_text = driver.find_element(By.XPATH,country_path).text
#                 print(f"Helen Bennet is in {country_text}")

    # find helen bennett's country
    driver.get("https://awesomeqa.com/webtable1.html")
    # get the table
    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr") #//table[@summary='Sample Table']/tbody/tr[4]/td

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            print(e.text)
