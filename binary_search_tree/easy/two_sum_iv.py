# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        result = []

        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)

        dfs(root)

        p1 = 0
        p2 = len(result) - 1
        while p1 < p2:
            s = result[p1] + result[p2]
            if s == k:
                return True
            elif s < k:
                p1 += 1
            else:
                p2 -= 1
        return False
