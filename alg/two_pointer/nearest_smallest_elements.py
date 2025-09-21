"""
https://www.youtube.com/watch?v=sDKpIO2HGq0
this is for greater element but the implementation is still the same
"""
def min_solve(xs : list[int]) -> list[int]:
    res=[-1 for _ in xs]
    stack=[]
    for i,x in enumerate(xs):
        while len(stack)>0 and x<xs[stack[-1]]:
            res[stack.pop()]=x
        stack.append(i)
    return res

def max_solve(xs : list[int]) -> list[int]:
    res = [-1 for _ in xs]
    stack = []
    for index,value in enumerate(arr):
        while len(stack) > 0 and value > xs[stack[-1]]:
            res[stack.pop()] = value
        stack.append(index)
    return res

if __name__ == "__main__":
    arr = [1,3,4,2,5,3,4,2]
    min_res = min_solve(arr)
    max_res = max_solve(arr)
    print(min_res)
    print(max_res)
