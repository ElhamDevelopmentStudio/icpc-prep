"""
my first naive implementation without any memoization
def solve(row,column):
    x,y = 0,0
    res = [0]
    def dfs(x,y):
        if x == column - 1 and y == row - 1:
            res[0] += 1
            return 
        if x + 1 <= column:
            dfs(x+1,y)
        if y+1 <= row:
            dfs(x,y+1)
    dfs(x,y)
    return res[0]
"""
"""
video impl of the problem
time : O(2^row+column)
space : O(row+column)
def solve(row,column):
    if row == 1 and column == 1 : return 1
    if row == 0 or column == 0 : return 0

    return solve(row-1,column) + solve(row,column-1)
"""

"""
memoized impl of the last impl
time  : O(row*column)
space : O(row+column)
"""
def solve(row,column,memo):
    this = f"{row},{column}"
    if this in memo : return memo[this]

    if row == 1 and column == 1 : return 1
    if row == 0 or column == 0 : return 0

    memo[this] = solve(row-1,column,memo) + solve(row,column-1,memo)
    return memo[this]



if __name__ == "__main__":
    # row,column = 2,3
    # expcted = 3
    row,column = 18,18
    expcted = 2333606220
    res = solve(row,column,{})
    assert res == expcted , f"Wrong anwer your answer was {res} expected {expcted}"
    print(res)