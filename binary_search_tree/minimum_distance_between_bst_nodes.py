# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.min_diff = float("inf")
        self.prev = float("-inf")

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                self.min_diff = min(self.min_diff, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        dfs(root)
        return self.min_diff