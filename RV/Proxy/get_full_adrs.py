from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
import re
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--lang=en")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

df = pd.read_json('/home/miguel/Desktop/Upwork/RV/Proxy/local_html/names.json')

driver.get("https://www.google.com/search?channel=fs&client=ubuntu&q=1000+Islands+RV+Centre+Gananoque%2C+Ontario")
driver.find_element(By.XPATH, '//button[@class="tHlp8d"]').click()
addresses = []
for i in range(10):
	search = df['name'].iloc[i] + ' ' + df['place'].iloc[i]
	print(search)
	q = driver.find_element("name","q")
	time.sleep(0.2)
	q.clear()
	time.sleep(0.2)
	q.send_keys(search)
	time.sleep(0.2)
	q.send_keys(Keys.ENTER)
	try:
		address = driver.find_element(By.XPATH, '//span[@class="LrzXr"]')
		addresses.append(address.text)
	except:
		addresses.append('None')
	time.sleep(0.2)

test = pd.DataFrame(addresses)
test.to_csv('test.csv')