# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, pathsum):
            if node is None:
                return 0

            pathsum = pathsum * 10 + node.val
            if node.left is None and node.right is None:
                return pathsum
            return dfs(node.left, pathsum) + dfs(node.right, pathsum)

        return dfs(root, 0)
