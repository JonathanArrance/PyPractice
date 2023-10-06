#for loop practice
def list_total(nums)->str:
    #build a for loop that will add the values in an list
    total = 0
    for n in nums:
        total = n + total

    return f'The totla of the list vals in {total}'

def list_evens(nums):
    #list only the evens
    out = []
    for n in nums:
        if (n % 2) == 0:
            out.append(str(n))
    
    return f'The even numbers are {",".join(out)}'

def list_odds(nums):
    #list only the odds
    out = []
    for n in nums:
        if (n % 2) > 0:
            out.append(str(n))
    
    return f'The odd numbers are {",".join(out)}'

def sorted_odds_evens(nums):
    #create a dict that holds the sorted values from least to greates
    # {'odd':[sorted],'even':[sorted]}
    odds = []
    evens = []
    for n in nums:
        if (n%2) == 0:
            evens.append(n)
        else:
            odds.append(n)
    
    out = {'odds':sorted(odds),'evens':sorted(evens)}
    return f'The sorted evens and odds are {str(out)}'


def sorted_fill_in_missing_vals(nums):
    


nums = [9,3,6,1,8,3,2,5,7,10,11,12,19,17,20]
print(list_total(nums) + "\n")
print(list_evens(nums) + "\n")
print(list_odds(nums) + "\n")
print(sorted_odds_evens(nums) + "\n")