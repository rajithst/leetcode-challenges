# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def identical_trees(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is not None and n2 is None:
                return False
            if n2 is not None and n1 is None:
                return False

            return (n1.val == n2.val) and identical_trees(n1.left, n2.left) and identical_trees(n1.right, n2.right)

        def check(node1, node2):
            if node2 is None:
                return True
            if node1 is None:
                return False
            if identical_trees(node1, node2):
                return True

            return check(node1.left, node2) or check(node1.right, node2)

        return check(root, subRoot)
