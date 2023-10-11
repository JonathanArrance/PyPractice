#imple try exccept
#IO error
try:
    o = open('myfile.txt')
except IOError as I:
    print(f'the was an excpetion: {I}')
    raise I


#simple excpet
try:
    x = 2
except Exception as e:
    print(f'x could not be set: {e}')
    print(e)

#try/except/finally
try:
    o = open('myfile.txt')
except IOError as I:
    print(f'the was an excpetion: {I}')
    raise I
finally:
    o.close()

#try/except/finally/else
try:
    o = open('myfile.txt')
except IOError as I:
    print(f'the was an excpetion: {I}')
    raise I
else:
    print('No errors happened')
finally:
    o.close()


#build your own Exception for try/except 
#extend the Excpetion class

class MyExcpet(Exception):
    pass

x = int(input('Enter number larger than 0'))
if x > 0:
    print("greater than 0")
else:
    raise MyExcpet
