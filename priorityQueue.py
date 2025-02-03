import heapq

dataList = [6,3,72,67,1,35,12,4,7,8]
print(dataList, "\n")
# print(sorted(dataList))

heapq.heapify(dataList)
print(dataList)

print(heapq.heappop(dataList))
print(dataList)

# heapq._heapify_max(dataList)
# print("\n\n", dataList)

# heapq._heappop_max(dataList)
# print("\n\n", dataList)

# data = [6,3,72,67,1,35,12,4,7,8]
# data2 = [2,4,6,23,52,53,24,7,8,42,35]

# print(list(heapq.merge(data,data2)))
