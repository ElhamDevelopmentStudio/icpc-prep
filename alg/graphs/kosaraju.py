from collections import defaultdict

def kosaraju(graph):
    stack = []
    visited = [False] * (len(graph) + 1)

    def first_step(graph, v):
        if visited[v]:
            return
        visited[v] = True
        stack.append(v)
        print("Visiting node", v)
        for neigh in graph[v]:
            first_step(graph, neigh)

    for v in graph:
        if not visited[v]:
            first_step(graph, v)

    rev_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            rev_graph[v].append(u)

    visited = [False] * (len(graph) + 1)

    sccs = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            scc = []
            visited[v] = True
            scc.append(v)
            while stack and stack[-1] != v:
                scc.append(stack.pop())
            scc.append(stack.pop())
            sccs.append(scc)

    return sccs

graph = {
    1 : [2,4],
    2 : [1],
    3 : [2,7],
    4 : [],
    5 : [4],
    6 : [5,3],
    7 : [6]
}

res = kosaraju(graph)
print(res)