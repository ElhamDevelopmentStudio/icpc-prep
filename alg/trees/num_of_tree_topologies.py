def count_trees(n):
    if n < 2:
        return 1
    return sum([count_trees(i) * count_trees(n - i - 1) for i in range(n)])

n = int(input("Enter a non-negative integer: "))
print("Number of possible binary tree topologies:", count_trees(n))