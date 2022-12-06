import pandas as pd

df = pd.read_csv("/nfs/homes/rreis-de/Projects/upwork/RV/koa/sussy_baka.csv")

df.to_xlxs('koa_parks.xlxs', index=False)