from collections import deque
from io import StringIO
import sys

def dfs_iterative(graph, start):
    """
    Performs a non-recursive Depth-First Search traversal on a graph.
    
    Args:
        graph (dict): A dictionary representing the graph as an adjacency list.
                     Keys are nodes and values are lists of neighboring nodes.
        start: The starting node for the DFS traversal.
    
    Returns:
        None: Prints the nodes in DFS order.
    
    Time Complexity: O(V + E) where V is number of vertices and E is number of edges
    Space Complexity: O(V) for the visited set and stack
    """
    visited = set()
    stack = [start]  # Use a list as a stack
    
    while stack:
        vertex = stack.pop()  # Pop from the end (LIFO)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            # Add neighbors in reverse order to match recursion
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

if __name__ == "__main__":
    # Example graph as an adjacency list
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
    
    # Run DFS
    dfs_iterative(graph, 'A')
    
    # Capture and restore output
    output = sys.stdout.getvalue().strip()
    sys.stdout = sys.__stdout__
    
    # One valid DFS traversal (note: multiple valid traversals are possible)
    expected = "A B D E F C"
    
    assert output == expected, f"Expected {expected}, but got {output}"
    print("DFS Output:", output)
    print("All tests passed!")