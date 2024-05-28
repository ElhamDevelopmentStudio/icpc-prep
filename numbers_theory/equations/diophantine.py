"""
from comp prog page 204

to solve the equation ax + by = c where a , b , c are constants and we have to find the x and y

when c is divisible by gcd(a,b) we can solve the probelm with ax + by = gcd(a,b)

"""


def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def diophantine_equation(a, b, c):
    gcd, x, y = extended_euclidean(a, b)
    if c % gcd != 0:
        print("No integer solution exists.")
    else:
        x = x * (c // gcd)
        y = y * (c // gcd)
        # just to make sure that it is matches the formula
        # print((a*x) + (b*y) == c)
        print(f"x = {x}, y = {y}")

diophantine_equation(39, 15, 12)


