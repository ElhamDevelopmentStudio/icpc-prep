import heapq

def prim(graph, start):
    mst = []
    visited = set()
    pq = [(0, start)]
    while pq:
        curr_weight, curr_node = heapq.heappop(pq)
        if curr_node in visited:
            continue
        visited.add(curr_node)
        for neigh, neigh_weight in graph[curr_node]:
            if neigh not in visited:
                heapq.heappush(pq, (neigh_weight + curr_weight, neigh))
                mst.append((curr_node, neigh, neigh_weight))
    return mst


# Define the graph as an adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}

# Define the expected minimum spanning tree
expected_mst = [
    ('A', 'B', 2),
    ('B', 'C', 1),
    ('C', 'D', 2)
]
import pprint
res = prim(graph,'A')
pprint.pp(res)