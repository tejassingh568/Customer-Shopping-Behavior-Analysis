#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas
print(pandas.__version__)


# In[3]:


import pandas as pd
df = pd.read_csv(r"C:\Users\My Pc\Downloads\customer_shopping_behavior.csv")
df.head()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[15]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[16]:


df.isnull().sum()


# In[8]:


df.columns= df.columns.str.lower()
df.columns= df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[9]:


df.columns


# In[10]:


# create a new column age group
labels = ['Young Adult','Adult','Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'], q=4 ,labels = labels)
df[['age','age_group']].head(10)


# In[31]:





# In[11]:


frequency_mapping = {'Fortnightly' : 14, 'Weekly':7,'Monthly':30,'Quarterly':90,'Bi-Weekly':14,'Annually':365,'Every 3 Months':90}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[39]:


df.head()


# In[12]:


(df['discount_applied']==df['promo_code_used']).all()


# In[13]:


df['discount_applied'].dtype


# In[14]:


df= df.drop('promo_code_used',axis=1)


# In[15]:


df.columns


# In[16]:





