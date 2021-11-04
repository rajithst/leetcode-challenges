# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node, target):
            if node is None:
                return 0

            l = dfs(node.left, target)
            r = dfs(node.right, target)
            if l == 1:
                node.left = None
            if r == 1:
                node.right = None

            if node.left is None and node.right is None and node.val == target:
                return 1
            # return 0

        dfs(root, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        else:
            return root
