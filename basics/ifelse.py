
def simple() -> str:
    # simple if else
    blah = True
    if blah:
        return("blah is True")
    else:
        return("blah is False")


def check_len(input_list):

    x = len(input_list)

    if x >= 5:
        return x
    else:
        return f'List len {x}'


def elif_test(input_list):

    x = len(input_list)

    if x == 3:
        return f'The list length is 3'
    elif x == 8:
        return f'The list length is 8'
    elif x >= 5:
        return f'The list length is larger than 5'
    else:
        return f'Can not determin length'

def main():

    l = [1,2]

    print(f'The result of simple if/else: {simple()}')

    print(f'The length test: {check_len(l)}')

    print(f'The result of if/elif: {elif_test(l)}')


if __name__ == "__main__":
    main()