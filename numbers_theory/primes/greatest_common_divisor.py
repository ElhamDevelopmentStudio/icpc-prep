"""
from page 201 of comp prog handbook

gcd is the greatest number that divides both a and b


Euclid's algorithm:
    gcd(a,b) = gcd(b,a%b) 
    fox ex: gcd(24,36)



                 a*b
lcm(a,b) =  -------------
               gcd(a,b)
"""
from functools import reduce


def gcd(a : int,b: int) -> int:
    if b == 0: return a
    return gcd(b,a%b)

inputs = list(map(int,input().split()))
res = reduce(gcd,inputs)
print(res)
