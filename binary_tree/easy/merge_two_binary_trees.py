# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(t1, t2):
            if t1 is None:
                return t2
            if t2 is None:
                return t1

            tl = TreeNode(t1.val + t2.val)
            tl.left = dfs(t1.left, t2.left)
            tl.right = dfs(t1.right, t2.right)
            return tl

        return dfs(root1, root2)
