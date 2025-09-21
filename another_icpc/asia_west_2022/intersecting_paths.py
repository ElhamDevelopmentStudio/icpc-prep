import sys
from io import StringIO
from collections import defaultdict,deque
sys.setrecursionlimit(2**20)
input_string  = """8 4
1 2
1 3
2 4
2 5
4 6
5 7
5 8
5 6
3 4
5 8
5 6
"""

sys.stdin = StringIO(input_string)



n,q = list(map(int,input().split()))

tree = defaultdict(list) 

for _ in range(n-1):
    a,b = list(map(int,input().split()))
    tree[a].append(b)
    tree[b].append(a)

def find_node(root,node):
    def dfs(current_node, current_path):
        current_path.append(current_node)
        
        if current_node == node:
            return current_path
        
        for child in tree.get(current_node, []):
            result = dfs(child, current_path.copy())  # Use a copy to avoid modifying the original path
            if result:  # If the target node is found, return the path
                return result
        
        # If the target node is not found in this branch, return None
        return None

    # Start the DFS from the root with an empty path
    return dfs(root, []) or []

def solve(s):
    if len(s) == 0:return 0
    res = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            ...


S = set()
for _ in range(q):
    a,b = list(map(int,input().split()))
    S.add((a,b))

from pprint import pp
pp(tree)
print(tree.get(5))
pp(find_node(5,6))

