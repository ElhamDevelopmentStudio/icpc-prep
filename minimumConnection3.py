outputs = []
def minimumConnection(graph):
  distance = {}
  for node in graph:
    distance[node] = float("inf")

  firstElement = list(graph) [0]
  distance[firstElement] = 0
  visited = set()
  
  while True:
    currentNode = None
    currentDistance = float("inf")

    for node in graph:
      if node not in visited and distance[node] < currentDistance:
        currentDistance = distance[node]
        currentNode = node
      
      if node is None:
        break

      visited.add(currentNode)

      for neighbor, cost in graph[currentNode].items():
        if neighbor not in visited:
          newDistance = distance[currentNode] + cost
          if distance[neighbor] > newDistance:
            distance[neighbor] = newDistance

    return distance
  
for _ in range(int(input())):
  nodes, numOfConnection = list(map(int, input().split()))

  graph = {}
  for i in range(numOfConnection):
    node1, node2, cost = list(map(int, input().split()))
    if node1 not in graph:
      graph[node1] = {}
    if node2 not in graph:
      graph[node2] = {}

    graph[node1][node2] = cost
    graph[node2][node1] = cost

  outputs.append(minimumConnection(graph))

for i in outputs:
  print(i)


