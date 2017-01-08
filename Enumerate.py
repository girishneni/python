
# coding: utf-8

# In[2]:

#tuples 

list = [1,2,3]

list =(1,2,'a')

len(list)


# In[3]:

#enumerate
list = ['a', 'b', 'c']

for number, item in enumerate(list):
    print(number)
    print(item)



# In[ ]:


def enmerater(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n+=1

