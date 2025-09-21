"""
given a number
for ex:
    13 
    count the number of 1s from 1 to 13

input : 13
output : 6
"""


num = int(input())
result = 0
for i in range(1,num+1):
    result += str(i).count("1")

print(result)
