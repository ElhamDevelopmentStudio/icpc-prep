"""
from page 255 page of comp prog handbook

given a string 's' and also strings of 'D' ,
find how many times can string 's' be formed using
strings from 'D'

for ex:
    s = ABAB
    D = {A,B,AB}
    ans : 4
"""
def count(s : str,D : list[str]) -> int:
    n = len(s)
    m = len(D)
    table = [0] * (n+1)

    for i in range(n):
        this_res = 0
        for j in range(m):
            if s[i] == D[j]: this_res+=1

        table[i] = this_res
    
    return sum(table)


if __name__ == "__main__":
    s = "ABAB"
    D = ["A","B","AB"]
    res = count(s,D)
    print(res)
