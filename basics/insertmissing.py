#take a list of integers and insert the missing values.
#the values will not go above 20

#psudo
'''
look at the values in the list
sort the values ascending

if i+1 is > 1 more than i, insert v + 1 in i+1

i+1 will be i test the value 

if the list will have values greater than 20 raise Exception
'''


array = [0,2,3,4,7,8,9,10,13,15,18,20]
array = sorted(array)
#print(array)
#if array[-1]:
#   raise Exception('Out of bounds.')

#res = list(set(range(max(array) + 1)) - set(array))
print(max(array) + 1)
print(range(max(array) + 1))
print(set(array))
print(set(range(max(array) + 1)) - set(array))

#out = sorted(array + res)
#print(out)