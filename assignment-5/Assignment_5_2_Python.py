
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
data_out = pd.DataFrame(data=GradeList,columns=['Names','Grades','bsdegrees','msdegrees','phddegrees'])
data_out

data_out['Grades'].count() # number of values

data_out['bsdegrees'].count()


data_out['msdegrees'].count()



data_out['phddegrees'].count()




data_out['Grades'].mean() # arithmetic average





data_out['bsdegrees'].mean()




data_out['msdegrees'].mean()



data_out['phddegrees'].mean()





data_out['Grades'].std() # standard deviation





data_out['bsdegrees'].std()





data_out['msdegrees'].std()


# In[27]:


data_out['phddegrees'].std()


# In[8]:


data_out['Grades'].min() # minimum


# In[28]:


data_out['bsdegrees'].min()


# In[29]:


data_out['msdegrees'].min()


# In[30]:


data_out['phddegrees'].min()


# In[9]:


data_out['Grades'].max() # maximum


# In[31]:


data_out['bsdegrees'].max()


# In[32]:


data_out['msdegrees'].max()


# In[33]:


data_out['phddegrees'].max()


# In[10]:


data_out['Grades'].quantile(.25) # first quartile


# In[34]:


data_out['bsdegrees'].quantile(.25)


# In[35]:


data_out['msdegrees'].quantile(.25)


# In[36]:


data_out['phddegrees'].quantile(.25)


# In[11]:


data_out['Grades'].quantile(.5) # second quartile


# In[37]:


data_out['bsdegrees'].quantile(.5) 


# In[38]:


data_out['msdegrees'].quantile(.5) 


# In[39]:


data_out['phddegrees'].quantile(.5) 


# In[12]:


data_out['Grades'].quantile(.75) # third quartile


# In[40]:


data_out['bsdegrees'].quantile(.75)


# In[41]:


data_out['msdegrees'].quantile(.75)


# In[42]:


data_out['phddegrees'].quantile(.75)


# In[13]:


# computes the arithmetic average of a column
# mean = dividing the sum by the number of values
data_out['Grades'].mean()


# In[43]:


data_out['bsdegrees'].mean()


# In[44]:


data_out['msdegrees'].mean()


# In[45]:


data_out['phddegrees'].mean()


# In[14]:


# finds the median of the values in a column
# median = the middle value if they are sorted in order
data_out['Grades'].median()


# In[46]:


data_out['bsdegrees'].median()


# In[47]:


data_out['msdegrees'].median()


# In[48]:


data_out['phddegrees'].median()


# In[15]:


# finds the mode of the values in a column
# mode = the most common single value
data_out['Grades'].mode()


# In[50]:


data_out['bsdegrees'].mode()


# In[51]:


data_out['msdegrees'].mode()


# In[52]:


data_out['phddegrees'].mode()


# In[16]:


data_out.var()

