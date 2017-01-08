# try except usage
try:
    f = open('test.txt', 'w')
    f.write('this is to test try')
except IOError:
    print('Error: Could not find file or read data')

else:
    print('writen successfully')


# how python handles the exceptions
try:
    f = open('test.txt', 'r')
    f.write('this is to test try')
except IOError:
    print('Error: Could not find file or read data')

else:
    print('writen successfully')


try:
    f = open('test.txt', 'w')
    f.write('this is to test try')
    print("write to file is successful")
finally:
    print("Finally always executes!!")

# how python handles the exceptions
try:
    f = open('test.txt', 'r')
    f.write('this is to test try')
except IOError:
    print('exception occured')
else:
    print('generic handlers')
finally:
    print('finally is executed')
    f.close()