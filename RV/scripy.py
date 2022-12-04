import pandas as pd

df = pd.read_csv("coordinates.csv")

def give_coord(zip):

    lat = df[df.ZIP == zip].LAT.item()
    print(type(lat))
    lng = df[df.ZIP == zip].LNG.item()
    return (lat, lng)

print(give_coord(30075))