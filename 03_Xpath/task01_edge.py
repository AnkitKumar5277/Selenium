import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


@allure.title("selenium mini project 2_ebay")
@allure.description("print the items and prices of Macmini")
@pytest.mark.itemsandprice
def test_print_items_price():
    edge_options = Options()
    edge_options.add_argument("--inprivate")
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(3)

    search_box_web_element = driver.find_element(By.XPATH, "//input[starts-with(@id,'gh')]")
    search_box_web_element.send_keys("macmini")

    search_button_web_element = driver.find_element(By.CSS_SELECTOR, "#gn-search-btn")
    search_button_web_element.click()

    items_name_web_element = driver.find_elements(By.CLASS_NAME, "s-item__title")
    items_price_web_element = driver.find_elements(By.CSS_SELECTOR, "s-item__price")

    for name, price in zip(items_name_web_element, items_price_web_element):
        print(f"Item: {name.text}, Price: {price.text}")

    time.sleep(5)
    driver.quit()

    # pytest -s C:\Users\Ankit Kumar\PycharmProjects\Focus\03_Xpath\task01_edge.py --alluredir=./allure-results
    # allure serve allure-results