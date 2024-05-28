"""
from page 210 of comp prog handbook

a catalan number equals the number of valid parantheses
that consists of n left and n right equals parentheses

the formula for it is :

            (n*2)!
C(n) = ---------------
           (n+1)!n!


for ex: C(3) = 5
"""

fact = lambda x : 1 if x < 2 else x * fact(x-1)

def main(n):
    upper = fact(2*n)
    lower = fact(n+1)*fact(n)
    return upper//lower


if __name__ == "__main__":
    n = 3
    res = main(n)
    print(res)
