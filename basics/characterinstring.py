#How do you count the occurrence of a given character in a string?

st = 'Today is a good day'
f = 'o'

st = st.replace(" ","")

print(f'There are {st.count(f)} number of {f} in the string.')

#How do you print the first non-repeated character from a string
x = "ooofooppijjj"

char_count = {}
    
# Count occurrences of each character in the input string
for char in x:
    char_count[char] = char_count.get(char, 0) + 1

# Find the first non-repeating character
for char in x:
    if char_count[char] == 1:
        print(f'The first non repeated character: {char}')
        break

