# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.result += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        dfs(root)
        return self.result
