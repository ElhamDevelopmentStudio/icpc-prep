def bellman_ford(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[node] + graph[node][neighbor] < distance[neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]

    for node in graph:
        for neighbor in graph[node]:
            if distance[node] + graph[node][neighbor] < distance[neighbor]:
                print("Graph contains a negative weight cycle")
                return

    return distance

# Example usage:
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'B': 2, 'D': 1},
    'D': {'C': 1}
}

source = 'A'
print(bellman_ford(graph, source))