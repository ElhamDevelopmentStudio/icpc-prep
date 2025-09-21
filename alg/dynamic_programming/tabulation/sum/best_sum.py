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
                    combs = table[i] + [num]
                    if table[i+num] == None or len(table[i+num]) > len(combs):
                        table[i+num] =  combs
                except IndexError :
                    continue
    return table[target]


if __name__ == "__main__":
    arr = [2,3,5]
    target = 8
    expected = [3,5]
    res = solve(arr,target)
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)