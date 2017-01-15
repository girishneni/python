from collections import namedtuple

t = (1,2,3)
print(t[0])

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Lab', name='Sam')
frank = Dog(age=3, breed='Shepard', name='Frank')

print(sam)

print(frank)

print(sam.age)

print(sam.breed)

print(sam.name)

print(sam[0])