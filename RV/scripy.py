import pandas as pd

df = pd.read_csv("coordinates.csv")

def give_coord(zip):

    lat = df[df.ZIP == zip].LAT.item()
    lng = df[df.ZIP == zip].LNG.item()
    return (lat, lng)

a = '56467-687'
print(a[:5])

#print(give_coord(30075))