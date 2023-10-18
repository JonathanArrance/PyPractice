#implement a simple bubble sort for an unsorted list

#pseudo
"""
l = [1,5,6,3,8,7,4,9,2,11,10]

loop over the list
if the value at n is less than n + 1 
then do nothing

if the value of n is greater than n + 1
then swap the value of n for n + 1

"""
def bubble(li):
    n = len(li)
    swap = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if li[j] > li[j + 1]:
                swap = True
                li[j], li[j + 1] = li[j + 1], li[j]
        if not swap:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return


li = [12,5,6,3,14,8,7,4,20,9,2,11,10]
bubble(li)

print(li)