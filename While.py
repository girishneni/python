
# coding: utf-8

# In[1]:

x = 0

while x <=5:
    print('value of x: ', x)
    x +=1
else:
    print('not in while')


# In[ ]:

# break, continue

#break: skips the current enclosing loop
#continue: goes to the top of the enclosing loop


# In[4]:

x = 0

while x <=5:
    x +=1
    if x ==3:
        print ('value of x: ', x)
    else:
        print('continue..')
        continue


# In[5]:

x = 0

while x <=5:
    x +=1
    if x ==3:
        print ('value of x: ', x)
        break
    else:
        print('continue..')
        continue


# In[ ]:

while True:
    


# In[12]:

list = [1,2,3,4,5,6,7,8,9]
 

for i in list:
    print(list[i])
    
    


# In[14]:

list = [1,2,3,4,5,6,7,8,9]
x = len(list)
while x > 0:
    print (x)
    x-=1


# In[ ]:

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
while i <= len(x):
    if(x[i] == 'c'):
        print(x[i])
    i+=1
        
        
        


# In[ ]:



