"""
find if the given number is the power of 2
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & n-1 == 0)