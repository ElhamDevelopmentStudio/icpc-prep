"""
given an array remove the duplicate and then print the new set's length

input : 4,5,6,7,6,5,4,1,2,9,8,8,7,6,5,0
output : 
0,1,2,4,5,6,7,8,9
7
"""



nums = list(map(int,input().split(",")))

set_nums = set(nums)
print(*set_nums)
print(len(nums)-len(set_nums))
