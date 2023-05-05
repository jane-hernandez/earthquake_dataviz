import numpy as np
import pandas as pd
df= pd.read_csv("earthquakeAPI_data.csv")

print(df.isnull().sum())

# Assign a continent label to rows that have missing values for that column.
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pycountry_convert as pc

# Define a list of continent names to convert the continent code to a significant name.
def get_continent_name(continent_code):
    continent_code_dict = {
        "AF": "Africa",
        "AS": "Asia",
        "AQ": "Antarctica",
        "EU": "Europe",
        "NA": "North America",
        "OC": "Oceania",
        "SA": "South America"}
    return continent_code_dict[continent_code]

# Use the longitude and latitude to assign a continent value. Ocean/Unknown is assigned when there isn't one assigned from the library.
def get_continent(lat,long):
    
    locator = Nominatim(user_agent="gklvsd@gmail.com", timeout=10)
    geocode = RateLimiter(locator.reverse, min_delay_seconds=1)

    loc = geocode(f"{lat}, {long}", language="en")
    
    if loc is None:
        return "Ocean/Unknown"

    address = loc.raw["address"]
    country_code = address["country_code"].upper()

    continent_code = pc.country_alpha2_to_continent_code(country_code)
    continent_name = get_continent_name(continent_code)

    return continent_name

# Apply the defined functions to a subset of the dataset that has missing values for the continent column.
subset_df = df[df["continent"].isna()]
subset_df['continent'] = subset_df.apply(lambda row: get_continent(row['latitude'], row['longitude']), axis=1)
id_continent_dict = dict(zip(subset_df['id'], subset_df['continent']))

# Replace the missing values for the column continent with the newfound values continents.
for index, row in df.iterrows():
    if row['id'] in id_continent_dict:
        df.at[index, 'continent'] = id_continent_dict[row['id']]

del subset_df, id_continent_dict, index,row 

df.to_csv("Earthquake_with_continents.csv")
