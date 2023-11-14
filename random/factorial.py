#calculate the factorial of a list of integer values
"""
factorial is adding the all of the numbers in a series
"""

nums = [1,2,3,4,5,6,7,8]

t = 0

if len(nums) == 0:
    print(0)

for n in nums:
    t = t + n

print(t)


# do the same thing, but give the last integer value.
"""
Give the factorial up to the integer 8
"""

num = 8

if num == 0:
    print(0)

t = 0
x = 0
while x <= 8:
    t = x + t
    x += 1

print(t)