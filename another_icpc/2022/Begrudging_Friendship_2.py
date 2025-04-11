from io import StringIO
import sys



input_string = """4
1 -3 2 1
"""

sys.stdin = StringIO(input_string)



k = int(input())
meals = list(map(int,input().split()))


l = min(meals)
meals.remove(l)
k = sum(meals)

print(k-l)



