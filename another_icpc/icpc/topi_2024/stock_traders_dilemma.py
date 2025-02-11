import sys
from io import StringIO


input_string = """3
2
6
10 22 5 75 65 80
3
6
10 22 5 75 65 80
1
5
90 80 70 60 50
"""


"""
10 22 5 75
"""


sys.stdin = StringIO(input_string)

def solve(k,num_of_days,days):
    memo = {}
    def backtrack(
            index : int,
            done : int,
    ) -> int:
        #print(f"here with days {days[index:]} and profit of {max_profit}")
        if done == k or index >= num_of_days:
            return 0 
        best_solution = backtrack(index+1,done) 

        for i in range(index+1,num_of_days):
            local_profit = days[i] - days[index]
            if local_profit > 0:
                backtrack_result = backtrack(
                    i+1,
                    done+1,
                )
                this_profit = local_profit + backtrack_result
                best_solution = max(best_solution,this_profit)

        memo[(index,done)] = best_solution
        return best_solution #type:ignore


    return backtrack(0,0)

for _ in range(int(input())):
    k = int(input())
    num_of_days = int(input())
    days = list(
        map(int,input().split())
    )

    result = solve(k,num_of_days,days)
    print(result)
