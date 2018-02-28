
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from numpy.random import randn


# In[3]:


np.random.seed(101)


# In[4]:


df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['w','X','Y','Z'])


# In[5]:


df


# In[8]:


df['w']


# In[9]:


type(df["w"])


# In[10]:


type(df)


# In[17]:


df['w']


# In[19]:


df[['w','Y']]


# In[21]:


df['new'] = df['w']+ df['Y']


# In[22]:


df


# In[29]:


df.drop('new',axis=1,inplace=True)


# In[30]:


df


# In[34]:


df.drop('E',axis =0,inplace=True)


# In[35]:


df


# In[36]:


df.shape


# In[37]:


df.loc['A']


# In[41]:


df.iloc[0]


# In[42]:


df.loc['B','Y']


# In[48]:


df.loc[['A','B'],['w','Y']]


# In[49]:


df>0


# In[51]:


df['w']>0


# In[52]:


df[df['w']>0]


# In[53]:


df[df['Z']<0]


# In[55]:


resultdf = df[df['w']>0]


# In[56]:


resultdf ['X']


# In[60]:


df[df['Z']<0][['w','Y']]


# In[61]:


boolser = df['w']>0
result = df[boolser]
result[['Y','X']]


# In[69]:


df[(df['w']<0) | (df['Y']>0)]


# In[70]:


df[(df['w']<0) & (df['Y']>0)]


# In[72]:


df.reset_index()


# In[74]:


df


# In[78]:


newind = 'CA NY WY CO'.split()


# In[79]:


newind


# In[80]:


df['States'] = newind


# In[81]:


df


# In[82]:


df.set_index('States')


# In[83]:





# In[ ]:




