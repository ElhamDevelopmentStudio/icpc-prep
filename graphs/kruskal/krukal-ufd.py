from io import StringIO
import sys

class UnionFind:
    """
    Union-Find data structure implementation with path compression and union by rank.
    Used for efficiently tracking connected components in a graph.
    
    Time Complexity:
        - Find: O(α(n)) amortized, where α is the inverse Ackermann function
        - Union: O(α(n)) amortized
    Space Complexity: O(n) where n is the number of elements
    """
    def __init__(self, size):
        """Initialize Union-Find data structure with given size."""
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, u):
        """Find the root/representative of the set containing element u."""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        """
        Union the sets containing elements u and v.
        Returns True if u and v were in different sets, False otherwise.
        """
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        if self.rank[pu] == self.rank[pv]:
            self.rank[pu] += 1
        return True

def kruskal(graph, num_vertices):
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    Args:
        graph (dict): Dictionary of dictionaries representing the weighted graph.
                     Format: {u: {v: weight}} for each edge (u,v) with weight.
        num_vertices (int): Number of vertices in the graph.
    
    Returns:
        tuple: (list of MST edges as (u,v,weight), total weight of MST)
    
    Time Complexity: O(E log E) where E is the number of edges
    Space Complexity: O(V + E) where V is the number of vertices
    """
    # Store edges as (weight, u, v)
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            if u < v:  # Avoid duplicates (undirected graph)
                edges.append((weight, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize Union-Find and MST
    uf = UnionFind(num_vertices)
    mst = []
    total_weight = 0
    
    # Process each edge
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

if __name__ == "__main__":
    # Redirect stdout to capture print output
    stdout = StringIO()
    sys.stdout = stdout
    
    # Test graph as an adjacency list with weights
    graph = {
        0: {1: 4, 2: 8},
        1: {0: 4, 2: 11, 3: 8},
        2: {0: 8, 1: 11, 3: 2, 4: 7},
        3: {1: 8, 2: 2, 4: 6},
        4: {2: 7, 3: 6}
    }

    # Run Kruskal's algorithm (5 vertices: 0 to 4)
    mst, total_weight = kruskal(graph, 5)
    print("MST Edges:", mst)
    print("Total Weight:", total_weight)
    
    # Capture and restore output
    output = sys.stdout.getvalue().strip()
    sys.stdout = sys.__stdout__
    
    # Verify MST properties
    # 1. Number of edges should be n-1 (where n is number of vertices)
    assert len(mst) == 4, f"MST should have 4 edges, but got {len(mst)}"
    
    # 2. Total weight should be 19 (minimum possible for this graph)
    assert total_weight == 19, f"MST weight should be 19, but got {total_weight}"
    
    # 3. All edges should be valid and in the original graph
    for u, v, w in mst:
        assert v in graph[u] and graph[u][v] == w, f"Invalid edge: {u}-{v} with weight {w}"
    
    print("Test output:", output)
    print("All tests passed!")