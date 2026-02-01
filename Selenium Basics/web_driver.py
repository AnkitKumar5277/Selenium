from selenium import webdriver
from selenium.webdriver.edge.service import Service
import allure
import pytest

def test_vwo_sample_selenium_3():
    driver_path = 'C:\\Users\\Ankit Kumar\\Downloads\\msedgedriver.exe'  # Windows path fix
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service)

    driver.get("https://app.vwo.com")

# pytest main.py --alluredir=reports
# allure serve reports
