#Write a program to check if two arrays are equal.

def value_equal(a1,a2)->str:
    if len(a1) == len(a2) == 0:
        return 'Not equal'
    
    T1 = 0
    T2 = 0
    for x in a1:
        T1 += x
    
    for x in a2:
        T2 += x
    
    if T1 == T2:
        return 'Equal'
    else:
        return 'Not Equal'


def length_equal(a1,a2):
    if len(a1) == len(a2):
        return 'Equal Length'
    else:
        return 'Unequal Length'

def mirror(a1,a2):
    if a1 == a2:
        return 'Lists are equal'
    else:
        return 'Lists not equal'


def minmax(a):
    x = max(a)
    y = min(a)

    return {'min':y,'max':x}


array1 = [1,2,3,4,5]
array2 = [1,2,3,4,5]
array3 = [3,1,90,0,4,2,8,30]
print(value_equal(array1,array2))
print(length_equal(array1,array2))
print(mirror(array1,array2))

#How do you find the smallest and largest numbers in an unsorted array?
print(minmax(array3))


#A left rotation operation on an array of size n shifts each of the 
#array’s elements unit to the left. Given an integer, d, rotate the 
#array that many steps left and return the result.

boob = [1,5,5,7,8,10,3,2,4,9]
shift = 3
c=0
while c <= shift-1:
    c += 1
    boob.append(boob.pop(0))

print(boob)


#There is a collection of input strings and a collection of query strings. 
#For each query string, determine how many times it occurs in the list of input strings. 
#Return an array of the results.

instring = ['super cow going home','ding dong chicken','big bear going chicken','home is good']
query = ['cow','going','boo','home']

import re
result = []
for i in instring:
    for q in query:
        if re.search(q,i):
            result.append(q)
print(result)




