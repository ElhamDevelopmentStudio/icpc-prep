"""

the only way the the input is gonna return 'impossible' 
is when graph has a cycle . one way of doing it is to check if the graph has cycle
if so return impossible otherwise it will always return some answer

"""

def has_cycle(graph):
    slow = 1
    fast = 1

    try:
        slow = graph[slow][0]
    except (KeyError, IndexError):
        return False  # No cycle detected

    try:
        fast = graph[fast][0]
        fast = graph[fast][0]
    except (KeyError, IndexError):
        return False  # No cycle detected

    while fast != slow:
        try:
            slow = graph[slow][0]
        except (KeyError, IndexError):
            return False  # No cycle detected

        try:
            fast = graph[fast][0]
            fast = graph[fast][0]
        except (KeyError, IndexError):
            return False  # No cycle detected

        if slow == fast:
            return True  # Cycle detected

    return False  # No cycle detected


def solve(graph):
    if has_cycle(graph) : return "impossible"
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neigh in graph.get(node,[]):
            if neigh not in visited:
                dfs(neigh)
        result.append(node)        
    
    
    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]
        

if __name__ == "__main__":
    for _ in range(int(input())):
        graph = {}
        num_of_jobs = int(input())
        for __ in range(num_of_jobs):
            job , dep = list(map(int,input().split()))

            if job in graph:
                graph[job].append(dep)
            else:
                graph[job] = [dep]

        all_jobs = list(map(int,input().split()))

        print(solve(graph))