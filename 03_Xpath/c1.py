import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("selenium mini project 2_ebay")
@allure.description("print the items and prices of Macmini")
@pytest.mark.itemsandprice

def test_print_items_price():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(3)

    # < input
    # data - marko = "{&quot;oninput&quot;:&quot;handleTextUpdate s0-1-4-13-4 false&quot;,&quot;onfocusin&quot;:&quot;handleMarkTimer s0-1-4-13-4 false&quot;,&quot;onkeydown&quot;:&quot;handleMarkTimer s0-1-4-13-4 false&quot;}"
    # data - marko - key = "@input s0-1-4-13-4"
    # id = "gh-ac"
    # class ="gh-search-input gh-tb ui-autocomplete-input"
    # title="Search"
    # type="text"
    # search_box_web_element = driver.find_element(By.XPATH,"//input[@class='gh-search-input gh-tb ui-autocomplete-input']")
    # search_box_web_element = driver.find_element(By.XPATH,"//input[contains(@class,'gh-search')]")
    search_box_web_element = driver.find_element(By.XPATH,"//input[starts-with(@id,'gh')]")
    search_box_web_element.send_keys("macmini")

    """  # <button
    # class="gh-search-button btn btn--primary"
    # data-ebayui=""
    # type="submit"
    # id="gh-search-btn"
"""
    search_button_web_element = driver.find_element(By.CSS_SELECTOR,"#gn-search-btn")
    search_button_web_element.click()

    # <div class="s-item__title"> ---- items
    # <span class="s-item__price"> ---- price
    items_name_web_element = driver.find_elements(By.CLASS_NAME, "s-item__title")
    items_price_web_element = driver.find_elements(By.CSS_SELECTOR,"s-item__price")

    for name, price in zip(items_name_web_element, items_price_web_element):
        print(f"Item: {name.text}, Price: {price.text}")

    time.sleep(5)
    driver.quit()
