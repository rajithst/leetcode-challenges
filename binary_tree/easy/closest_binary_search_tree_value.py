# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = float("inf")
        self.mindiff = float("inf")

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def dfs(node):
            if node:
                diff = abs(node.val - target)
                if diff < self.mindiff:
                    self.ans = node.val
                    self.mindiff = diff
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.ans


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        cv = float("inf")

        def helper(root, target, cv):
            if root is None:
                return cv
            if abs(target - root.val) < abs(target - cv):
                cv = root.val
            if target > root.val:
                return helper(root.right, target, cv)
            elif target < root.val:
                return helper(root.left, target, cv)
            else:
                return cv

        return helper(root, target, cv)