#!/usr/bin/env python3
# Author ID: msingh869

#!/usr/bin/env python3

# Author ID: YOUR_SENECA_ID

def is_digits(sobj):
    return sobj.isdigit()


# Main Program
if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
