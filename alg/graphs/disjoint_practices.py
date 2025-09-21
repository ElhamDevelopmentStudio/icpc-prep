"""
Edje-disjoint paths -> each edge can only occur one = max flow where each edge capacity is 1
Node-disjoint paths -> solve below
"""




from max_flow import Graph





"""
    1   <-  3
0   =       =   6
    3   ->  5

"""

graph = [
#    0 1 2 3 4 5
    [0,1,0,1,0,0], # 0
    [0,1,0,1,0,0], # 1
    [0,1,1,0,1,1], # 2
    [0,0,1,1,1,0], # 3
    [0,0,0,0,1,1], # 4
    [0,0,0,0,0,0], # 5
]

g = Graph(graph)
print(g.FordFulkerson(0,5))