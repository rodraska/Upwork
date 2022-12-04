from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# def launchBrowser():
# 	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# 	driver.get("https://chromedriver.chromium.org/downloads")


# launchBrowser()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.cruiseamerica.com/rv-rental-locations/alabama")
names = driver.find_elements(By.XPATH, '//div[@class="location-services"]')
addresses = driver.find_elements(By.XPATH, '//div[@class="location-address"]')

for name, address in zip(names, addresses):
	print(name.text)
	print(address.text)
