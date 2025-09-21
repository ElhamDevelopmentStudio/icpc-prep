"""
Explanation From https://youtu.be/Ph95IHmRp5M?si=dngtnrg0QrcvNUvW
we just keep the record of cols and pos diags and neg diags
and then we put them until we can
"""

if __name__ == "__main__":
    n  = 4
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for i in range(n)] 
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."
    
    backtrack(0)
    print(len(res))