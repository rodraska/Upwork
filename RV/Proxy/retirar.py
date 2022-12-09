import pandas as pd

df = pd.read_csv("bosta.csv")

canada = df.loc[(df["Zip"].str.len() > 6) & (df["Zip"] != "Not Found")]

canada.to_csv('canada300.csv', index=False)

print(canada)