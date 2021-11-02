# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxval = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            lh = max(dfs(node.left), 0)
            rh = max(dfs(node.right), 0)
            subtree_sum = lh + rh + node.val
            self.maxval = max(self.maxval, subtree_sum)
            return max(lh, rh) + node.val

        dfs(root)
        return self.maxval
