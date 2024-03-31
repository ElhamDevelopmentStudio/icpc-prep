"""
can construct problem but we return the number of ways it is possible
"""


"""
basic impl
def solve(words:list[int],target:int) -> int:
    if target == "" : return True
    ways = 0
    for word in words:
        try:
            if target.index(word) == 0:
                ways += solve(words,target[len(word):])
        except ValueError:
            continue
    
    return ways
"""


# memoized 
def solve(words:list[int],target:int,memo) -> int:
    if target in memo : return memo[target]
    if target == "" : return True
    ways = 0
    for word in words:
        try:
            if target.index(word) == 0:
                ways += solve(words,target[len(word):],memo)
        except ValueError:
            continue
    
    memo[target] = ways
    return ways


if __name__ == "__main__":
    # word = ["ab","abc","cd","def","abcd","ef"]
    # target = "abcdef"
    # expected = 0
    """
    0 : ab , 2 : cd , 5 : ef
    1 : abc , 3 : def
    4 : abcd , 5 : ef
    so 3 ways to make this 
    """
    word = [
        "e",
        "ee",
        "eee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeee",
    ]
    target = "eeeeeeeeeeeeeeeeeeeeeeeeeeef"
    expected = 0
    res = solve(word,target,{})
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)