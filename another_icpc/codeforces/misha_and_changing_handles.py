import sys
from io import StringIO

input_string = """5
Misha ILoveCodeforces
Vasya Petrov
Petrov VasyaPetrov123
ILoveCodeforces MikeMirzayanov
Petya Ivanov
"""

sys.stdin = StringIO(input_string)

n = int(input())

mapping = {}

for _ in range(n):
    old,new = input().split()
    mapping[old] = new


visited = set()
count = 0
result = []
for name in mapping.keys():
    if name not in visited:
        count += 1
        original = name
        while mapping.get(original,None):
            visited.add(original)
            original = mapping[original]
        result.append((name,original))
print(count)
for r in result:
    print(r[0],r[1])

