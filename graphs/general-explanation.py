# We'll use a dictionary called 'graph' to store our adjacency list.
# Keys   -> node labels (like 'A', 'B', or integers)
# Values -> list of neighboring nodes (those directly connected by an edge)

graph = {}  # Global dictionary for storing our undirected graph

def add_edge(u, v):
    """
    Connects node u to node v, and node v to node u (undirected edge).
    """
    # If u is not in the dictionary yet, initialize it with an empty list
    if u not in graph:
        graph[u] = []
    # If v is not in the dictionary yet, initialize it with an empty list
    if v not in graph:
        graph[v] = []
    
    # Add each node to the other's adjacency list
    graph[u].append(v)
    graph[v].append(u)

def print_graph():
    """
    Prints each node and the list of its neighbors.
    """
    for node in graph:
        print(f"{node} -> {graph[node]}")

# Let's test this with a tiny example:
if __name__ == "__main__":
    # Add a few edges
    add_edge('A', 'B')
    add_edge('B', 'C')
    add_edge('A', 'C')
    add_edge('C', 'D')

    # Show how the graph looks
    print_graph()
