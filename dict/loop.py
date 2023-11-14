#we need to loop throug a dictionary and do the following
#1. print keys
#2. print vals

d = {'val1':1,'val2':2,'val3':3,"val4":4}

for key,value in d.items():
    print(f'I am a key: {key}')
    print(f'I am a value: {value}')

#get a list of the keys
print(f'This is a list of keys {d.keys()}')

#get a list of the values
print(f'This is a list of values {d.values()}')