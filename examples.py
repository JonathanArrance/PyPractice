#remove duplicates from sorted array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return(1)

        for n in nums:
            if nums.count(n) > 1:
                print(nums)
                nums.pop(n)

        return(len(nums))

nums = [1,1,2,3,3,3,4,5,6,6,7,7,8,8,8,9]

[1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9]
[1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9]
[1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9]
[1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 8, 9]

[1,2,3,4,5,6,7,8,9]


#Roman numeral to integer

class Solution:
    def romanToInt(self, s: str) -> int:
        special = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        out = 0
        if s in special.keys():
            return special[s]

        elif s in nums.keys():
            return nums[s]

        else:
            for i in range(len(s)):
                if i < len(s) -1 and nums[s[i]] < nums[s[i+1]]:
                    out = out - nums[s[i]]
                else:
                    out = out + nums[s[i]]
        return out

s = "MCMXCIV"
out = 1994


#Palandrom number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negative numbers are not palandromes
        if x < 0:
            return False

        #0 to 9 are always palandromes - single digit
        if x >= 0 and x <= 9:
            return True

        raw = list(str(x))
        print(raw)
        #reverse the list
        rev = list(reversed(raw))
        print(rev)
        if raw == rev:
            return True
        else:
            return False

x = 121

['1', '2', '1']
['1', '2', '1']


#remove unwanted value from a List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #find the number of k element that are not val.
        #sort the list
        nums = sorted(nums)

        #base case if only 1 element
        if len(nums) == 1:
            if nums[0] != val:
                return 1

        yo = []
        for num in nums:
            if num == val:
                continue
            else:
                yo.append(num)
        return(yo)

l = [3,2,2,3]
yo = [2,2]

#same as above but in place removal of elemet
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index



    # increment the digits in a list
    def plusOne(self, digits: List[int]) -> List[int]:
            s= ''.join(map(str,digits))
            i=int(s)+1
            li=list(map(int,str(i)))
            return li

digits = [1,2,3]
out = [1,2,4]

digits = [9]
out = [1,0]

#search for an index position of a given target
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #base
        if target == 1 and nums[0] > 1:
            #insert 1 in index 0
            nums.insert(0,1)
            return 0

        elif target == 1 and nums[0] == 1:
            return 0

        elif target >= nums[-1]:
            nums.append(target)

        else:
            for index in range(0,len(nums),1):
                if target < nums[index]:
                    nums.insert(index,target)
                if target == nums[index]:
                    return index

        print(nums.index(target))
        return nums.index(target)

num = [1,2,3,4]
T=5
index = 4

num = [1,2,4,5]
T=3
index=2

#Find the lingth of the last word in a string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        out = s.split()

        return len(list(out[-1]))

s = "hello world"
out = 4

#move all 0's to the end of the List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 and nums[0] == 0:
            return [0]

        i = 0
        for index in range(len(nums)):
            if nums[index] != 0 and nums[i] == 0:
                nums[i],nums[index] = nums[index],nums[i]
            if nums[i] != 0:
                i += 1
s = [1,2,0,4,0,6]
out = [1,2,4,6,0,0]

s = [0]
out = [0]

#return true if there are dups in the list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return false

        if len(list(set(nums))) < len(nums):
            return True
        else:
            return False
l = [1,2,3,4,4]
out = True

l = [1,2,3,4]
out = False


#find the sqrt
class Solution:
    import math
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))


#modify nums1 in place and use slicing to remove last n number of zeros from nums1 and merge with nums2
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #handle the base case
        if len(nums1) == 1 and m == 1 and n == 0:
            nums1[0] = 1

        if len(nums2) == 1 and m == 0 and n == 1:
            nums1[0] = 1

        #take each list and pull out the zeros
        #look at the last entry is it 0?
        #print(nums1)
        #if nums1[-1] == 0:
        nums1 = nums1[:len(nums1)-m]

        #merge the 2 lists togehter the length should be n + m = total length
        if nums1 == n+m:
            nums1 = sorted(nums1+nums2)
            return nums1

#list comprehension
#convert all elements to uppercase
fruits = ["aplles","pears","peach"]
fruits = [fruits.upper() for fruit in fruits]

print(fruits)

[True,False,True,True,False]
out = [1 if b == True else 0 for b in bits]
out = [1,0,1,1,0]

s = "MyNameIsJon"
s = "".join([i if i.islower() else " " + i for i in s])

print(s)


#main - keeps imported modules from running needs to be there or code will
#run when imported.
if __name__ == "__main__":
    pass


#class example with functions and usage.
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor (initializer) method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Instance method
    def speak(self, sound):
        return f"{self.name} says {sound}!"

# Create instances (objects) of the Dog class
dog1 = Dog("Buddy", 2)
dog2 = Dog("Molly", 5)

# Access instance attributes and call methods
print(f"{dog1.name} is a {dog1.species}.")
print(dog2.description())
print(dog1.speak("Woof"))


#lambda - nameless anonymous functions
def f(x):
    return 3*x + 1

7

#lambda way
g = lambda x: 3*x + 1
g(2) = 7

lambda x1 x2 xN: expression to do work

#return last name in a list in alphabetic order
names = ["jon arrance", "Chris Wilson", "Keven Arrance"]
names.sort(key=lambda name: name.split(" ")[-1].lower())
names = ["jon arrance", "Keven Arrance", "Chris Wilson"]


#merge sort Example

#Merge Sort divides the input data into smaller halves recursively until it reaches the base case (arrays of size 1 or 0),
#and then it merges the sorted halves back together.
#This divide-and-conquer approach is what gives Merge Sort its efficiency.
#O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Split the array into two halves
        right_half = arr[mid:]

        # Recursive calls to sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print("Sorted list:", my_list)

#Selection Sort

#After running the code, you'll see the sorted list printed to the console. Selection Sort has a time complexity of O(n^2),
#where 'n' is the number of elements to be sorted,
#making it less efficient than some other sorting algorithms for larger datasets.

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted list:", my_list)


#Look for a value in a Binary search tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    if root is None or root.value == target:
        return root

    if target < root.value:
        # Search in the left subtree
        return search_bst(root.left, target)
    else:
        # Search in the right subtree
        return search_bst(root.right, target)

#EX.
# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

result = search_bst(root, 7)
if result:
    print(f"Value {result.value} found in the BST.")
else:
    print("Value not found in the BST.")
 
