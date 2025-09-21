"""
given a range n find in that all the numbers which equal to n and also their product is odd

so if n in 4
the range is 1,3
the only matching is 1 and 3 since 1+3 = 4 and 1*3 = 3 which is odd

return the len of sets u found

so if u found 2 sets of diffrent lens returns 2
if u found 2 sets of the same len then return 1


"""



def product(arr) -> int:
    res = 1
    for a in arr: res *= a
    return res

state = []
output = []
def solve(curr_sum,start,target):
    if curr_sum == target:
        w = set(state)
        if sum(w) == target and product(w) % 2 != 0:
            output.append(len(w))
        return

    for i in range(start,target):
        if curr_sum + i <= target:
            state.append(i)
            solve(curr_sum+i,i,target)
            state.pop()


for _ in range(int(input())):
    n = int(input())
    state = []
    output = []
    solve(0,1,n)
    print(len(set(output)))
