def dijkstra(graph, startNode, goalNode):
  distances = {}
  for node in graph:
    distances[node] = float("inf")
  distances[startNode] = 0
  visited = set()

  while True:
    currentNode = None
    minDistance = float("inf")

    for node in graph:
      if node not in visited and distances[node] < minDistance:
        minDistance = distances[node]
        currentNode = node
    
    if currentNode is None:
      break

    visited.add(currentNode)
      
    for neighbor, cost in graph[currentNode].items():
      if neighbor not in visited:
        distance = distances[currentNode] + cost
        if distance < distances[neighbor]:
          distances[neighbor] = distance
  
  return distances[goalNode]
      


for _ in range(int(input())):
  numOfNodes = int(input())
  startNode, goalNode, totalConnection = list(map(int,input().split()))
  graph = {}
  for i in range(numOfNodes):
    graph[i+1] = {}
  for i in range(totalConnection):
    node1, node2, cost = list(map(int, input().split()))

    graph[node1][node2] = cost
    graph[node2][node1] = cost



  print(dijkstra(graph, startNode, goalNode))