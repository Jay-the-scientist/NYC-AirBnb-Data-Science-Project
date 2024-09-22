######################################
Comparing data from two neighborhoods Project - Final Version
######################################
import pandas as pd
import os

# Load the dataset
df = pd.read_csv(os.path.join(os.getenv('WORKSPACE'), 'AB_NYC_2019.csv'))

# Clean the data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Identify the two most popular neighborhoods
top2 = df["neighbourhood_group"].value_counts().nlargest(2).index.tolist()
print(f"The top two most popular boroughs are {top2[0]} and {top2[1]}")

# Convert 'last_review' to datetime
df['last_review'] = pd.to_datetime(df['last_review'])

# Filter for luxury homes in the top two neighborhoods
specialdf = df.query('(neighbourhood_group == @top2[0] or neighbourhood_group == @top2[1]) & price > 999 & minimum_nights < 3')

# Display results
print(f"\nIn these areas, the number of luxury homes costing more than $1000/night and having a minimum stay of 1 or 2 nights is {len(specialdf)}:\n")
print(specialdf.head(20).to_string())
