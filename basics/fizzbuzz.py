#take a set of number from 1-100 and if the number is divisable by 3 print fizz by 5 buzz and 
#if both print fizzbuzz. If not divisible print the number.

#"print everything on a single line"

#psedo
"""
th = None
fi = None
if i % 3 is 0 
    th = fizz
elif i % 5 is 0
    fi = buzz
else 
    print i

    
"""

def fizz(i):
    
    if i % 3 == 0 and i % 5 == 0:
        return ('FizzBuzz')
    elif i % 3 == 0:
        return ('fizz')
    elif i % 5 == 0:
        return ('buzz')

    else:
        return (str(i))

a = []
#O(n) runn time since it is linear. Takes longer to run as more numbers added.
for x in range(100):
    #fizz(x)
    a.append(fizz(x))
print(",".join(a))

