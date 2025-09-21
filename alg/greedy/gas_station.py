"""
gas = [3,5,2,1,7]
cost = [4,2,1,9,1]


 -> 0 | 1 | 2 | 3 | 4
g   3 | 5 | 2 | 1 | 7
c   4 | 2 | 1 | 9 | 1
r   5 | 8 | 9 | 1 | 6



"""

def solve(gas : list[int], cost : list[int]) -> int:
    d = {i:[i,gas[i],cost[i],gas[i]-cost[i]] for i,x in enumerate(gas)}
    sorted_d = dict(sorted(d.values(), key=lambda x: -x[3]))
    print(sorted_d)
    print(d)
    max_num = sorted_d[0][3]
    find_i = d.index()
    print(max_num)



if __name__ == "__main__":

    gas = [3,5,2,1,7]
    cost = [4,2,1,9,1]
    res = solve(gas,cost)
    print(res)