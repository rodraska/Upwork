from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import pandas as pd

dfc = pd.read_csv("coordinates.csv")

def give_coord(zip):
        lat = dfc[dfc.ZIP == zip].LAT.item()
        lng = dfc[dfc.ZIP == zip].LNG.item()
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
        name = dealer.find('h3').text
        dealer_name.append(name)
        br = dealer.find('div', class_='details').br
        address = br.previousSibling.strip('\n')
        dealer_address.append(address)
        ziptotal = br.nextSibling.strip().replace('\n', '').split(',')
        dealer_city.append(ziptotal[0])
        dealer_state.append(ziptotal[1])
        zip = ziptotal[2]
        dealer_zip.append(zip)
        try:
            lat, lng = give_coord(int(zip))
            dealer_lat.append(lat)
            dealer_lng.append(lng)
        except ValueError:
            lat, lng = "Not Found", "Not Found"
            dealer_lat.append(lat)
            dealer_lng.append(lng)
        #print(ziptotal)
    #print(len(dealer_zip))

    data = {
        'Name': dealer_name,
        'Address': dealer_address,
        'City': dealer_city,
        'State': dealer_state,
        'Zip': dealer_zip,
        'Lat': dealer_lat,
        'Lng': dealer_lng
    }

    df = pd.DataFrame(data)

    df.to_csv('rv_dealers.xlsx', index=False)
        


