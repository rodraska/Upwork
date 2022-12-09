import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

def give_coord(zip):
	df = pd.read_csv("../coordinates.csv")
	lat = df[df.ZIP == zip].LAT.item()
	lng = df[df.ZIP == zip].LNG.item()
	return (lat, lng)

def get_coord_online(driver, address):
	driver.get('https://www.latlong.net/convert-address-to-lat-long.html')
	input_adress = driver.find_element(By.XPATH, '//input[@id="uB2301"]')
	input_adress.send_keys(address)
	

df = pd.read_csv('../Proxy/rv_dealers.csv')
coords = []
for i in range(len(df.Zip)):
	try:
		lat, lng = give_coord(int(df.Zip.loc[i]))
	except ValueError:
		pass
	coords.append((lat, lng))
	i += 1
