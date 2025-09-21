class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self.__to_str = ""

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def _delete(self, parent: Node, node: Node, direction):
        num_of_childs = 0
        if node.left: num_of_childs += 1
        if node.right: num_of_childs += 1

        if num_of_childs == 0:
            # Node is a leaf
            if parent:
                if direction == "left":
                    parent.left = None
                elif direction == "right":
                    parent.right = None
            else:
                # Deleting root node
                self.root = None

        elif num_of_childs == 1:
            # Node has one child
            child = node.left if node.left else node.right
            if parent:
                if direction == "left":
                    parent.left = child
                elif direction == "right":
                    parent.right = child
            else:
                # Deleting root node
                self.root = child

        elif num_of_childs == 2:
            # Node has two children
            succ_parent = node
            successor = node.right
            while successor.left:
                succ_parent = successor
                successor = successor.left

            # Replace node's data with successor's data
            node.data = successor.data

            # Delete the successor node
            if succ_parent.left == successor:
                succ_parent.left = successor.right
            else:
                succ_parent.right = successor.right

    def delete(self, value):
        parent_info = self._parent(self.root, value)
        if parent_info is None:
            if self.root and self.root.data == value:
                # Deleting the root node
                self._delete(None, self.root, None)
            else:
                return None  # Node not found
        else:
            parent, node, direction = parent_info
            self._delete(parent, node, direction)

    def _parent(self, node, data):
        if node is None:
            return None
        if node.left and node.left.data == data:
            return node, node.left, "left"
        if node.right and node.right.data == data:
            return node, node.right, "right"
        if data < node.data:
            return self._parent(node.left, data)
        elif data > node.data:
            return self._parent(node.right, data)
        else:
            # The node is the root (no parent)
            return None

    def parent(self, value):
        return self._parent(self.root, value)

    def _search(self, node, data) -> Node | None:
        if node == None:
            return None
        if node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        elif data > node.data:
            return self._search(node.right, data)
        return None

    def search(self, value) -> Node | None:
        return self._search(self.root, value)

    def _to_str(self, node):
        if node is not None:
            self._to_str(node.left)
            self.__to_str += f"{node.data},"
            self._to_str(node.right)

    def __str__(self) -> str:
        self.__to_str = ""
        self._to_str(self.root)
        return self.__to_str

if __name__ == "__main__":
    bst = BST()
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    node_parent = bst.parent(3)
    print(node_parent)  # Should be None since 3 is root
    bst.delete(3)
    print(bst)

