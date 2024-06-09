from math import ceil, log2

class SegmentTree:
    def __init__(self, input_):
        self.n = 2 ** ceil(log2(len(input_)))
        print(self.n)
        self.tree = [0] * (2 * self.n)
        print(len(self.tree))
        self.build(input_)

    def build(self, input_):
        for i, val in enumerate(input_):
            self.update(i, val)

    def sum_range(self, l, r):
        l, r, ans = l + self.n, r + self.n, 0
        while l <= r:
            if l % 2:
                ans += self.tree[l]
                l += 1
            if r % 2 == 0:
                ans += self.tree[r]
                r -= 1
            l, r = l // 2, r // 2
        return ans

    def update(self, i, val):
        # n = 8
        # i = 0
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]


input_ = [1, 2, 3, 4, 5]  # Example input
segment_tree = SegmentTree(input_)

print(segment_tree.tree)  # Print the tree for debugging

# Perform some updates and queries
segment_tree.update(2, 10)  # Update the value at index 2 to 10
print(segment_tree.sum_range(2, 3))  # Get the sum from index 1 to 3



