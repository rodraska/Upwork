import pandas as pd
import numpy as np

df1 = pd.read_csv("rvtoolcom.csv")
df2 = pd.read_csv("limpa_usa.csv")
df3 = pd.read_csv("limpa_canada.csv")

result = df1.append(df2).append(df3)

#df = df.drop_duplicates(subset='favorite_color', keep="first")

result = result.drop_duplicates(subset='address', keep="first")

result.to_csv('rv dealers.csv', index=False)
