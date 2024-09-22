######################################
Sort Results
######################################
import pandas as pd
import os

#reading the dataframe that was created in the last example
df4 = pd.read_csv(os.path.join(os.getenv('WORKSPACE'),'nyc_airbnb_df3.csv'), sep="\t")

#Sort the dataframe by neighborood group and last review
df4.sort_values(by=["neighbourhood_group", "last_review"], inplace=True)

df4.info()
print()
print(df4.head(10).to_string())
print()
print(df4.tail(10).to_string())
