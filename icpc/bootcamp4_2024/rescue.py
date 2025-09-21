import sys
from io import StringIO
from collections import deque, defaultdict

test_input = """6 7
1 2
1 3
2 4
2 5
3 5
4 6
5 6
1
"""
sys.stdin = StringIO(test_input)

nodes, edges = map(int, input().split())
conns = defaultdict(list)

for _ in range(edges):
    nodea, nodeb = map(int, input().split())
    conns[nodea].append(nodeb)
    conns[nodeb].append(nodea)

start = int(input())

dist = [float("inf")] * (nodes + 1)
dist[start] = 0

queue = deque([start])
while queue:
    node = queue.popleft()

    for neigh in conns[node]:
        if dist[node] + 1 < dist[neigh]:
            dist[neigh] = dist[node] + 1
            queue.append(neigh)


result = []
for r in dist[1:]:
    if r != float("inf"):
        result.append(r)
    else:
        result.append(r)
print(" ".join(map(str,result)))
