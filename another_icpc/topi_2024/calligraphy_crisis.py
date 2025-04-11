import sys
from io import StringIO


input_string = """5
rat
art
tarp
part
trap
3
tra
ar
tp
"""

sys.stdin = StringIO(input_string)


num_of_pieces = int(input())

pieces = [input() for _ in range(num_of_pieces)]


def solve(target,words):
    target_set = set(target)
    len_target_set = len(target_set)

    result = 0
    for word in words:
        completed = 0
        is_anagram = True
        for w in word: 
            if completed  == len_target_set:
                is_anagram = True
                break
            else:
                if w in target_set:
                    completed += 1
                    continue
                else:
                    is_anagram = False
                    break
        if is_anagram:
            result += 1

        is_anagram = True
        completed = 0
    
    return result if result != 0 else -1


for _ in range(int(input())):
    word = input()
    result = solve(
        word,pieces
    )
    print(result)
