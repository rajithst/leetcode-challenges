# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = float("inf")
        self.mindiff = float("inf")

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def dfs(node):
            if node:
                diff = abs(node.val - target)
                if diff < self.mindiff:
                    self.ans = node.val
                    self.mindiff = diff
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.ans
