from collections import deque

this_arr = [2,3,4,5,6,1,8]
my_deq = deque(this_arr)

another_arr = [3,4,5,6,7,8]

my_deq.extend(another_arr)

print(my_deq)
for i in range(len(my_deq)):
    print(my_deq[i])