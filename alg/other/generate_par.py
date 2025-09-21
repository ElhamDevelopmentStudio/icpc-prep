def main():
    res = []
    ans = []
    def solve(openn,close):
        if openn == close == n:
            res.append("".join(ans))
            return
        
        if openn <  n:
            ans.append("(")
            solve(openn+1,close)
            ans.pop()

        if close < openn:
            ans.append(")")
            solve(openn,close+1)
            ans.pop()
    
    solve(0,0)

    return res



if __name__ == "__main__":
    n = 3
    res = main()
    from pprint import pp
    pp(res)
    pp(len(res))
