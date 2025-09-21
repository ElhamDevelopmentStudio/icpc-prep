
"""
_____________________
    
ab  |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
    |   |   |   |   |
_____________________

"""

from pprint import pp
def solve(words:list[str] , target : str) -> bool:
    table = [False] * (len(target) + 1)
    table[0] = True

    


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
    res = solve(word,target)
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)