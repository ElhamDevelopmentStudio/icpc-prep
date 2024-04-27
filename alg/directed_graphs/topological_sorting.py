def topological_sort(graph):
    """
    Performs a topological sort on a directed acyclic graph (DAG) using DFS and a stack.

    Args:
        graph: A dictionary representing the graph, where each key is a node and
            each value is a list of its neighbors.

    Returns:
        A list of nodes in topological order.
    """
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]


# graph = {
#     1 : [2],
#     2 : [3],
#     3 : [6],
#     4 : [1,5],
#     5 : [2,3]
# }
graph = {
    1 : [2],
    2 : [3],
    3 : [5,6],
    4 : [1,5],
    5 : [2,3]
}

# res = solve(graph,1)
res = topological_sort(graph)
print(res)