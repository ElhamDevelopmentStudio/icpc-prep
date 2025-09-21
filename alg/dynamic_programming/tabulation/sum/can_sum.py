"""
n -> m , coins.len
m -> target
time : O(n*m)
space : O(n)
"""
def solve(coins : list[int] , target : int) -> bool:
    table = [False] * (target + 1)
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for num in coins:
                try :table[i+num] = True
                except IndexError : continue
    return table[target]


if __name__ == "__main__":
    arr = [5,3,4]
    target = 7
    expected = True
    res = solve(arr,target)
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)