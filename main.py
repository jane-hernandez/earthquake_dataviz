
#!/usr/bin/env python
# coding: utf-8

# In[60]:

import numpy as np
import pandas as pd
df= pd.read_csv("earthquakeAPI_data.csv")


# In[61]:


df


# In[64]:


print(df.isnull().sum())


# In[65]:

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pycountry_convert as pc
 
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

subset_df = df[df["continent"].isna()]
subset_df['continent'] = subset_df.apply(lambda row: get_continent(row['latitude'], row['longitude']), axis=1)
id_continent_dict = dict(zip(subset_df['id'], subset_df['continent']))

for index, row in df.iterrows():
    if row['id'] in id_continent_dict:
        df.at[index, 'continent'] = id_continent_dict[row['id']]

del subset_df, id_continent_dict, index,row 
# In[86]:



import seaborn as sns
sns.relplot(
    data=df,
    x="depth", y="nst", hue='continent', palette = "bright"
)


# In[87]:


import plotly.express as px
fig = px.scatter(df, x="depth", y="nst", color='continent', size= 'magnitude')
fig.show()


# In[ ]:


#df.drop('alert', axis=1, inplace=True)
#df.drop('subnational', axis=1, inplace=True)
#df.drop('city', axis=1, inplace=True)
#df.drop('postcode', axis=1, inplace=True)
#df.drop('what3words', axis=1, inplace=True);
#df.drop('country', axis=1, inplace=True);

#print(df.isnull().sum())


# In[ ]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[69]:


# plotting scatterplot with histograms for features total bill and tip.

sns.jointplot(data=df, x= 'magnitude', y='mmi',hue='tsunami',sizes='felt' )


# In[84]:


#add column month
df['month'] = df['date'].dt.month
df.head()


# In[90]:


import plotly.express as px

fig = px.histogram(df, y="type", animation_frame="month",
            range_x=[0,200], color='type')

fig.show()


# In[ ]:




