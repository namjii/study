
class Node:
    left, right = None, None

    def __init__(self, data):
        self.data = data


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.left)
        print(node.data)
        self.traverse(node.right)



