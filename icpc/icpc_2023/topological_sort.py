from collections import defaultdict
import sys
from io import StringIO


input_ = """1
5
1 2
1 3
3 2
4 2
4 3
1,2,3,4
"""

"""




"""



sys.stdin = StringIO(input_)

def topological_sort(graph,jobs):
    visited = {key:0 for key in jobs} 
    result = []

    def dfs(node):
        visited[node] = 1 
        for neighbor in graph.get(node,[]):
            if visited[neighbor] == 1:
                return False 
            elif visited[neighbor] != 2:
                dfs(neighbor)
        visited[node] = 2
        result.append(node)

    for node in graph:
        if visited[node] != 2:
            dfs(node)
    return result[::-1]



for _ in range(int(input())):
    number_of_jobs = int(input())
    graph = defaultdict(list)
    for _ in range(number_of_jobs):
        a,b = list(map(int,input().split()))
        graph[a].append(b)
    jobs = list(map(int,input().split(",")))
    res = topological_sort(graph,jobs)
    if not res:
        print("Impossible")
    else:
        print(",".join(map(str,res)))

