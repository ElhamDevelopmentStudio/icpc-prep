"""
seieve's impl of prime , 
preprocess the table from 2 -> n
if the res[i] is 0 then i is prime
otherwise in res[i] resides atleast one prime factor of i
"""
def sieve(n):
    res = [0] * (n+1)
    for x in range(2,n+1):
        if res[x] != 0: continue
        u = 2*x 
        while u <= n:
            res[u] = x
            u+=x

    return res
n = 20
res = sieve(n)
print(res[2:])
