def do_asses(l, r, original_arr, delta):
    current_max = float('-inf')
    global_max = float('-inf')
    
    # Iterate through the specified range
    for i in range(l-1, r):
        # Calculate adjusted value with accumulated delta
        val = original_arr[i] + delta
        # Kadane's algorithm
        current_max = max(val, current_max + val)
        global_max = max(global_max, current_max)
    
    # Return maximum of 0 and the found maximum (per problem requirements)
    return max(global_max, 0)

# Read input
n, q = map(int, input().split())
original_A = list(map(int, input().split()))
delta = 0  # Tracks cumulative additions

for _ in range(q):
    event = input().split()
    
    if event[0] == 'A':
        # Query: find maximum subarray sum in range [l, r]
        l = int(event[1])
        r = int(event[2])
        print(do_asses(l, r, original_A, delta))
    else:
        # Update: add value to all elements (track via delta)
        delta += int(event[1])
