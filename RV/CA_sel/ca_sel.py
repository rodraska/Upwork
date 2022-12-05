from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import re

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

def separate_city_zipcode(cities_zipcodes):
	cities = (re.sub(r',[ ](\w)*[ ](\w)*', '', cities_zipcodes))
	zipcodes = (re.sub(r'((\w)*.)?((\w)*[ ]?)*,[ ](\w)*[ ]', '', cities_zipcodes))
	states_small = (re.sub(r'[ ](\w)*$','',(re.sub(r'((\w)*.)?((\w)*[ ]?)*,[ ]', '', cities_zipcodes))))
	return (cities, zipcodes, states_small)

def get_all_links(driver):
	driver.get("https://www.cruiseamerica.com/rv-rental-locations/")
	states_sel = driver.find_elements(By.XPATH, '//select[@id="ddlStates"]')
	states = []
	for state in states_sel:
		states.append(state.text.lower())
	states = states[0].split('\n')
	states.pop(0)
	final_states = []
	for state in states:
		state = state.strip()
		if ' ' in state:
			state = state.replace(' ', '-')
		final_states.append(state)
	links = []
	for state in final_states:
		links.append("https://www.cruiseamerica.com/rv-rental-locations/" + state)
	return(links)

def get_all_dealers(links, driver):
	for link in links:
		
# driver.get("https://www.cruiseamerica.com/rv-rental-locations/alabama")
# names = driver.find_elements(By.XPATH, '//div[@class="location-services"]')
# addresses = driver.find_elements(By.XPATH, '//div[@class="location-address"]')



# for name, address in zip(names, addresses):
# 	print(name.text)
# 	addss = re.sub('\n.+', '',address.text)
# 	city, zipcode, state = separate_city_zipcode(re.sub('.+\n', '',address.text))
# 	print(addss)
# 	print(city)
# 	print(zipcode)
# 	print(state)

