# class TreeNode:
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                tmp = node.left
                node.left = node.right
                node.right = tmp

        dfs(root)
        return root
