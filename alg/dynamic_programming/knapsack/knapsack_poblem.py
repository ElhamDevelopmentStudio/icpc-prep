# def knapsack(
#             n : int,
#             capacity : list[int],
#             weights : list[int],
#             prices : int
#             ) -> int:
#     if(n==0 or capacity==0):
#         return 0
 
#     if (weights[n-1]>capacity):
#         return knapsack(n-1,capacity,weights,prices)
   
#     else:
#         return max(
#                     prices[n-1] + knapsack(n-1,capacity-weights[n-1],weights,prices),
#                    knapsack(n-1,capacity,weights,prices)
#                    )

def knapsack(
            n : int,
            capacity : list[int],
            weights : list[int],
            prices : int
            ) -> int:
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n-1] > capacity:
        return knapsack(n-1,capacity,weights,prices)

    else:
        return max(
            prices[n-1] + knapsack(n-1,capacity-weights[n-1],weights,prices),
            knapsack(n-1,capacity,weights,prices)
        )



    

if __name__ == "__main__":
    weights : list[int] = [1,2,3,4]
    prices : list[int] = [50,200,150,100]
    n : int = 4
    capacity : int = 7
    res : int = knapsack(n,capacity,weights,prices)
    expected : int = 400
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)