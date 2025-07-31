from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_test():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://rdtest.aadhaardevice.com/")
    print("Selenium test launched.")
    driver.quit()