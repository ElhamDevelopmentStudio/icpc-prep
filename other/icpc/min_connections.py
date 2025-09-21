import heapq

def solve(conn,number_of_points):
    distance = {node:float("-inf") for node in range(number_of_points)}
    distance[0] = 0 
    queue = [(0,0)]
    total_cost = 0
    visited = set()
    print(conn)
    while len(visited) < number_of_points:
        print(f"current queu is {queue}")
        curr_point,curr_node = heapq.heappop(queue)

        if curr_node in visited:
            continue



        visited.add(curr_node)
        total_cost += curr_point


        for next_node,next_point in conn.get(curr_node,[]):
            heapq.heappush(queue,(next_point,next_node))
            distance[next_node] = next_point 
    

    return total_cost 



for _ in range(int(input())):
    number_of_points,number_of_connections = list(map(int,input().split()))
    target = number_of_points -1 
    conn = {}
    for _ in range(number_of_connections):
        a,b,point = list(map(int,input().split()))
        if conn.get(a,None):
            conn[a].append((b,point))
        else:
            conn[a] = [(b,point)]
        if conn.get(b,None):
            conn[b].append((a,point))
        else:
            conn[b] = [(a,point)]
    res = solve(conn,number_of_points)
    print(res)
