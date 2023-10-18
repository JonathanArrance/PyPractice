#Count up the instances of the highest value in the array


array = [4,4,5,3,7,1,1,8,8,8]

m = max(sorted(array))

count = 0
for x in array:
    if m == x:
        count += 1

print(count)