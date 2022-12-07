import pandas as pd

coords = pd.read_csv("coordinates.csv")

def give_coord(zip):
    return (coords[coords.ZIP == zip].LAT.item(), coords[coords.ZIP == zip].LNG.item())

data = pd.read_csv('CA_sel/CruiseAmerica.csv')


coordinates = []
for i in range(len(data.name)):
    try:
        coordinates.append(give_coord((data.zipcode.iloc[i])))
    except ValueError:
        coordinates.append(('none', 'none'))

data = data.join(pd.DataFrame(coordinates, columns=['Lat', 'Lng']))
data.to_csv('deliver/CruiseAmerica.csv', index=False)