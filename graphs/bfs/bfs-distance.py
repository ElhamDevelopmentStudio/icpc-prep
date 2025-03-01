from collections import deque
from io import StringIO
import sys

def bfs_with_distance(graph, start):
    """
    Performs a breadth-first search starting from a given node and calculates
    the shortest distance to all reachable nodes.
    
    Args:
        graph (dict): Adjacency list representation of the graph where
                     keys are nodes and values are lists of neighbors
        start: Starting node for the BFS traversal
    
    Returns:
        dict: Dictionary mapping each reachable node to its shortest distance from start
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    # Dictionary to store distance from start
    distance = {start: 0}
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[vertex] + 1
    
    return distance

# Test case
if __name__ == "__main__":
    # Create a test graph using the example from bfs-competitive.py
    graph = {
        'A': ['B', 'C'],    # Node A is connected to B and C
        'B': ['A', 'D', 'E'],  # Node B is connected to A, D, and E
        'C': ['A', 'F'],    # Node C is connected to A and F
        'D': ['B'],         # Node D is connected to B
        'E': ['B', 'F'],    # Node E is connected to B and F
        'F': ['C', 'E']     # Node F is connected to C and E
    }
    
    # Redirect stdout to capture print output
    stdout = StringIO()
    sys.stdout = stdout
    
    # Calculate and print distances
    distances = bfs_with_distance(graph, 'A')
    print("Distances from A:", distances)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Verify the output
    output = stdout.getvalue()
    expected = "Distances from A: {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}\n"
    
    print(output)
    assert output == expected, f"Expected {expected}, but got {output}"
    print("All tests passed!")