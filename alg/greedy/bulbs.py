"""
given 'n' bulbs , either on (1) or off (0)
turning on ith bulb cause all reamining bulbs on  
the right to flip

find the min number of switches to turn all the bulbs on 

consts :
1 <=n <= 1e5
A[i] = {0,1}
"""


def solve(arr : list[int]) -> int:
    # o(n^2)
    # count = 0
    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         count += 1
    #         arr[i] = 1
    #         for j in range(i+1,len(arr)):
    #             arr[j] = not arr[j]
    #     else:
    #         continue
    # print(arr)
    # return count
    """
    0 1 1 1 0  
    0 0   
    """
    count = 0
    for bulb in arr:
        if count % 2 == 0: bulb = bulb
        else: bulb = not bulb


        if bulb % 2 == 1 : continue
        else : count += 1

    return count



if __name__ == "__main__":
    arr = [1,0,1]
    res = solve(arr)
    print(res)