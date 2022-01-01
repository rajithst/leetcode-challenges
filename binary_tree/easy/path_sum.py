# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, pathsum):
            if node is None:
                return False
            pathsum += node.val
            if pathsum == targetSum and node.left is None and node.right is None:
                return True

            return dfs(node.left, pathsum) or dfs(node.right, pathsum)

        return dfs(root, 0)
