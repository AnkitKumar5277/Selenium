from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# 1. Create a folder to store downloads
download_path = os.getcwd() + "\\downloads"

# 2. Set Chrome options to download automatically
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_path,  # set custom download folder
    "download.prompt_for_download": False,        # disable download prompt
    "plugins.always_open_pdf_externally": True    # open PDFs in download instead of browser
}
options.add_experimental_option("prefs", prefs)

# 3. Launch Chrome with these options
driver = webdriver.Chrome(service=Service(), options=options)

# 4. Open a sample file download website
driver.get("https://file-examples.com/index.php/sample-documents-download/")

# 5. Click on download link (example button)
download_button = driver.find_element(By.XPATH, "(//a[text()='Download sample DOC file'])[1]")
download_button.click()

# 6. Wait to ensure download completes
time.sleep(5)

driver.quit()

print(f"File downloaded in: {download_path}")
