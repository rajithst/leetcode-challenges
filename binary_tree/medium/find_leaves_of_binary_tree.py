# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        mem = {}

        def dfs(node):

            if node is None:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)
            mh = max(lh, rh) + 1
            if mh not in mem:
                mem[mh] = []
            mem[mh].append(node.val)
            return mh

        dfs(root)
        return mem.values()