
# coding: utf-8

# In[1]:

class Circle(object):
   
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def setRadius(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius


# In[4]:

c = Circle()
c.setRadius(2)
print('Radius is: ', c.getRadius())
print('Area is: :', c.area())


# In[6]:

d = Circle()
d.getRadius()
print(d.area())


# In[ ]:



