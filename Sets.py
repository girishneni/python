
# coding: utf-8

# In[1]:

# Sets and Boolean


# In[4]:

x = set()


# In[7]:

x.add(1)


# In[8]:

x


# In[10]:

x.add(2)


# In[11]:

x.add(3)


# In[12]:

x


# In[13]:

x.add(2)


# In[14]:

x


# In[16]:

ch = set()
ch = ['a','a','b','c','d','e','e']
ch


# In[17]:

ch.add('a')


# In[19]:

ch = set()
ch.add('a')
ch.add('a')
ch.add('b')
ch.add('a')
ch


# In[20]:

# Set Operations


# In[21]:

ch


# In[22]:

ch.clear()


# In[23]:

ch


# In[24]:

x


# In[25]:

y = x.copy()
y


# In[26]:

y


# In[27]:

x


# In[28]:

x.addd(4)


# In[29]:

x.add(4)
x


# In[30]:

y


# In[31]:

x.difference(y)


# In[33]:

set1 = {1,2,3}
set2 = {1,4,5}


# In[34]:

set1


# In[35]:

set2


# In[38]:

set1.difference_update(set2) # it updates set1 with the difference of both sets


# In[39]:

set1


# In[40]:

set1.add(1)


# In[41]:

set2.difference_update(set1)


# In[ ]:




# In[ ]:




# In[42]:

set2


# In[43]:

#discard
set1


# In[44]:

set1.discard(3)


# In[45]:

set1


# In[47]:

#intersecti2n

set2.add(1)
set2.add(2)
set2


# In[48]:

set1


# In[49]:

set1.intersection(set2)


# In[50]:

set1.issubset(set2)


# In[51]:

set2.issubset(set1)


# In[52]:

set2.issuperset(set1)


# In[53]:

#symmetric_difference
set1
set2


# In[54]:

set1


# In[55]:

set1.symmetric_difference(set2)


# In[56]:

set1


# In[57]:

set2.symmetric_difference(set1)


# In[58]:

set1.union(set2) # no duplicates


# In[59]:

set1.update(set2)


# In[60]:

set1

