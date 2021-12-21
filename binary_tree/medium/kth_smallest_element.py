# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            results.append(node.val)
            dfs(node.right)

        dfs(root)
        return results[k - 1]