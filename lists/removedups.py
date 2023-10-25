#How do you remove duplicates from an array in place?

'''
Python list of integers.
The input list will be unsorted 
End result - [1, 2, 3, 4, 6, 8, 9, 10, 15, 20]
'''

array = [6,6,8,3,2,9,10,4,20,2,1,6,1,8,15]

#sort the list
array = sorted(array)
#[1, 1, 2, 2, 3, 4, 6, 6, 6, 8, 8, 9, 10, 15, 20]
#python dict can not have a duplicate key
array = list(dict.fromkeys(array))

print(array)