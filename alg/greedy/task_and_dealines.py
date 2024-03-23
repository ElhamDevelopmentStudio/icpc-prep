"""
from page 60 of comp prog
"""

tasks = [
    (4,2), # duration - deadline
    (3,5),
    (2,7),
    (4,5)
]

tasks.sort(key= lambda x :x[0])
print(tasks)
prof = 0
end_time = 0
for duration,dealine in tasks:
    end_time += duration
    print(f"got {dealine - end_time} points")
    prof += (dealine - end_time)

print(prof)

