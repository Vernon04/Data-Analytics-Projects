#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[61]:


df=pd.read_csv(r'D:\Data analytics\Datasets\top50.csv', encoding='latin-1',index_col=0)


# In[62]:


df.head().T


# In[63]:


df.columns


# In[64]:


df.info()


# In[65]:


df.describe()


# In[66]:


df['Length_mins']=np.round(df['Length.']/60,2)


# In[68]:


df.drop(['Length.'],axis=1,inplace=True)
df.head()


# In[69]:


sns.pairplot(data=df,kind='scatter')


# In[8]:


sns.countplot(x='Genre',data=df)
plt.xticks(
    rotation=90, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large'  
)


# In[9]:


fig=plt.figure(figsize=(12,8))
sns.countplot(x='Artist.Name',data=df)
plt.xticks(
    rotation=90, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large'  
)


# In[34]:


fig=plt.figure(figsize=(12,8))
sns.boxplot(x='Artist.Name',y='Popularity',data=df)
plt.xticks(
    rotation=90, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large'  
)


# In[11]:


df.shape[1]


# In[20]:


fig=plt.figure(figsize=(17,12))
c=df.corr()
sns.heatmap(c,annot=True)


# In[39]:


sns.jointplot(x='Beats.Per.Minute',y='Popularity',data=df,kind='kde')


# In[70]:


sns.boxplot(x='Length_mins',data=df)


# In[86]:


sns.jointplot(x='Beats.Per.Minute',y='Valence.',data=df,kind='kde')


# In[ ]:





# In[ ]:




