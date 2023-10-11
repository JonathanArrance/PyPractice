#ceaser cipher

import string
 
def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    print(letters)
    mask = letters[shift_num:] + letters[:shift_num]
    print(mask)
    trantab = str.maketrans(letters, mask)
    print(trantab)
    return plain_text.translate(trantab)
    

shift_num = 18
plain_text = 'I love the juice'

print(caesar(plain_text,shift_num))