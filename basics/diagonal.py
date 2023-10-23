#Given a square matrix, calculate the absolute difference between
#the sums of its diagonals. For example, the square matrix 
#ar = [1, 2, 3, 4, 5, 6 , 7, 8, 9], arranged in a 3×3 grid resembling a phone keypad.\
# the matrix has be an x by x array 
#1 2 3
#4 5 6
#7 8 9

# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16

#we will need to play a numbers game and count the number of indexs on each "line" of the matrix.
#Since a matrix in this case is even width and height and only 2 dimension we can do this with the square root.


import math

array = [1, 2, 3, 4, 5, 6 , 7, 8, 9]
s = int(math.sqrt(len(array)))
ld = 0
rd = 0
#
for ind in range(0,len(array),s+1):
    print(f'Looking at the index{ind}: right diag')
    ld += array[ind]
print(ld)

for ind in range(s-1,len(array),s-1):
    print(f'Looking at the index{ind}: left diag')
    rd += array[ind]
rd = rd - array[-1]
print(rd)


    