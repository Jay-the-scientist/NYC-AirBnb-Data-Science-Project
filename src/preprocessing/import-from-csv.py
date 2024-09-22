######################################
Import data from a csv file
######################################

import pandas as pd
import os

df = pd.read_csv(os.path.join(os.getenv('WORKSPACE'),'AB_NYC_2019.csv')) #Reading the file into the pandas dataframe. The 'os' parameter is because this was done in a virtual environmen connecting to the file. 

print(df.head(1).to_string()) #Print the first column of the dataframe. Can change the number to show as many columns

df.info() #Gives all he information on the table. Specifies how many rows and columns there are, and if the non-null count does not equal the toal amount of entries, that means some data is missing.

