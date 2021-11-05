# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if q is None and p is not None:
                return False
            if p.val != q.val:
                return False

            return dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(root.left, root.right)
