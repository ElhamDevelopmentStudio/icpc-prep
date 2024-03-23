import heapq
def solve(arr : list[int]) -> int:
    sum = 0
    heapq.heapify(arr)
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        sum += (first+second)
        heapq.heappush(arr,(first+second))

    return sum

arr = [1,4,7,10]
output = solve(arr)
print(output)
assert output == 39