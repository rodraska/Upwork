from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd

dfc = pd.read_csv("coordinates.csv")

def give_coord(zip):
        lat = dfc[dfc.ZIP == zip].LAT.item()
        lng = dfc[dfc.ZIP == zip].LNG.item()
        return (lat, lng)

dfc2 = pd.read_csv("canadacoord.csv")

def give_coord2(zip):
        lat = dfc2[dfc2.POSTAL_CODE == zip].LATITUDE.item()
        lng = dfc2[dfc2.POSTAL_CODE == zip].LONGITUDE.item()
        return (lat, lng)

df = pd.read_csv("full_adrs_from_google.csv")

address_list = df['0'].tolist()

with open('rvt.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    bloco = soup.find('ul', class_='three-col-list')
    dealers = bloco.find_all('li')
    dealers_name = []
    dealers_city = []
    dealers_state = []
    dealers_phone = []
    dealers_address = []
    dealers_zip = []
    dealers_lat = []
    dealers_lng = []

    for string in address_list:
        dados = string.split(', ')
        full_address = dados[0]
        dealers_address.append(full_address)
        if (dados[-1] == "Estados Unidos"):
            zip = dados[-2][-5:]
            try:
                lat, lng = give_coord(int(zip))
                dealers_lat.append(lat)
                dealers_lng.append(lng)
            except:
                lat, lng = "Not Found", "Not Found"
                dealers_lat.append(lat)
                dealers_lng.append(lng)
        elif (dados[-1] == "Canadá"):
            zip = dados[-2][-7:]
            try:
                lat, lng = give_coord2(zip)
                dealers_lat.append(lat)
                dealers_lng.append(lng)
            except:
                lat, lng = "Not Found", "Not Found"
                dealers_lat.append(lat)
                dealers_lng.append(lng)
        else:
            zip = "Not Found"
            lat, lng = "Not Found", "Not Found"
            dealers_lat.append(lat)
            dealers_lng.append(lng)
        dealers_zip.append(zip)
    for dealer in dealers:
        info = dealer.find_all('span')
        dealers_name.append(info[0].text)
        loc = info[1].text.split(', ')
        dealers_city.append(loc[0])
        dealers_state.append(loc[1])
        dealers_phone.append(info[2].text)

    data = {
        'name': dealers_name,
        'address': dealers_address,
        'city': dealers_city,
        'state': dealers_state,
        'zip': dealers_zip,
        'lat': dealers_lat,
        'lng': dealers_lng
    }

    frame = pd.DataFrame(data)

    frame.to_csv('bosta.csv', index=False)
    



