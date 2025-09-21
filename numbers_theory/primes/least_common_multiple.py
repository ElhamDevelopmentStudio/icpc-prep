"""

a*b = lcm(a,b)*gcd(a,b)

so then:


                 a*b
lcm(a,b) =  -------------
               gcd(a,b)


"""

import functools
from typing import List

def gcd(a : int,b: int) -> int:
    if b == 0: return a
    return gcd(b,a%b)


def lcm(
    a : int,
    b : int
) -> int:
    upper = a*b
    lower = gcd(a,b)
    #print(upper)
    #print(lower)
    return upper//lower


def lcms(
    nums : List[int]
) -> int:
    return functools.reduce(lcm,nums)

print(
    lcms(
        list(map(int,input().split()))
    )
)
