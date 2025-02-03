def process_customers(counters, customers):
    total_time = 0
    #create [0,0] meaning customers will be free
    next_available_time = [0] * counters

    for customer in customers:
        arrival_time, processing_time = customer

        # Find the counter with the earliest available time
        min_time = min(next_available_time)

        if arrival_time > min_time:
            # If the customer arrives after the earliest available time,
            # update the counter's available time to the customer's arrival time
            min_time = arrival_time

        # Add the processing time to the counter's available time
        counter_index = next_available_time.index(min_time)

        next_available_time[counter_index] = min_time + processing_time




        # Update the total time if the current customer's completion time is greater
        if next_available_time[counter_index] > total_time:
            total_time = next_available_time[counter_index]
  

    return total_time

# Get the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    counters, num_customers = map(int, input().split())
    customers = []

    # Get the arrival time and processing time for each customer
    for _ in range(num_customers):
        arrival_time, processing_time = map(int, input().split())
        customers.append((arrival_time, processing_time))

    # Calculate the total time to process all customers
    total_time = process_customers(counters, customers)
    print(total_time)