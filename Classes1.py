
# coding: utf-8

# In[2]:

print(type(1))


# In[3]:

print(type([]))


# In[4]:

print(type(()))


# In[5]:

print(type({}))


# In[10]:

class Dog():
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed = 'Lab')
frank = Dog(breed = 'Huskie')


# In[ ]:




# In[11]:

sam.breed


# In[12]:

frank.breed


# In[22]:

class Dog():
    
    species = 'mammal' #data attributes
    
    def __init__(self, breed, name):  #methods
        self.breed = breed
        self.name = name


# In[14]:

sam = Dog('Lab', 'sam')


# In[15]:

sam.name


# In[16]:

sam.breed


# In[17]:

sam.species


# In[19]:

frank = Dog('Huskie', 'frank')
frank.name


# In[20]:

frank.breed


# In[21]:

frank.species

