import sys
from io import StringIO


input_string = """1
BGI,CDG,DEL,DOH,DSM,EWR,EYW,HND,ICN,JFK,LGA,LHR,ORD,SAN,SFO,SFO,SIN,TLV,BUD
19
DSM,ORD
ORD,BGI
BGI,LGA
SIN,CDG
CDG,SIN
CDG,BUD
DEL,DOH
DEL,CDG
TLV,DEL
EWR,HND
HND,ICN
HND,JFK
ICN,JFK
JFK,LGA
EYW,LHR
LHR,SFO
SFO,SAN
SFO,DSM
SAN,EYW
LGA
"""

sys.stdin = StringIO(input_string)


from collections import defaultdict, deque

def build_graph(routes):
    graph = defaultdict(list)
    for route in routes:
        src, dst = route.split(',')
        graph[src].append(dst)
    return graph

def bfs_reachable(graph, start, airports):
    visited = set()
    queue = deque([start])

    while queue:
        airport = queue.popleft()
        if airport in visited:
            continue
        visited.add(airport)
        for neighbor in graph[airport]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited

def find_minimum_connections(airports, routes, start_airport):
    graph = build_graph(routes)
    reachable_from_start = bfs_reachable(graph, start_airport, airports)
    
    # Find airports that are not reachable from the start
    missing_airports = set(airports) - reachable_from_start
    print(missing_airports) 
    if not missing_airports:
        return 0 

    additional_routes = 0
    while missing_airports:
        best_new_airport = None
        best_new_reach = 0
        best_new_reach_airports = set()

        # Check which missing airport connects to the most unreachable ones
        for airport in missing_airports:
            new_reach = bfs_reachable(graph, airport, airports) - reachable_from_start
            #print(new_reach)
            if len(new_reach) > best_new_reach:
                best_new_airport = airport
                best_new_reach = len(new_reach)
                best_new_reach_airports = new_reach

        # Add this best airport and its reach to the reachable set
        reachable_from_start.update(best_new_reach_airports)
        missing_airports -= best_new_reach_airports
        additional_routes += 1

    return additional_routes

test_cases = int(input())
for _ in range(test_cases):
    airports = input().split(',')
    num_routes = int(input())
    routes = [input() for _ in range(num_routes)]
    start_airport = input()

    result = find_minimum_connections(airports, routes, start_airport)
    print(result)

