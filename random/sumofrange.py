def add_it_up(inval):
    total = 0
    x = 0
    if not isinstance(inval,int):
        return total
    
    while x <= inval:
        total = total + x
        x += 1
    return total


ints = [1,4,5,7,9,'blah']

for i in ints:
    print(add_it_up(i))