

# my_file = open('sample.txt','w+')
#
# my_file.write('this is a new line')
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readlines())

# writing to a file

#my_file = open("test.txt", "w+")
# my_file.write('This is a new line')
# my_file.write('This is a second line')
#
# print(my_file.read())

# Iterate through files
for line in open("test.txt"):
    print(line)

for line in open("sample.txt"):
    print(line)


# StringIO
msg = "this is a normal message"

f = StringIO.StringIO(msg)

f.read()
f.write()
