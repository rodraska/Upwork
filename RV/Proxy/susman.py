from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import pandas as pd

dfc = pd.read_csv("canadacoord.csv")

def give_coord(zip):
        lat = dfc[dfc.POSTAL_CODE == zip].LATITUDE.item()
        lng = dfc[dfc.POSTAL_CODE == zip].LONGITUDE.item()
        return (lat, lng)

with open('rvt.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    dealers = soup.find_all('div', class_='standard-dealer')
    dealer_name = []
    dealer_address = []
    dealer_city = []
    dealer_state = []
    dealer_zip = []
    dealer_lat = []
    dealer_lng = []

    for dealer in dealers:
        br = dealer.find('div', class_='details').br
        ziptotal = br.nextSibling.strip().replace('\n', '').split(',')
        zip = ziptotal[2]
        if (len(zip) > 5):
            name = dealer.find('h3').text
            dealer_name.append(name)
            address = br.previousSibling.strip('\n')
            dealer_address.append(address)
            dealer_city.append(ziptotal[0])
            dealer_state.append(ziptotal[1])
            dealer_zip.append(zip)
            try:
                lat, lng = give_coord(zip)
                dealer_lat.append(lat)
                dealer_lng.append(lng)
            except ValueError:
                lat, lng = "Not Found", "Not Found"
                dealer_lat.append(lat)
                dealer_lng.append(lng)

    print(len(dealer_zip))
    #print(len(dealer_zip))

    data = {
        'name': dealer_name,
        'address': dealer_address,
        'city': dealer_city,
        'state': dealer_state,
        'zip': dealer_zip,
        'lat': dealer_lat,
        'lng': dealer_lng
    }

    df = pd.DataFrame(data)

    df.to_csv('great_canada.xlsx', index=False)
        


