#create a dictionary that will grow up to a certain number of given values

"""
G = 5
Create a dictionary with values up to 5 added to it
Then print the values everytime a new val is added to we can see the dict grow.
Take a number in from the user
"""

import random

def grow(G):
    d = {}
    x = 0
    while x <= int(G):
        d["key"+str(x)] = "val"+str(x)
        print(d)
        x+=1

#now shrink the dictionary


G = input("How many values should be added? ")

grow(G)