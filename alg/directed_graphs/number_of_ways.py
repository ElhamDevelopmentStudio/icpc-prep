# def solve(graph,start,end):
#     stack = [start]
#     count = 0
#     while stack:
#         curr_node = stack.pop(-1)
#         if curr_node == end:
#             count += 1
#             continue
#         for neigh in graph[curr_node]:
#             stack.append(neigh)
#     return count


def solve(graph,start,end):
    stack = [start]
    paths = [0] * (end + 1)
    while stack:
        curr_node = stack.pop(-1)
        paths[curr_node] += 1
        if curr_node == end:
            continue
        for neigh in graph[curr_node]:
            stack.append(neigh)
    print(paths)
    return paths[end]

graph = {
    1 : [2,4],
    2 : [3],
    3 : [6],
    4 : [5],
    5 : [2,3]
}

res = solve(graph,1,6)
print(res)

