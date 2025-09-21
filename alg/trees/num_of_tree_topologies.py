def count_trees(n,memo):
    if n in memo : return memo[n]
    if n < 2:
        return 1
    memo[n] =  sum([count_trees(i,memo) * count_trees(n - i - 1,memo) for i in range(n)])
    return memo[n]

n = int(input("Enter a non-negative integer: "))
print("Number of possible binary tree topologies:", count_trees(n,{}))
import uuid
print(uuid.uuid4())