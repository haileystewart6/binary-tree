class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a node into the binary tree."""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        current_node = self.root
        while current_node:
            if data < current_node.data:
                if not current_node.left:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def search(self, data):
        """Search for a node in the binary tree."""
        current_node = self.root
        while current_node:
            if data == current_node.data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def in_order_traversal(self, node):
        """Perform an in-order traversal of the binary tree."""
        if node.left:
            self.in_order_traversal(node.left)
        print(node.data)
        if node.right:
            self.in_order_traversal(node.right)

# Example usage
tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

# Search for a value
result = tree.search(60)
print(f"Value 60 found: {result}")

# Perform in-order traversal
print("In-order traversal:")
tree.in_order_traversal(tree.root)
