#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy  as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv('Export-Data.csv', encoding='unicode_escape', low_memory=False)


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.drop(['Policy','Remarks'],axis = 1, inplace=True)


# In[7]:


pd.isnull(df).sum()


# In[8]:


df.shape


# In[9]:


df.dropna(inplace=True)


# In[10]:


df.describe()


# ## EXPLORATORY DATA ANALYSIS

# In[11]:


df.columns


# In[12]:


ax = sns.countplot(x = 'Seller Country',data = df) 

for bars in ax.containers:
    ax.bar_label(bars)


# In[13]:


df.groupby(['Seller Country'], as_index = False)['Quantity'].sum().sort_values(by='Quantity',ascending=False)


# In[14]:


sales_Seller= df.groupby(['Seller Country'], as_index = False)['Quantity'].sum().sort_values(by='Quantity',ascending=False)

sns.barplot(x = 'Seller Country',y='Quantity' ,data=sales_Seller)


# In[15]:


df.columns


# ## Buyer country

# In[16]:


Export_BuyerCountry = df. groupby(['BuyerCountry'], as_index=False)['Quantity'].sum().sort_values(by='Quantity', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = Export_BuyerCountry, x= 'BuyerCountry' , y='Quantity')


# ## HSCODES
# 

# In[17]:


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('HS Codes')['Quantity'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# In[18]:


EXPORT = df.groupby(['HS Codes'], as_index=False)['Quantity'].sum().sort_values(by='Quantity', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = EXPORT, x = 'HS Codes',y= 'Quantity')

