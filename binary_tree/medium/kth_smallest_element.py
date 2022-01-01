# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, nov, lv):
        self.nov = nov
        self.lv = lv


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node, ti, k):
            if node is None or ti.nov >= k:
                return

            dfs(node.left, ti, k)
            if ti.nov < k:
                ti.nov += 1
                ti.lv = node.val
                dfs(node.right, ti, k)

        ti = TreeInfo(0, -1)
        dfs(root, ti, k)
        return ti.lv
