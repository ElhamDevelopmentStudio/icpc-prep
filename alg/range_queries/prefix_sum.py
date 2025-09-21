def solve(arr : list[int]) -> list[int]:
    result = []
    sum = arr[0]
    result.append(arr[0])
    for value in arr[1:]:
        sum += value
        result.append(sum)
    
    return result

def find_sum(a : int,b : int,prefix_arr : list[int]) -> int:
    return prefix_arr[b] - prefix_arr[a]


if __name__ == "__main__":
    those = tuple([0])
    that = tuple([10,20])
    whose = those.__add__(that)

    print(whose)
    arr : list[int] = [1,3,4,8,6,1,4,2]
    prefix_arr : list[int] = solve(arr)

    # range for 3,6
    this = find_sum(3,6,prefix_arr)
    print(this)
    
