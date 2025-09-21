import collections


def spfa(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    queue = collections.deque()
    queue.append(source)

    while queue:
        node = queue.pop()
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                distance[neighbor] = distance[node] + graph[node][neighbor]
                queue.append(neighbor)

    return distance

# Example usage:
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'B': 2, 'D': 1},
    'D': {'C': 1}
}

source = 'A'
print(spfa(graph, source))