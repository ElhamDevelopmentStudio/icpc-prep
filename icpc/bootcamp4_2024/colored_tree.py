import sys
from io import StringIO
from collections import defaultdict

test_input = """5 4
1 1 3 3
1 4 2 1 2
"""


"""
        1(1)

    2(4)       3(2)
            
        4(1)       5(2)


-1 -1 -1 1 3

"""

sys.stdin = StringIO(test_input)


number_of_vertices, number_of_colors = map(int, input().split())
parents = list(map(int, input().split()))
colors = list(map(int, input().split()))

tree = defaultdict(list)
for child, parent in enumerate(parents, start=2):
    tree[parent].append(child)

result = [-1] * (number_of_vertices + 1) 
recent_ancestor = {}  

def dfs(node):
    current_color = colors[node - 1]  
    previous_ancestor = recent_ancestor.get(current_color, None)

    recent_ancestor[current_color] = node

    result[node] = previous_ancestor if previous_ancestor is not None else -1

    for child in tree[node]:
        dfs(child)

    if previous_ancestor is None:
        del recent_ancestor[current_color]
    else:
        recent_ancestor[current_color] = previous_ancestor

dfs(1)

print(" ".join(map(str, result[1:])))



