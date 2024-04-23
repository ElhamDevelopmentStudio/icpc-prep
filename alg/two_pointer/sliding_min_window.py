from collections import deque

# max sliding window implementation
def max_solve(arr : list[int], size:int) -> list[int]:
    queue = deque()
    left = 0
    right = 0
    output = []
    length_of_arr = len(arr)
    while right < length_of_arr:
        while queue and arr[right] > arr[queue[-1]]:
            queue.pop()

        queue.append(right)

        if left > queue[0]:
            queue.popleft()

        if right + 1 >= size:
            output.append(arr[queue[0]])
            left += 1
        right += 1
    
    return output
        


if __name__ == "__main__":
    # max sliding window
    max_arr = [1,3,-1,-3,5,3,6,7]
    max_size = 3
    max_res  = max_solve(max_arr,max_size)
    max_expected = [3,3,5,5,6,7]
    assert max_res == max_expected , f"wrong answer got {max_res} expected {max_expected}"
    print(max_res)