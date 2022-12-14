import pandas as pd

df = pd.read_csv("biggertool.csv")

print(df.query("state == 'Texas'").describe())