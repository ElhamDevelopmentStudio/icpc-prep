class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

    def diameter(self, node_a, node_b):
        self.diameter = 0 # type: ignore
        self._diameter(node_a, node_b)
        return self.diameter

    def _diameter(self, node_a, node_b):
        if node_a is None or node_b is None:
            return 0
        if node_a == node_b:
            return 0
        left_height = self._height(node_a, node_b)
        right_height = self._height(node_b, node_a)
        self.diameter = max(self.diameter, left_height + right_height) # type: ignore
        self._diameter(node_a.left, node_b)
        self._diameter(node_a.right, node_b)

    def _height(self, node_a, node_b):
        if node_a is None or node_b is None:
            return 0
        if node_a == node_b:
            return 1
        left_height = self._height(node_a.left, node_b)
        right_height = self._height(node_a.right, node_b)
        return 1 + max(left_height, right_height)

# Example usage:
tree = Tree()
node_right = Node(2)
node_left = Node(1)
tree.insert(1)
tree.insert(2)
node_a = tree.root.left # type: ignore
node_b = tree.root.right # type: ignore
print(tree.diameter(node_a, node_b))  # Output: 3