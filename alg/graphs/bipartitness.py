from collections import deque
def solve(graph : list[list[int]]) -> bool:
    n = len(graph)
    is_b = True
    queue = deque()
    sides = [-1] * n
    print(sides)
    for st in range(n):
        if sides[st] == -1:
            queue.append(st)
            sides[st] = 0
            while queue:
                v = queue.popleft()
                for u in graph[v]:
                    if sides[u] == -1:
                        sides[u] = sides[v] ^ 1
                        queue.append(u)
                    else:
                        is_b &= sides[u] != sides[v]

    return is_b

if __name__ == "__main__":
    graph = [
           [4,3]  ,   # 1
            [4,2] ,#2
            [5,1] ,#3
            [0] , #4
            [0,1],#5
            [2,4],#6
            ]

    res = solve(graph)
    print(res)
