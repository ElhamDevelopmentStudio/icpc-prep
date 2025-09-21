from collections import deque

def bfs(arr,start):
    visisted = set()
    distance = []
    distance[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()

        for neigh in arr[node]:
            if neigh in visisted : continue
            visisted.add(neigh)
            distance[neigh] = distance[node] + 1
            queue.append(neigh)


