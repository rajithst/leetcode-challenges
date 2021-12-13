# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def calc_diameter(node):
            nonlocal max_diameter
            if node is None:
                return 0

            left_height = calc_diameter(node.left)
            right_height = calc_diameter(node.right)
            max_diameter = max(max_diameter, left_height + right_height + 1)
            return max(left_height, right_height) + 1

        calc_diameter(root)
        return max_diameter - 1
