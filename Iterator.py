
# coding: utf-8

# In[2]:

x = ['a','c']
y = len(x)
print(y)
while y > 0:
    if(x[y-1] == 'c'):
        print(x[y-1])
        y-=1
        break;

i =0;
x = ['a','c']
while i < len(x):
    if(x[i] == 'c'):
        print(x[i])
    i+=1
        
    


# In[3]:

list = [1,2,3,43] 
for i in list:
    print(i)


# In[4]:

iterator = iter(list)
next(iterator)


# In[8]:

next(iterator)


# In[9]:

list = ['abc', 'def','ghi']
strIterator = iter(list)
next(strIterator)


# In[ ]:



