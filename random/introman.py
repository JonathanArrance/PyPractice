def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    if num < 1 or  num >=3999:
        return None

    nums = str(num)
    #make a hash table
    first = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:"DC",700:"DCC",800:"DCCC",900:"CM",1000:'M',2000:'MM',3000:'MMM'}

    length = len(nums)
    out = []
    for x in range(length):
        #there is an issue here
        length = length - 1
        a = int(nums[x]) * (10 ** length)
        out.append(a)
    
    st = []
    for o in out:
        try:
            st.append(first[int(o)])
        except Exception as e:
            print(e)
    
    return "".join(st)

for x in range(2000):
    print(f'Here is X: {x}')
    print(f'Here is Roman {intToRoman(x)}')