#revers an integer with the limitation that the int can not be over 32 bits long
#if it is 32 bits or more return 0
"""
-123 = -321
12344 = 44321
409804982908423 = 0
"""
def reverse(x):
    if(x.bit_length() >= 32):
        return 0

    n = str(x)
    reversed = 0
    if x < 0:
        n = n[1:]
        reversed = "-" + n[::-1]
    else:
        reversed = str(x)[::-1]

    if(int(reversed).bit_length() >= 32):
        return 0
    
    return int(reversed)

print(reverse(1484839))