from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://gocampingamerica.com/states/camping-in-california').text
soup=BeautifulSoup(html_text, 'lxml')

with open('html_cali', 'w') as f:
    f.write(soup.prettify())

camps = soup.find_all('div', class_='col-md-4')

#print(camps)

links_list = []
for camp in camps:
    if (camp.a is not None):
        link = camp.a['href']
        links_list.append(link)
        #print(link)

#print(links_list)

""" for link in links_list:
    html_camp=requests.get(link).text
    soup_camp=BeautifulSoup(html_camp, 'lxml')
    print('ola')
    camp_header = soup_camp.find('div', class_='listing-header')
    camp_name = camp_header.find('h2', class_='listing-header-title').text
    camp_location = camp_header.find('h3', class_='listing-header-location').text.strip()
    camp_buttons = soup_camp.find('div', class_='row listing-buttons')
    if (camp_buttons.a is not None):
        camp_website = camp_buttons.a['href']
    if (soup_camp.find('div', class_='listing-section') is not None):
        camp_open = soup_camp.find('div', class_='listing-section').p.text

    print(camp_open) """


html_camp=requests.get('https://gocampingamerica.com/parks/wine-country-rv-resort-93446').text
soup_camp=BeautifulSoup(html_camp, 'lxml')

with open('html_camp', 'w') as g:
    g.write(soup_camp.prettify())

camp_header = soup_camp.find('div', class_='listing-header')
camp_name = camp_header.find('h2', class_='listing-header-title').text
camp_location = camp_header.find('h3', class_='listing-header-location').text.strip()
camp_buttons = soup_camp.find('div', class_='row listing-buttons')
camp_website = camp_buttons.a['href']
camp_open = soup_camp.find('div', class_='listing-section').p.text

print(camp_location)