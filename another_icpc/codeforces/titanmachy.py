def get_consecutive_subsets(arr):
    n = len(arr)
    subsets = []
    
    for start in range(n):
        for end in range(start + 1, n + 1):
            subsets.append(arr[start:end])
    
    return subsets

ptr = 0

n,q = list(map(int,input().split()))
#print(n,q)
ptr+=1 

A = tuple(map(int,input().split()))
ptr+=1
#print(A)


def do_asses(l,r):
    #print(A)
    res = float("-inf")
    #print(A[l-1:r])
    #a = get_subsets(A[l-1:r])
    #pp(a)
    for subset in get_consecutive_subsets(A[l-1:r]):
        res = max(res,sum(subset))
    return max(res,0)

for _ in range(q):
    event = input()
    ptr+=1
    if event[0] == "A":
        splitted = event.split()
        l,r = int(splitted[1]),int(splitted[2])
        print(do_asses(l,r))
    else:
        number = int(event.split()[1])
        A = tuple(map(lambda x : x + number,A)) 


