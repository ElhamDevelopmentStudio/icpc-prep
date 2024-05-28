"""
from page 199 of comp prog handbook
find all prime factors of that number 
"""
def factors(n) -> list[int]:
    """
    finds the factors of the given number
    """
    f = []
    x = 2
    while x**x <= n:
        while n%x == 0:
            f.append(x)
            n /= x ; n = int(n)
        x+= 1
    if n > 1: f.append(n)
    return f

print(factors(10)) # 2 5
