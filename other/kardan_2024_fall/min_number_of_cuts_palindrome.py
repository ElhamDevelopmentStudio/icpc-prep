def is_pal(word,i,j):
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

"""
def solve(i,j,word):
    if i >= j or is_pal(word,i,j):
        return 0

    ans = float("inf")
    for k in range(i,j):
        count = solve(i,k,word) + solve(k+1,j,word) + 1
        ans = min(ans,count)

    return ans
"""

def is_pal(word, i, j):
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

def solve(i, j, word, dp, partitions):
    if i >= j or is_pal(word, i, j):
        partitions[i][j] = [word[i:j+1]]
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    ans = float("inf")
    best_partition = []

    for k in range(i, j):
        left = solve(i, k, word, dp, partitions)
        right = solve(k + 1, j, word, dp, partitions)
        count = left + right + 1

        if count < ans:
            ans = count
            best_partition = partitions[i][k] + partitions[k+1][j]

    dp[i][j] = ans
    partitions[i][j] = best_partition

    return ans

def min_palindrome_cuts(word):
    n = len(word)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    partitions = [[[] for _ in range(n)] for _ in range(n)]
    solve(0, n - 1, word, dp, partitions)

    result = " | ".join(partitions[0][n-1])
    print(f"Minimum cuts needed for Palindrome Partitioning is {dp[0][n-1]}")
    print(f"Palindromic Partition: {result}")



word = "ababbbabbababa"
res = min_palindrome_cuts(word)

print(res)


