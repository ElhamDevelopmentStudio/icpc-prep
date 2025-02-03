import heapq

def dijkstra(graph, start, goalNode):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[goalNode]


for _ in range(int(input())):
    numOfNodes = int(input())
    startNode, goalNode, totalConnection = list(map(int, input().split()))
    graph = {}

    for i in range(1, numOfNodes + 1):
        graph[i] = {}

    for i in range(totalConnection):
        node1, node2, cost = list(map(int, input().split()))
        graph[node1][node2] = cost
        graph[node2][node1] = cost
        

            

    distances = dijkstra(graph, startNode, goalNode)
    print("Shortest distance:", distances)

    
