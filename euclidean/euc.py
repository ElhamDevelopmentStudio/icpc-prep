

def gcd(a, b):
  
  while b:
    a, b = a, a % b

  return a

def lcm(a, b):

  return a * b // gcd(a, b)

def example():
    """
    Example
    """
    print(gcd(12, 8)) # 4
    print(lcm(12, 8)) # 24


if __name__ == "__main__":
    example()
