def prime(n) -> bool:
    if n < 2: return False

    x = 2
    while x**x <= n:
        if n%x == 0: return False
        x+=1

    return True

print(prime(10))
