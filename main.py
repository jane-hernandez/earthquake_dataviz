#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
url='https://raw.githubusercontent.com/jane-hernandez/earthquake_dataviz/main/earthquakeAPI_data.csv?token=GHSAT0AAAAAACBOABKJG7MIV37VBSCCUZMSZB5PNGA'
df= pd.read_csv(url)


# In[46]:


df


# In[47]:


print(df.isnull().sum())


# In[51]:


dfresult = df.dropna(subset=['continent'])
print(dfresult.isnull().sum())


# In[54]:


sns.relplot(
    data=dfresult,
    x="depth", y="nst", hue="continent", 
)


# In[ ]:


dfresult = df2.dropna(subset=['Population'])


# In[16]:


#df.drop('alert', axis=1, inplace=True)
#df.drop('subnational', axis=1, inplace=True)
#df.drop('city', axis=1, inplace=True)
#df.drop('postcode', axis=1, inplace=True)
#df.drop('what3words', axis=1, inplace=True);
#df.drop('country', axis=1, inplace=True);

#print(df.isnull().sum())


# In[24]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


# plotting scatterplot with histograms for features total bill and tip.

sns.jointplot(data=df, x= 'magnitude', y='mmi',hue='tsunami',sizes='felt' )


# In[41]:


#df[['placeonly', 'country']] = df['placeOnly'].str.split(',', expand=True)


# In[ ]:





# In[ ]:





# In[ ]:




