# A simple implementation of Priority Queue
# using Queue.
import heapq

class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			max_val = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max_val]:
					max_val = i
			item = self.queue[max_val]
			del self.queue[max_val]
			return item
		except IndexError:
			print()
			exit()


def heap_impl(arr):
	print(f"first arr is {arr}")
	another_arr = [2,34,5,6,7]
	#heapq.heapify(arr) # for min heap
	heapq._heapify_max(arr) # for max heap
	print(f"second arr is {arr}")
	heapq.heappush(arr,100)
	heapq._heappop_max(arr)
	# heapq._heappushpop_max(arr,100)
	print(f"third arr is {arr}")
	#heapq.heappop(arr)
	print(f"fourth arr is {arr}")
    #max_heap_first_elem = heapq.nlargest(1,max_heap_queue)
	#min_heap_first_elem = heapq.nsmallest(1,min_heap_queue)

if __name__ == '__main__':
	#impl = "Queue(O(n))" # or Heap(O(1))
	impl = "Heap(O(1))"
	if impl == "Queue(O(n))":	
		myQueue = PriorityQueue()
		myQueue.insert(12)
		myQueue.insert(1)
		myQueue.insert(14)
		myQueue.insert(7)
        # print(myQueue)		 
		while not myQueue.isEmpty():
			print(myQueue.delete())
	elif impl == "Heap(O(1))":
		arr = [2,6,5,8,1,2,3]
		heap_impl(arr)