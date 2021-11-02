# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        results = ""

        def dfs(node, results):
            if node is None:
                return

            results += str(node.val)
            dfs(node.left, results)
            dfs(node.right, results)
            if node.left is None and node.right is None:
                self.total += int(results)
                results = results[:-1]

        dfs(root, results)
        return self.total
