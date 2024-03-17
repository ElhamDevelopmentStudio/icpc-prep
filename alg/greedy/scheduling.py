import itertools

events = [
  (1, 3), # event 1 starts at time 1, ends at time 4
  (2, 5), 
  (3, 9),
  (6, 9),
]


# Sort events by ending time
events.sort(key=lambda x: x[1]) 
print(events)
schedule = []
current_time = 0

for start, end in events:
  if start >= current_time:
    schedule.append((start, end))
    current_time = end

print(schedule)







