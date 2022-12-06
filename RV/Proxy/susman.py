from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import pandas as pd


with open('rvt.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    dealers = soup.find_all('div', class_='standard-dealer')
    dealer_name = []
    dealer_address = []
    dealer_city = []
    dealer_state = []
    dealer_zip = []

    for dealer in dealers:
        name = dealer.find('h3').text
        dealer_name.append(name)
        br = dealer.find('div', class_='details').br
        address = br.previousSibling.strip('\n')
        dealer_address.append(address)
        ziptotal = br.nextSibling.strip().replace('\n', '').split(',')
        dealer_city.append(ziptotal[0])
        dealer_state.append(ziptotal[1])
        dealer_zip.append(ziptotal[2])

        #print(ziptotal)
    #print(dealer_zip)

    data = {
        'Name': dealer_name,
        'Address': dealer_address,
        'City': dealer_city,
        'State': dealer_state,
        'Zip': dealer_zip
    }

    df = pd.DataFrame(data)

    df.to_csv('rv_dealers.xlsx', index=False)
        


