num_tests = int(input()) 
for _ in range(num_tests):
  n = int(input())
  laptops_used = 0
  intervals = []
  for _ in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))
  
  intervals.sort(key=lambda x : x[1])

  print(intervals)
  current_time = 0

  for start, end in intervals:
    if start > current_time:  
      current_time = end
    else:
      laptops_used += 1
      
  print(laptops_used)