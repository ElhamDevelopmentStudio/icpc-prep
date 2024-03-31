def solve(_row,_column):
    table = [[0] * (_column+1) for _ in range(_row + 1)]
    table[1][1] = 1

    for row in range(_row+1):
        for column in range(_column+1):
            if column +1  <= _column : table[row][column+1] += table[row][column]
            if row+1 <= _row : table[row+1][column] += table[row][column]
            
    return table[row][column]





if __name__ == "__main__":
    row,column = 3,3
    expcted = 6
    # row,column = 18,18
    # expcted = 2333606220
    res = solve(row,column)
    assert res == expcted , f"Wrong anwer your answer was {res} expected {expcted}"
    print(res)