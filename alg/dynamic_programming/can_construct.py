
"""
def solve(words:list[str] , target:str) -> bool:
    if target == "" : return True

    for word in words:
        if len(word) <= len(target):
            is_true = True
            for i in range(len(word)):
                if word[i] != target[i]:
                    is_true = False
                    break
            if is_true : 
                if solve(words,target[len(word):]): return True
    return False
"""

"""
def solve(words:list[str] , target:str) -> bool:
    if target == "" : return True

    for word in words:
        try:
            if target.index(word) == 0:
                if solve(words,target[len(word):]) : return True
        except ValueError:
            continue
    return False

"""

def solve(words:list[str] , target:str,memo : dict[str,bool]) -> bool:
    if target in memo : return memo[target]
    if target == "" : return True

    for word in words:
        try:
            if target.index(word) == 0:
                if solve(words,
                         target[len(word):],
                         memo): memo[target] = True ; return True
        except ValueError:
            continue
    memo[target] = False
    return False


if __name__ == "__main__":
    # word = ["ab","abc","cd","de","abcd"]
    # target = "abcdef"
    # expected = True
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
    expected = False
    res = solve(word,target,{})
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)