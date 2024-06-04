def is_pal(word,i,j):
    while i < j:
        if word[i] != word[j]:
            return False
        i +=1
        j-=1
    return True

def min_pal_par(word,i,j):
    
    if i >=j or is_pal(word,i,j):
        return 0

    ans = float("inf")

    for k in range(i,j):
        count = min_pal_par(word,i,k) + min_pal_par(word,k+1,j)+1
        ans = min(ans,count)

    return ans


if __name__ == "__main__":
    word = "noonabbad"
    res = min_pal_par(word,0,len(word)-1)
    print(res)
