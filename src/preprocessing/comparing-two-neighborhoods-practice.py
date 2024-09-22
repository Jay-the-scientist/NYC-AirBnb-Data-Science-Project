######################################
Comparing data from two neighborhoods Project
######################################


import pandas as pd
import os

df = pd.read_csv(os.path.join(os.getenv('WORKSPACE'),'AB_NYC_2019.csv'))
#df.info()
#print()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
#df.info()
#print()

#Now we want to be able to automatically tell which two neighborhoods are he most popular
#We can take the value counts of the neighborhood_group group, then take the two largest useing .largest(2), then index to lis to be able use he names. alternatively could use index[0[] or [1] to get the number value associated with
#group = df["neighbourhood_group"].value_counts()
#mostpopular = group.nlargest(2)
#print(mostpopular)
#print(mostpopular[0])
#tops = mostpopular.index.tolist()
#print(tops)

#You could also take the group and shorten the above code to :
#tops = group.nlargest(2).index.tolist()

#You can combine all this code into one line to save your name variables accecssible by top2[i]
top2 = df["neighbourhood_group"].value_counts().nlargest(2).index.tolist()
print(f"The top two most popular boroughs are {top2[0]} and {top2[1]}")

#This is what it would look like if i needed to traverse for calculations
#for neighborhood,e in populargroup:
#	print(populargroup[e])
df['last_review'] = pd.to_datetime(df['last_review'])
specialdf = df.query('(neighbourhood_group == @top2[0] or neighbourhood_group == @top2[1]) & price > 999 & minimum_nights < 3')
print()
print(f"In these areas, the number of  Luxury Homes costing more than $1000/night and have minimum stay of 1 or 2 nights is {len(specialdf)} :")
print()
print(specialdf.head(20).to_string())
print()
#print(df.head(20).to_string())
