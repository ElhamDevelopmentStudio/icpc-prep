for i in range(int(input())):

    numNodes = int(input())
    startNode, goalNode, numOfConnections = map(int, input().split())

    graph = {}
    for node in range(1, numNodes+1):
        graph[node] = {}

    for j in range(numOfConnections):
        node1, node2, cost = map(int, input().split())
        graph[node1][node2] = cost
        graph[node2][node1] = cost
  
    distances = {}
    for node in graph:
        distances[node] = float("inf")

    distances[startNode] = 0

    visited = set()

    while True:

        minDist = float("inf")
        u = None
        for node in graph:
            if node not in visited and distances[node] < minDist:
                u = node
                minDist = distances[node]

        if u is None:
            break
        
        visited.add(u)

        for v, cost in graph[u].items():
            if v not in visited:
                newDist = distances[u] + cost
                if newDist < distances[v]:
                    distances[v] = newDist

    print(distances[goalNode])
