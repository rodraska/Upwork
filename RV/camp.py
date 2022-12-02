from bs4 import BeautifulSoup
import requests
import pandas as pd


def ft_camp(link):

    html_camp=requests.get(link).text
    soup_camp=BeautifulSoup(html_camp, 'lxml')

    """ with open('html_camp', 'w') as g:
        g.write(soup_camp.prettify()) """
    
    camp_header = soup_camp.find('div', class_='listing-header')
    camp_name = camp_header.find('h2', class_='listing-header-title').text
    name_list.append(camp_name)
    camp_location = camp_header.find('h3', class_='listing-header-location').text.strip()
    location_list.append(camp_location)
    camp_buttons = soup_camp.find('div', class_='row listing-buttons')
    if (camp_buttons.a is not None):
        camp_website = camp_buttons.a['href']
    elif (camp_buttons.a is None):
        camp_website = "Not Found"
    website_list.append(camp_website)
    if (soup_camp.find('div', class_='listing-section') is not None):
        if (soup_camp.find('div', class_='listing-section').p is not None):
            camp_open = soup_camp.find('div', class_='listing-section').p.text
        elif (soup_camp.find('div', class_='listing-section').p is None):
            camp_open = "Not Found"
    elif (soup_camp.find('div', class_='listing-section') is None):
        camp_open = "Not Found"
    open_list.append(camp_open)
    #print(camp_website)


init_link = 'https://gocampingamerica.com/search/'

states = ['Alabama', 'Alaska', 'Arizona', 'Arskansas', 'California',
'Colorado, Connecticut', 'Delaware', 'Florida', 'Georgia',
'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
'Michigan', 'Minnesota', 'Mississipi', 'Missouri', 'Montana',
'Nebraska', 'Nevada', 'New Hamsphire', 'New Jersey', 'New Mexico',
'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgina',
'Washington', 'West Virgina', 'Wisconsin', 'Wyoming']

for state in states:
    html_text=requests.get(init_link+state).text
    soup=BeautifulSoup(html_text, 'lxml')

    """ with open('html_cali', 'w') as f:
        f.write(soup.prettify()) """

    camps = soup.find_all('div', class_='col-md-4')

    #print(camps)

    links_list = []
    for camp in camps:
        if (camp.a is not None):
            link = camp.a['href']
            links_list.append(link)
            #print(link)

    #print(links_list)

    print(len(links_list))

    website_list = []
    name_list = []
    location_list = []
    open_list = []



    for link in links_list:
        ft_camp(link)

    print(len(name_list))
    print(len(website_list))
    print(len(location_list))
    print(len(open_list))

    data = {
        'Name': name_list,
        'Location': location_list,
        'Open': open_list,
        'Webiste': website_list
    }

    df = pd.DataFrame(data)

    df.to_csv('Illinois.xlsx', index=False)