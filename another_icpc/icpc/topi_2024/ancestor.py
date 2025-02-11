import sys
from io import StringIO
from math import log2

input_string = """1
5 2 5
5 3
1 3
4 3
1 2
4 2
1 3
"""

sys.stdin = StringIO(input_string)

import sys
from math import log2

def solve():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])  # Number of test cases
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])  # Number of family members
        q = int(data[idx + 1])  # Number of queries
        r = int(data[idx + 2])  # Root of the tree
        idx += 3
        
        # Build the tree using adjacency list
        tree = [[] for _ in range(n + 1)]
        parent = [0] * (n + 1)  # Parent of each node
        parent[r] = -1  # Root has no parent
        
        for _ in range(n - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            tree[u].append(v)
            parent[v] = u  # v's parent is u
            idx += 2
        
        # Binary Lifting Table: up[node][j] = 2^j-th ancestor of node
        LOG = int(log2(n)) + 1
        up = [[-1] * LOG for _ in range(n + 1)]
        
        # Initialize 2^0-th ancestor (direct parent)
        for i in range(1, n + 1):
            up[i][0] = parent[i]
        
        # Fill the binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                if up[i][j - 1] != -1:
                    up[i][j] = up[up[i][j - 1]][j - 1]
        
        # Process queries
        for _ in range(q):
            u = int(data[idx])
            k = int(data[idx + 1])
            idx += 2
            
            # Find the k-th ancestor of u
            current = u
            for j in range(LOG):
                if k & (1 << j):  # If the j-th bit of k is set
                    current = up[current][j]
                    if current == -1:  # No ancestor exists
                        break
            
            results.append(current)
    
    # Print all results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

# Call the solve function
if __name__ == "__main__":
    solve()

"""

def kth_ancestor(node,k,up,LOG):
    current = node
    for j in range(LOG):
        if k & (1 << j):
            current = up[current][j]
            if current == -1:
                break
    return current


def solve():
    num_of_people,num_of_query,root = list(map(int,input().split()))
    tree = [[] for _ in range(num_of_people+1)]
    parents = [0] * (num_of_people+1)
    parents[root] = -1


    for _ in range(num_of_people-1):
        parent,child = list(map(int,input().split()))
        tree[parent].append(child)
        parents[child] = parent

    LOG = int(log2(num_of_people))+1
    up = [[-1] * LOG for _ in range(num_of_people+1)]
    
    for i in range(1,num_of_people+1):
        up[i][0] = parents[i]

    for j in range(1,LOG+1):
        for i in range(1,num_of_people+1):
            if up[i][j-1] != -1:
                up[i][j] = up[up[i][j-1]][j-1]
    
    for _ in range(num_of_query):
        node,k = list(map(int,input().split()))
        print(kth_ancestor(node,k,up,LOG))

for _ in range(int(input())):
    result = solve()
    exit(1)
"""

