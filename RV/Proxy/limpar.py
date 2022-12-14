import pandas as pd

df = pd.read_csv("bosta.csv")

df["site"] = "RVT"

limpo = df.query("lat != 'Not Found'")

limpo_canada = limpo.loc[df["zip"].str.contains(" ")]
limpo_usa = limpo.loc[~df["zip"].str.contains(" ")]

limpo_usa.to_csv('limpa_usa.csv', index=False)
limpo_canada.to_csv('limpa_canada.csv', index=False)
