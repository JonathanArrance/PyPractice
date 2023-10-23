#calculate the first N fibinachi numbers
"""
What is a fibinachi number?
0+1 = 1
0+1+2+3 = 6
0+1+2+3+4+5 = 15

Input N = 10 - Calculate the first 10 fibinachi numbers
Output Integer of calculated value
The numbers always start with 0
"""

def fib(val)->int:
    
    if val <= 1:
        return 0

    num = 0
    fib = 0
    l = []
    for x in range(0,val,1):
        l.append(num)
        num += 1
    
    for y in l:
        fib += y
    
    return fib

x = input("First N fibinachi numbers: ")
print(fib(int(x)))