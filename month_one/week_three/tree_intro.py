#!.venv/bin/python
from ppbtree import *

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


"""
A TreeNode is as TreeNode(val, left, right), where:
    - val is an int
    - left is a TreeNode
    - Right is a TreeNode
"""

"""
        100
       /   \
      50   150
"""

fifty = TreeNode(50)
one_fifty = TreeNode(150)
one_hundred = TreeNode(100)

one_hundred.left = fifty
one_hundred.right = one_fifty

# print(one_hundred.left)


class Tree:
    def __init__(self, root: TreeNode = None):
        self.root = root

    def insert(self, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(val)
            return

        ptr = self.root
        prev = None

        while ptr is not None:
            prev = ptr
            if val < ptr.val:
                ptr = ptr.left
            elif val > ptr.val:
                ptr = ptr.right
            else:
                return

        if val < prev.val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

    # def _insert(self, root: TreeNode, val: int) -> TreeNode:
    #     if root is None:
    #         return TreeNode(val)

    #     if val < root.val:
    #         root.left = self._insert(root.left, val)
    #     elif val > root.val:
    #         root.right = self._insert(root.right, val)

    #     return root


our_tree = Tree()
our_tree.insert(10)

our_tree.insert(15)
our_tree.insert(3)
our_tree.insert(1)

print_tree(our_tree.root, right_child='left', left_child='right')