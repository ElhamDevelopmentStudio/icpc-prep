def solve(a:str,b:str) -> int:
    len_a : int = len(a)
    len_b : int  = len(b)

    table : list[list[int]] = [[0] * (len_b + 1) for _ in range(len_a + 1)]  

    for _a in range(1,len_a+1):
        table[_a][0] = _a

    for _b in range(1,len_b+1):
        table[0][_b] = _b

    from pprint import pp
    pp(table)
    print()
    print("------------------------------------------------")
    print()
    for j in range(1,len_b+1):
        for i in range(1,len_a+1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            table[i][j] = min(
                table[i-1][j]+1, # deletion
                table[i][j-1]+1, # insertion
                table[i-1][j-1] + cost # substitution
            )

    pp(table)
    return table[len_a][len_b]

if __name__ == "__main__":
    a : str = "MOVIE"
    b : str = "LOVE"
    expected : int = 2
    res = solve(a,b)
    assert res == expected , f"Wrong answer expected {expected}, got {res}"
    print(res)