"""
from page 208 of comp prog handbook

given a n of 5 and k of 3 find their binomial coeffecient

n means the combinations will be from 1-5 and since the formula for finding the number of subsets is

2^n-1 then : the number of combinations is 2^4 = 16

so the question is how many of those contains 3

the given formula for that is


              n!
c(n,k) = ---------------
            k!(n-k)!

for ex: c(5,3) = 10
"""


fact = lambda x:  1 if x < 2 else x * fact(x-1)

def main(n,k):
    upper = fact(n)
    lower = fact(k) * fact(n-k)
    return upper // lower


if __name__ == "__main__":
    n = 5
    k = 3
    res = main(n,k)
    print(res)




