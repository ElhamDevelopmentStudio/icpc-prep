import sys
from io import StringIO

input_string = """5
EMAIL 3 5 6 7 8 9 10
CRASH 2 7 1 8 2 8 1
MOUSE 4 0 9 3 9 1 7
SWERC 6 3 1 4 1 5 9
PAINT 6 0 0 0 0 0 10
"""


sys.stdin = StringIO(input_string)


num_teams = int(input())

result = []

def calculate_trampolin_score(scores):
    max_value = float("-inf")
    min_value = float("inf")
    value = 0
    for i in range(len(scores)):
        value += scores[i]
        if max_value < scores[i]:
            max_value = scores[i]

        if min_value > scores[i]:
            min_value = scores[i]

    return value - max_value - min_value


def solve(value):
    team,programming_score,trampolin_score = value[0],int(value[1]),list(map(int,value[2:]))
    print(trampolin_score)
    tramp_score = calculate_trampolin_score(trampolin_score)
    print(tramp_score)
    print(programming_score)
    score =  tramp_score + (10*programming_score)

    return team,score



for _ in range(num_teams):
    result.append(
        solve(input().split())
    )


final_result = sorted(result,key=lambda x : x[1])
print(*final_result)

