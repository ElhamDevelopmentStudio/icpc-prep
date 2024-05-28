"""
from page 202 of comp prog handbook

x mod m = x * ( x ^ - 1 ) mod m = 1


"""

def x_mod_m(x,m):
    return x % m

def x_inverse_mod_m(x,m):
    return x * ( x ** - 1) % m


print(x_mod_m(10,2))
print(x_inverse_mod_m(10,2))
