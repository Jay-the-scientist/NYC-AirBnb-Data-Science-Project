######################################
Comparing data from two neighborhoods Project - Final Version
This code should work in a non practice environment to view he data straight from the repoisitory
######################################

import pandas as pd
import os
import requests
import io

url = "https://raw.githubusercontent.com/VinayakW/AB_NYC_2019/refs/heads/main/AB_NYC_2019.csv"
response = requests.get(url)

df = pd.read_csv(io.StringIO(response.text))

#df = pd.read_csv(url)
#df.info()
#print()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
#df.info()
#print()

top2 = df["neighbourhood_group"].value_counts().nlargest(2).index.tolist()
print(f"The top two most popular boroughs are {top2[0]} and {top2[1]}")

df['last_review'] = pd.to_datetime(df['last_review'])
specialdf = df.query('(neighbourhood_group == @top2[0] or neighbourhood_group == @top2[1]) & price > 999 & minimum_nights < 3')
print()
print(f"In these areas, the number of  Luxury Homes costing more than $1000/night and have minimum stay of 1 or 2 nights is {len(specialdf)} :")
print()
print(specialdf.head(20).to_string())
print()
