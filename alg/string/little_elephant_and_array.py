from collections import defaultdict
def count(arr,q):
    result = 0
    hashmap = defaultdict(int)
    l,r = q
    for i in range(l,r+1):
       hashmap[arr[i]]+=1
    for key,value in hashmap.items():
        if int(key) == value : result+=1
    return result

def solve(arr,qs):
    result = []
    for q in qs:
        result.append(str(count(arr,q)))
    return "\n".join(result)


if __name__ == "__main__":
    len_of_arr , num_of_q = list(map(int,input().split()))
    arr = input().split()
    q_s = []
    for i in range(num_of_q):
        l,r = list(map(int,input().split()))
        q_s.append([l-1,r-1])
    res = solve(arr,q_s)
    print(res)

