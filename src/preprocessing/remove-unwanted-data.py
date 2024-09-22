######################################
Remove unwanted columns and rows from a dataframe
######################################

import pandas as pd
import os

df = pd.read_csv(os.path.join(os.getenv('WORKSPACE'),'AB_NYC_2019.csv'))


#Specifies the columns that we will not need in our studies. 
droplist = [
    "host_name",
    "neighbourhood",
    "latitude",
    "longitude",
    "room_type",
    "calculated_host_listings_count",
    "reviews_per_month"
	]
    
#Create a new dataset from the columns that were not dropped
df2 = df.drop(droplist, axis='columns')

#Verify that the columns were dropped from the new dataset
print(df2.head(1).to_string())

#Drops all the empty columns from the dataframe. inplace option allows this change without needing to be saved into a new dataframe
df2.dropna(inplace=True)

df2.info() #now you can see the non-null count matches the total entries now

#You can back up your new work or newly saved dataframes as a new cvs file using the to_csv function
#For example df.to_csv('out.cvs', index=False) will save the dataframe to out.csv without indexes/row names
