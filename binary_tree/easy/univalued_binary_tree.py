# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, val):
            if node is None:
                return True

            return node.val == val and dfs(node.left, val) and dfs(node.right, val)

        return dfs(root, root.val)
