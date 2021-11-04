# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, high, low):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return dfs(node.left, node.val, low) and dfs(node.right, high, node.val)

        return dfs(root, float("inf"), float("-inf"))
