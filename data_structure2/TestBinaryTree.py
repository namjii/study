import unittest

from data_structure2.BinaryTree import BinaryTree
from data_structure2.BinaryTree import Node


class TestBinaryTree(unittest.TestCase):

    def test_binarytree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        tree = BinaryTree(root)
        tree.traverse(root)

