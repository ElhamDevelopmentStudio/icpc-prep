from math import factorial

def modular_inverse(a, m):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    g, x, _ = extended_gcd(a, m)
    
    if g != 1:
        return None  
    else:
        return x % m  

def I(n,k):
    res = modular_inverse(k**2,n)
    if not res:
        return 0
    return res

def S(n):
    res = 0
    for i in range(n):
        res += I(n,i)
    return res


def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def solve(l,m):
    m_fact = factorial(m)
    #print(m_fact)
    res = 0
    for i in range(1,l+1):
        if m_fact % i == 0:
            res += S(i) % i
    #print(f"{res}\n")
    return res % 998244353

l,m = list(map(int,input().split()))

print(solve(l,m))



