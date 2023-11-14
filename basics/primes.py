#print all of the prime numners up to a given number
"""
What is a prime?
Prime numbers are numbers greater than 1 that only have two factors, 1 and the number itself.

2 = 2 x 1 - Prime
3 = 3 x 1 - Prime
4 = 2 x 2 and 4 x 1 - Not Prime
5 = 5 x 1 - Prime
6 = 6 x 1 and 3 x 2 - Not Prime
etc...
"""

def primes(num):
    
    if num == 1:
        return(f'{num} is not calculated.')
    if num == 2:
        return(f'{num} is prime.')
    
    #take mod of the number
    for n in range(2, int(num/2)+1):
        if num % n == 0:
            return(f'{num} is not prime.')
    return(f'{num} is prime.')

nums = 20
x = 1
while x <= nums:
    print(primes(x))
    x += 1