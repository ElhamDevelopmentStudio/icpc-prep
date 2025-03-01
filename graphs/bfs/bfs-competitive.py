from collections import deque
from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = StringIO()

def bfs(graph, start):
    """
    Performs Breadth-First Search traversal on a graph.
    
    Args:
        graph (dict): A dictionary representing the graph as an adjacency list.
                     Keys are nodes and values are lists of neighboring nodes.
        start: The starting node for the BFS traversal.
    
    Returns:
        None: Prints the nodes in BFS order.
    
    Time Complexity: O(V + E) where V is number of vertices and E is number of edges
    Space Complexity: O(V) for the visited set and queue
    """
    # Set to keep track of visited nodes
    visited = set()
    # Queue for BFS - stores nodes to be processed in FIFO order
    queue = deque([start])
    # Mark the starting node as visited
    visited.add(start)
    
    # Process nodes until the queue is empty
    while queue:
        # Get the next node to process from the front of the queue
        vertex = queue.popleft()
        print(vertex, end=' ')  # Simulate processing (e.g., printing the node)
        
        # Explore all neighbors of the current node
        for neighbor in graph[vertex]:
            # Only process unvisited neighbors to avoid cycles
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],    # Node A is connected to B and C
    'B': ['A', 'D', 'E'],  # Node B is connected to A, D, and E
    'C': ['A', 'F'],    # Node C is connected to A and F
    'D': ['B'],         # Node D is connected to B
    'E': ['B', 'F'],    # Node E is connected to B and F
    'F': ['C', 'E']     # Node F is connected to C and E
}

# Run BFS
bfs(graph, 'A')

# Capture and restore output
output = sys.stdout.getvalue().strip()
sys.stdout = old_stdout

print("BFS Output:", output)