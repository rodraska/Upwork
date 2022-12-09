from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
import random
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--lang=en")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=None)

df = pd.read_json('RV/Proxy/local_html/names.json')

driver.get("https://www.google.com/search?channel=fs&client=ubuntu&q=1000+Islands+RV+Centre+Gananoque%2C+Ontario")
driver.find_element(By.XPATH, '//button[@class="tHlp8d"]').click()
addresses = []
for i in range(len(df.name)):
	try:
		search = df['name'].iloc[i] + ' ' + df['place'].iloc[i]
		q = driver.find_element("name","q")
		time.sleep(random.random())
		q.clear()
		time.sleep(random.random())
		q.send_keys(search)
		time.sleep(random.random())
		q.send_keys(Keys.ENTER)
		address = driver.find_element(By.XPATH, '//span[@class="LrzXr"]')
		addresses.append(address.text)
	except:
		try:
			search = df['name'].iloc[i]
			q = driver.find_element("name","q")
			time.sleep(random.random())
			q.clear()
			time.sleep(random.random())
			q.send_keys(search)
			time.sleep(random.random())
			q.send_keys(Keys.ENTER)
			address = driver.find_element(By.XPATH, '//span[@class="LrzXr"]')
			addresses.append(address.text)
		except:
			addresses.append('None')
	print(f"{addresses[i]}, {i}")
	time.sleep(0.2)

test = pd.DataFrame(addresses)
test.to_csv('test.csv')