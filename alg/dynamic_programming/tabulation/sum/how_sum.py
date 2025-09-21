"""
n -> m , coins.len
m -> target
time : O(m^2 *n)
space : O(m ^ 2)
"""
def solve(coins : list[int] , target : int) -> bool:
    table = [None] * (target + 1)
    table[0] = []
    for i in range(len(table)):
        if table[i] != None:
            for num in coins:
                try :
                    # if there is nothin in the table create it else add to it
                    table[i+num] = [num] if table[i+num] == None else table[i+num] + [num]
                except IndexError :
                    continue
    return table[target]


if __name__ == "__main__":
    arr = [5,3,4]
    target = 7
    expected = [4,3]
    res = solve(arr,target)
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)