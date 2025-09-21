"""
#O(1) impl
import math
def fib(n : int) -> int:
    SQRT_5 = math.sqrt(5)
    phi = (1 + SQRT_5) / 2
    phi_bar = (1 - SQRT_5) / 2
    return (phi ** n - phi_bar ** n) / SQRT_5
num  = 7
res = int(fib(num))
assert res == 13 , "Wrong answer"
"""


"""
basic recursive fib impl
time : O(2^n)
space : O(n)
def fib(n : int) -> int:
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)
"""

"""
recursive with memo
time : O(2*n) or O(n)
space : O(n)
"""
def fib(n : int,memo : dict[int,int]) -> int:
    if n in memo : return memo[n]
    elif n <= 2 : return 1
    else:
        memo[n] =  fib(n-1,memo) + fib(n-2,memo)
        return memo[n]
    
if __name__ == "__main__":
    num = 7
    expected = 13
    res = int(fib(num,{}))
    assert res == expected,f"Wrong answer your answer was {res} when it should have been {expected}"
    print(res)

