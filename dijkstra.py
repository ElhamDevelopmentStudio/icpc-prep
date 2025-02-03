def dijkstra(graph, startNode):
  distances = {}
  for node in graph:
    distances[node] = float("inf")
  distances[startNode] = 0

  visited = set()

  while True:
    currentNode = None
    currentDistance = float("inf")

    for node in graph:
      if node not in visited and distances[node] < currentDistance:
        currentDistance = distances[node]
        currentNode = node
      
    if currentNode is None:
      break

    visited.add(currentNode)

    for neighbor, cost in graph[currentNode].items():
      if neighbor not in visited:
        distance = currentDistance + cost
        if distance < distances[neighbor]:
          distances[neighbor] = distance

  return distances


totalNumOfConnections = int(input())
startNode = int(input())

graph = {}
# dict = { 1: [(2,3) (3,4)]}
for i in range(totalNumOfConnections):
  node1, node2, cost = list(map(int, input().split()))
  if node1 not in graph:
    graph[node1] = {}
  if node2 not in graph:
    graph[node2] = {}
  graph[node1][node2] = cost
  graph[node2][node1] = cost


print(dijkstra(graph, startNode))

