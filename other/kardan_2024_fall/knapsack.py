def knapsack(len_of_arr,max_weight,weights,values):
    if len_of_arr == 0 or max_weight == 0:
        return 0
    

    if weights[len_of_arr-1] > max_weight:
        return knapsack(len_of_arr-1,max_weight,weights,values)

    else:
        # we either take the item or not take the item
        include = values[len_of_arr-1] + knapsack(len_of_arr-1,max_weight - weights[len_of_arr-1],weights,values)
        exclude  = knapsack(len_of_arr-1,max_weight,weights,values)

        return max(include,exclude)




weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_weight = 5
len_of_arr = len(weights)
print(knapsack(len_of_arr, max_weight, weights, values))  
