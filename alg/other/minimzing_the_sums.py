arr = [1,2,9,2,6]
"""
for minimzing the sums we take the median
for maximizing the sums we take the average
"""

# minimzing
res_min = 0
sorted_minimize =sorted(arr)
x_minimize = sorted_minimize[len(sorted_minimize) // 2]
for i in sorted_minimize:
    # for some reason the abs value is necessary
    res_min += abs((i - x_minimize))

print(res_min)

# maximizing
res_max = 0
average = sum(arr) // len(arr)
print(average)
for i in arr:
    res_max += 2**abs((i-average))

print(res_max)
