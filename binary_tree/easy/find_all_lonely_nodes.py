# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        ls = []

        def dfs(node):
            nonlocal ls
            if node is None:
                return -1
            lv = dfs(node.left)
            rv = dfs(node.right)
            if (lv == -1 and rv != -1):
                ls.append(rv)
            if (lv != -1 and rv == -1):
                ls.append(lv)

            return node.val

        dfs(root)
        return ls
