"""
can construct problem but we return the detail of the number of ways it is possible
"""
# def solve(words:list[int],target:str) -> list[list[str]]:
#     if target == "" : return [[]]
#     ways = []
#     for word in words:
#         try:
#             if target.index(word) == 0:
#                 res = solve(words,target[len(word):])
#                 if res != None: 
#                     for my_res in res:
#                         my_res.append(word)
#                     ways.extend(res)
#         except ValueError:
#             continue
#     return None if len(ways) == 0 else ways

"""
def solve(words:list[int],target:str) -> list[list[str]]:
    if target == "" : return [[]]
    result = []
    for word in words:
        try:
            if target.index(word) == 0:
                suffix_res = solve(words,target[len(word):])
                added_suffix_res = map(lambda ways : [word] + ways ,suffix_res)
                result.extend(added_suffix_res)
        except ValueError:
            continue
    return result
"""

#time : O(n^m)
#space : O(m)
def solve(words:list[int],target:str,memo) -> list[list[str]]:
    if target in memo : return memo[target]
    if target == "" : return [[]]
    result = []
    for word in words:
        if target.find(word) == 0:
            suffix_res = solve(words,target[len(word):],memo)
            added_suffix_res = map(lambda ways : [word] + ways ,suffix_res)
            result.extend(added_suffix_res)
    memo[target] = result
    return result

if __name__ == "__main__":
    # word = ["ab","abc","cd","def","abcd","ef"]
    # target = "abcdef"
    # expected = [['ab', 'cd', 'ef'], ['abc', 'def'], ['abcd', 'ef']]
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
    expected = []
    res = solve(word,target,{})
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)