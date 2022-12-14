import pandas as pd

df = pd.read_csv("rvtool.csv")

df["site"] = "rvtool"

df.to_csv('rvtoolcom.csv', index=False)