
# coding: utf-8

# In[1]:

# For loops


# In[3]:

list = [1,2,3,4,5] 

for i in list:
    print(i)


# In[4]:

list = ['a', 'b', 'c']

for a in list:
    print(a)


# In[5]:

list


# In[7]:

list = [1,2,3,4, 5] 

list_sum = 0

for a in list:
    list_sum += a;
    #list_sum = list_sum + a;
    
list_sum


# In[8]:

list = [(2,4), (6,8)]
for i in list:
    print(i)


# In[11]:

dict = {'k':'va1', 'k2':'val2'}
for item in dict:
    print(dict[item])

