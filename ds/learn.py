class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for the number of keys)
        self.leaf = leaf  # True if the node is a leaf
        self.keys = []  # List of keys
        self.children = []  # List of children

    def traverse(self):
        """Prints the tree in-order (for visualization)."""
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[-1].traverse()

    def find_key(self, k):
        """Returns the index of the first key greater than or equal to k."""
        idx = 0
        while idx < len(self.keys) and self.keys[idx] < k:
            idx += 1
        return idx


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Root node
        self.t = t  # Minimum degree

    def traverse(self):
        """Print the tree in-order."""
        if self.root:
            self.root.traverse()
        print()

    def search(self, k, node=None):
        """Searches for a key in the tree."""
        if node is None:
            node = self.root
        i = node.find_key(k)
        if i < len(node.keys) and node.keys[i] == k:
            return node, i
        if node.leaf:
            return None
        return self.search(k, node.children[i])

    def delete(self, k):
        """Deletes a key from the B-tree."""
        if not self.root:
            print("The tree is empty.")
            return

        self._delete(self.root, k)

        # If the root has no keys, update the root
        if len(self.root.keys) == 0:
            if self.root.leaf:
                self.root = None  # The tree becomes empty
            else:
                self.root = self.root.children[0]  # The first child becomes the new root

    def _delete(self, node, k):
        t = self.t
        idx = node.find_key(k)

        # Case 1: The key is in this node
        if idx < len(node.keys) and node.keys[idx] == k:
            if node.leaf:
                # Case 1a: Key is in a leaf node
                node.keys.pop(idx)
            else:
                # Case 1b: Key is in an internal node
                self._delete_internal_node(node, k, idx)
        else:
            # Case 2: The key is not in this node (descend)
            if node.leaf:
                print(f"Key {k} not found in the tree.")
                return

            # Ensure the child has enough keys before descending
            flag = (idx == len(node.keys))  # Check if the key is in the last child
            if len(node.children[idx].keys) < t:
                self._fill(node, idx)

            # Descend to the correct child
            if flag and idx > len(node.keys):
                self._delete(node.children[idx - 1], k)
            else:
                self._delete(node.children[idx], k)

    def _delete_internal_node(self, node, k, idx):
        t = self.t
        if len(node.children[idx].keys) >= t:
            pred = self._get_predecessor(node, idx)
            node.keys[idx] = pred
            self._delete(node.children[idx], pred)
        elif len(node.children[idx + 1].keys) >= t:
            succ = self._get_successor(node, idx)
            node.keys[idx] = succ
            self._delete(node.children[idx + 1], succ)
        else:
            self._merge(node, idx)
            self._delete(node.children[idx], k)

    def _get_predecessor(self, node, idx):
        cur = node.children[idx]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def _get_successor(self, node, idx):
        cur = node.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def _fill(self, node, idx):
        t = self.t
        if idx > 0 and len(node.children[idx - 1].keys) >= t:
            self._borrow_from_prev(node, idx)
        elif idx < len(node.children) - 1 and len(node.children[idx + 1].keys) >= t:
            self._borrow_from_next(node, idx)
        else:
            if idx < len(node.children) - 1:
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    def _borrow_from_prev(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx - 1]
        child.keys.insert(0, node.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        node.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        node.keys[idx] = sibling.keys.pop(0)

    def _merge(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        t = self.t
        child.keys.append(node.keys[idx])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        node.keys.pop(idx)
        node.children.pop(idx + 1)


# Example Usage
b_tree = BTree(3)

# Insert keys for testing
b_tree.root.keys = [10, 20]
b_tree.root.children = [
    BTreeNode(3, True),
    BTreeNode(3, True),
    BTreeNode(3, True)
]
b_tree.root.leaf = False
b_tree.root.children[0].keys = [5, 7]
b_tree.root.children[1].keys = [12, 15]
b_tree.root.children[2].keys = [25, 30]

print("Initial B-tree:")
b_tree.traverse()

# Test deletion cases
b_tree.delete(7)  # Case 1: Delete from a leaf
print("\nAfter deleting 7:")
b_tree.traverse()

b_tree.delete(20)  # Case 2: Delete from internal node
print("\nAfter deleting 20:")
b_tree.traverse()

b_tree.delete(10)  # Case 3: Requires rebalancing
print("\nAfter deleting 10:")
b_tree.traverse()

