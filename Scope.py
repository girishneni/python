
# coding: utf-8

# In[3]:

print('hi')


# In[6]:

# Local scope: with in a function
def func():
    x = 10
    print(x)

def func1():
    y = 10;
    print(x)


# In[15]:

# Enclsoing scope: bnetween functions: Nested functions


name = 'hello'

def greet() :  #function1
    name = 'world'
    
    def hello():   # nested function
        print('Welcome, '+name)
    
    hello()
    

greet()


# In[12]:

# global scope

x = 50 

def func():
    global x
    print('value of x:', x)
    
    x = 30
    print('value of x:', x)
        
func()


# In[ ]:




# In[13]:

str = 'hello world'
print(len(str))

