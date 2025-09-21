# def solve(target : int) -> int:
#     arr = [0] * (target + 1)
#     arr[1] = 1

#     for i in range(2,target+1):
#         arr[i] = arr[i-2] + arr[i-1]

#     return arr[target]

def solve(target : int) -> int:
    arr = [0] * (target + 1)
    arr[1] = 1

    for i in range(0,target+1):
        try: arr[i+1] += arr[i] ; arr[i+2] += arr[i]
        except IndexError : pass 
    return arr[target]

if __name__ == "__main__":
    fib = 7
    res = solve(fib)
    expected = 13
    assert res == expected , f"Wrong answer , the answer should have been {expected} while yours was {res}"
    print(res)