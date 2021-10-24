from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.results = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, direction):
            if node.left is None and node.right is None:
                if direction == 1:
                    return node.val
                else:
                    return 0
            total = 0
            if node.left:
                total += dfs(node.left, 1)
            if node.right:
                total += dfs(node.right, 2)
            return total

        return dfs(root, 0)
