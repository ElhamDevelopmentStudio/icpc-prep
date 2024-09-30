"""
given an integer u should return the reverse

input : 321
output : 123

input2 : -600
output : -6
"""


num = input()
isManfi = False

if num[0] == "-": isManfi = True

if not isManfi:
    print(num[::-1])
else:
    num = num[1:]
    result = int(num[::-1])
    print(f"-{result}")


