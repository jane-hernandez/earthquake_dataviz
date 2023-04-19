
#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
url='https://raw.githubusercontent.com/jane-hernandez/earthquake_dataviz/main/earthquakeAPI_data.csv?token=GHSAT0AAAAAACBOABKJDJ4PZUO7YNTW2J2MZB7TYOQ'
df= pd.read_csv(url)


# In[61]:


df


# In[64]:


print(df.isnull().sum())


# In[65]:


#dataframe dropping Column null values because couldn't find a way to create a column continent from 'place' or 'location'
dfresult = df.dropna(subset=['continent'])
print(dfresult.isnull().sum())


# In[86]:



import seaborn as sns
sns.relplot(
    data=df,
    x="depth", y="nst",size="magnitude", sizes=(20, 200), hue='continent'
)


# In[87]:


import plotly.express as px
fig = px.scatter(dfresult, x="depth", y="nst", color='continent', size= 'magnitude')
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




