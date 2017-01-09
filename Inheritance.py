
# coding: utf-8

# In[3]:

class Animal(object):
    def __init__(self):
        print("animal created")
        
    def whoAmI(self):
        print('Animal')
    
    def eat(self):
        print("Eating")


# In[6]:

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
    def whoAmI(self):
        print('Dog')
    
    def bark(self):
        print('woof')
    


# In[7]:

d = Dog()


# In[8]:

d.whoAmI()


# In[9]:

d.bark()


# In[10]:

d.eat()


# In[19]:

class Cat(Animal):
    
    name = 'cat'
    
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")
        
    def whoAmI(self):
        print('Cat')
    
    def bark(self):
        print('meaw')
    


# In[15]:

c = Cat()
c.eat()


# In[21]:

class Inherit(Cat):
    pass


# In[22]:

i = Inherit()
i.eat()
i.bark()
print(i.name)


# In[24]:

class MultipleInheritance(Dog, Cat):
    pass


# In[25]:

m = MultipleInheritance()
m.eat()


# In[26]:

print(m.name)


# In[27]:

print(m.bark())


# In[ ]:



