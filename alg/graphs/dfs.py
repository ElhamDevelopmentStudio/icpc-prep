visisted = set()
# assuming we are using adj list for showing the graph
arr = []
def dfs(node):
    if node in visisted : return
    visisted.add(node)
    for neigh in arr[node]:
        dfs(neigh)
    


