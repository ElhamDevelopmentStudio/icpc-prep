import heapq
min_this = [1,2,3,4,5]
max_this = [3,4,5,6,7,8]

# for min heap
heapq.heapify(min_this)
# for max heap
heapq._heapify_max(max_this)


first_smallest_number = heapq.heappop(min_this)
first_largest_number = heapq.nlargest(1,max_this)

print(first_smallest_number)
print(first_largest_number)
