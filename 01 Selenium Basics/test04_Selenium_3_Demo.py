from selenium import webdriver
from selenium.webdriver.edge.service import Service
import allure
import pytest


def test_vwo_sample_selenium_3():
    driver_path = 'C:\\Users\\Ankit Kumar\\Downloads\\msedgedriver.exe'  # Windows path fix
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service)

    driver.get("https://app.vwo.com")

# pytest Folder_1/test04_Selenium_3_Demo.py --alluredir=./allure-results

# allure serve allure-results