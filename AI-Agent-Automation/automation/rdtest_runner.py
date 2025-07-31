from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def run_rd_test():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(), options=options)

    try:
        driver.get("https://rdtest.aadhaardevice.com/")
        time.sleep(3)
        print("✅ Page Title:", driver.title)
    finally:
        driver.quit()
