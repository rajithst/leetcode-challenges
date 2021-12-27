# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        results = []
        cv = float("inf")

        def helper(root, target, cv):
            if root is None:
                return results

            if abs(target - root.val) < abs(target - cv) or len(results) < k:
                cv = min(cv, root.val)
                if len(results) < k:
                    results.append(cv)
                else:
                    pass
            if target > root.val:
                return helper(root.right, target, cv)
            elif target < root.val:
                return helper(root.left, target, cv)
            else:
                return cv

        return helper(root, target, cv)
