# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_dim = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)
            self.max_dim = max(self.max_dim, lh + rh)

            return max(lh, rh) + 1

        dfs(root)
        return self.max_dim
