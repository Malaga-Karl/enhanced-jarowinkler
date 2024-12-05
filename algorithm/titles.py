import pandas as pd

myfilepath = 'algorithm\\assets\\Books_df.csv'

df = pd.read_csv(myfilepath)
titles = df["Title"]

# for index, title in titles.items():
#     print(f'{index}: {title}')
