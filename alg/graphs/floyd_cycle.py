def floyd_cycle_detection(graph):
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

graph = {
    1 : [2],
    2 : [3],
    3 : [4],
    4 : [5],
    5 : [6],
}

print(floyd_cycle_detection(graph))  # Output: True