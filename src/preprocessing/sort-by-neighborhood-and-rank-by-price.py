######################################
Separate hosts by neighborhood group and rank by  price
######################################

import pandas as pd
import os

#creating a dataframe called promotion from the sorted dataframe from last example
promotion = pd.read_csv(os.path.join(os.getenv('WORKSPACE'),'nyc_airbnb_sorted.csv'), sep="\t")

#sort by neighborhood group and price . inplace means the current dataframe will be updated
promotion.sort_values(by=["neighbourhood_group", "price"], inplace=True)
print()
print(promotion.head(20).to_string())

#to provide a count of how many results are from each neighborhood group, we use value_counts()
groups = promotion["neighbourhood_group"].value_counts()

#Print groups to a file and also to the screen
print(groups, file=open(os.path.join(os.getenv('WORKSPACE'),'neighbourhood_counts.txt'), 'a'))
print()
print(groups)
promotion.to_csv(os.path.join(os.getenv('WORKSPACE'),'nyc_airbnb_promotion.csv'), sep='\t', index_label=False)


#Your print(groups) will #look like:
#Brooklyn         231
#Manhattan        143
#Queens           133
#Bronx             29
#Staten Island     18
#Name: neighbourhood_group, dtype: int64
