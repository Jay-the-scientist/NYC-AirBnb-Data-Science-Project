######################################
Remove rows that dont fit parameters
######################################
import pandas as pd
import os

#In this example, we are reading the file from the new dataframe file we would have just created in the last step at the end
df3 = pd.read_csv(os.path.join(os.getenv('WORKSPACE'),'nyc_airbnb_df2.csv'), sep="\t")

#Its always a good idea to remove duplicates to avoid counting something twice
df3.drop_duplicates(inplace=True)

#To make sure all of data in column is in same format. Ensures all date columns are in same dae format
df3['last_review'] = pd.to_datetime(df3['last_review'])

#Now we remove any fields from our data tha dont meet our requirements
#Requirements:Promote airbnb units that are $100/night or less, don't require more than 2 nights minimum stay, have at least 100 reviews, and avalable at least 180 days per year
df3 = df3.query('price < 101 & minimum_nights < 3 & number_of_reviews > 99 & availability_365 > 179')

df3.info()
print() # print blank line
print(df3.head(20).to_string()) # print first 20 lines of data

#You can use len(df) to print store or calculate number of entries in dataframe
