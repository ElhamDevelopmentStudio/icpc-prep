class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

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
            if node.children:
                for child in node.children:
                    if child.value < value:
                        self._insert(child, value)
                        return
            else:
                node.children.append(Node(value))
        elif value > node.value:
            if node.children:
                for child in node.children:
                    if child.value > value:
                        self._insert(child, value)
                        return
            else:
                node.children.append(Node(value))

    def traverse(self):
        if self.root: self._traverse(self.root)

    def _traverse(self, node):
        if node:
            print(node.value)
            for child in node.children:
                self._traverse(child)

# Example usage:
tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.traverse()