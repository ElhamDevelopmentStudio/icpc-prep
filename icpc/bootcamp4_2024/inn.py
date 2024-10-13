import sys
from io import StringIO
from collections import defaultdict

test_input = """5
1 1 2 3
"""

sys.stdin = StringIO(test_input)


n = int(input())
subs = list(map(int,input().split()))

res = []

dist = defaultdict(list)

for i in range(len(subs)):
    dist[subs[i]].append(i+2)


for i in range(1,n+1):
    stack = [i]
    count = 0

    while stack:
        curr_node = stack.pop()
        for neigh in dist.get(curr_node,[]):
            count += 1
            stack.append(neigh)

    res.append(count)



dfs_res = [0] * (n + 1)

def dfs(node):
    count = 0

    for subs in dist.get(node,[]):
        count += 1 + dfs(subs)

    dfs_res[node] = count

    return count

dfs(1)
print(*dfs_res[1:])


print(*res)
