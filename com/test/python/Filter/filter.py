# filter : function, list

#filter(function, sequence)

# function should return boolean value: true or false

# result of this filter would be only the list with which this function has returned true

def even_check(num):
    if(num %2 == 0 ):
        return True

numbersList = range(20) # 0 to 20

d = filter(even_check, numbersList)

for item in d:
    print(item)
